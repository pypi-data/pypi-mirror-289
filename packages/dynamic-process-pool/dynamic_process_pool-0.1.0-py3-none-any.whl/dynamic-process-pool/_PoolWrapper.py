import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import Any, Awaitable, Callable, ItemsView, List, Tuple, Optional
from uuid import UUID, uuid4
from EnhancedFuture import EnhancedFuture
from PoolTask import PoolTask
from PoolType import PoolType
from _PoolTaskQueueAndManager import _PoolTaskQueueAndManager
from _TaskStatus import _TaskStatus

#########################################################################################################
#########################################################################################################
#####  Pool Wrapper (Private)                                                                       #####
#### - This class is used to wrap the ProcessPoolExecutor and manage the tasks and users assigned to it #
#########################################################################################################
#########################################################################################################
class _PoolWrapper():

    #########################################################################################################
    #####  Initilization and Get ID                                                                     #####
    #########################################################################################################

    def __init__(self, pool_type: PoolType, num_workers: int) -> None:
        self.pool: ProcessPoolExecutor = ProcessPoolExecutor(max_workers=num_workers)
        self.pool_id: UUID = uuid4() 
        self.queue_manager: _PoolTaskQueueAndManager = _PoolTaskQueueAndManager(num_workers, self._try_start_new_task)

        self.pool_type: PoolType = pool_type
        self.event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    def get_pool_id(self) -> UUID:
        return self.pool_id
    
    #########################################################################################################
    #####  User Management                                                                              #####
    #########################################################################################################
    
    def add_user(self, user_id: str) -> None:
        self.queue_manager.add_user(user_id)

    def remove_user(self, user_id: str) -> None:
        self.queue_manager.remove_user(user_id)

    def get_user_count(self) -> int:
        return self.queue_manager.get_user_count()
   
    #########################################################################################################
    #####  Sync, Async Task Run Logic                                                                   #####
    #########################################################################################################
  
    async def run_sync_task(self, func: Callable, *args, **kwds) -> Any:
        try:
            return await self.event_loop.run_in_executor(self.pool, partial(func, *args, **kwds))
        except Exception as e:
            # logger.error(f"Error running sync task: {e}")
            raise

    def _run_async_in_executor(self, func: Callable, *args, **kwds) -> Any:
        loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            coro: Awaitable= func(*args, **kwds)
            if not asyncio.iscoroutine(coro):
                raise TypeError("The provided function is not an async function")
            result: Any = loop.run_until_complete(coro)
        except Exception as e:
            print(f"Error Running Async: {e}")
            return None
        finally:
            loop.close()
        return result
    
    async def run_async_task(self, func: Callable, *args, **kwds) -> Any:
        return await self.event_loop.run_in_executor(self.pool, 
                                                     partial(self._run_async_in_executor, 
                                                             func, *args, **kwds))
    
    #########################################################################################################
    #####  Add Tasks to Queue and Start New Tasks                                                       #####
    #########################################################################################################

    def _try_start_new_task(self) -> None:
        if not self.queue_manager.task_can_be_scheduled():
            return
        
        next_task_id: UUID = self.queue_manager.assert_pop_task()
        task: PoolTask = self.queue_manager.assert_get_task(next_task_id)
        
        future: EnhancedFuture = self.queue_manager.get_task_future(next_task_id)

        async def _task_wrapper() -> None:
            try: 
                if asyncio.iscoroutinefunction(task.func):
                    result: Any = await self.run_async_task(task.func, *task.args, **task.kwds)
                else:
                    result: Any = await self.run_sync_task(task.func, *task.args, **task.kwds)
                future.set_result(result)
            except Exception as e:
                future.set_exception(e)
        
        self.queue_manager.set_future_basic_callback(next_task_id, self._try_start_new_task)
        self.queue_manager.schedule_task_with_runner(_task_wrapper)

    def _add_task(self, task: PoolTask) -> UUID:
        if task.cost is None:
            task.cost = self.get_task_cost()
        
        self.queue_manager.add_task(task, try_schedule=True)
        
        return task.task_id  #will likely return before task is even added to pool due to run_in_executor
    
    #########################################################################################################
    #####  Add Tasks & Batches to Pool and Waiters                                                      #####
    #TODO: Add _add_batch_tasks method / chunksize: might not be possible because no map function in asyncio and might not help since tasks are variable length
    #########################################################################################################
    
    def add_task_get_future(self, task: PoolTask) -> Tuple[UUID, EnhancedFuture]:
        task_id: UUID = self._add_task(task)
        return (task_id, self.queue_manager.get_task_future(task_id))
    
    async def add_task_and_wait(self, task: PoolTask) -> Any:
        return await self.add_task_get_future(task)[1]
    
    def add_batch_tasks_get_futures(self, tasks: List[PoolTask]) -> List[Tuple[UUID, EnhancedFuture]]:
        task_ids: List[UUID] = [self._add_task(task) for task in tasks]
        return [(task_id, self.queue_manager.get_task_future(task_id) )for task_id in task_ids]

    async def add_batch_tasks_and_wait(self, tasks: List[PoolTask]) -> List[Any]:
       futures_and_ids: List[Tuple[UUID, EnhancedFuture]] = self.add_batch_tasks_get_futures(tasks)
       return await asyncio.gather(*[future for task_id, future in futures_and_ids]) 

    #########################################################################################################
    #####  Await Task Future and Get Futures                                                            #####
    #########################################################################################################

    async def get_task_result(self, task_id: UUID) -> Any:
        await self.queue_manager.aget_task_result(task_id)

    def get_all_pending_and_running_tasks(self) -> ItemsView[UUID, EnhancedFuture]:
        return self.queue_manager.get_all_futures()

    #########################################################################################################
    #####  Utilization, Worker, and Task Count Getters                                                  #####
    #########################################################################################################

    def get_utilization(self) -> float:
        return self.queue_manager.get_utilization()

    def get_pending_utilization(self) -> float:
        return self.queue_manager.get_pending_utilization()
    
    def get_active_utilization(self) -> float:
        return self.queue_manager.get_active_utilization()
    
    def get_idle_workers(self) -> int:
        return self.queue_manager.pool_utilization.idle_workers()

    def get_pending_tasks_count(self) -> int:
        return self.queue_manager.get_pending_task_count()
    
    def get_active_tasks_count(self) -> int:
        return self.queue_manager.get_active_task_count()
    
    def get_task_count(self) -> int:
        return self.queue_manager.get_task_count()
    
    def get_worker_count(self) -> int:
        return self.queue_manager.get_worker_count()


    #########################################################################################################
    #####  Determine Task Cost                                                                      #####
    #########################################################################################################
    
    def get_task_cost(self) -> float:
        #TODO Implement
        return 1.0
     

    #########################################################################################################
    #####  Shutdown Pool                                                                                #####
    #########################################################################################################

    def terminate(self) -> None:
        self.pool.shutdown(wait=True)

    #########################################################################################################
    #####  To String                                                                                    #####
    #########################################################################################################
    
    def __str__(self) -> str:
        return f"Pool ID: {self.pool_id}"
