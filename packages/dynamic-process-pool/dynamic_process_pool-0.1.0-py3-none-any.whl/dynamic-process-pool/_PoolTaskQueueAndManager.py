import math
import time
from queue import Queue
from typing import Any, Callable, Dict, ItemsView, Optional, Set
from uuid import UUID
import asyncio

from _PoolUtilization import _PoolUtilization
from PoolTask import PoolTask
from EnhancedFuture import EnhancedFuture
from _TaskStatus import _TaskStatus



    #########################################################################################################
    #########################################################################################################
    #####  _PoolTaskQueueAndManager (Private):
    ##### - Manages the queue of tasks and the running tasks of the pool  ######
    #########################################################################################################
    #########################################################################################################

    # Tiebreaker: SJF and WSPT Scheduling (minimizing AVERAGE wait time) -> tasks are ran in order of submission for each user: TODO: add priority later?
    # (1) Choose user with less currently running tasks (prevent monopolization of WORKERS)
    # (2) choose user with least cost of task (improve system throughput) + (3) Choose user with longest wait time within epsilon (prevent starvation) (based on herustic)
    # (4) Choose user with least amount of tasks in queue (prevent future monopolization of WORKERS)
    # (5) choose user who has been waiting longest since LAST task (TODO: implement fully, currently will just select person who did not finish last)
    # (6) Alphabetic order

class _PoolTaskQueueAndManager: # not actually a queue
    #########################################################################################################
    #####  Constants
    #########################################################################################################
    
    MAXIMIM_QUEUE_SIZE: int = -1
    EPSILON_HEURISTIC: float = 2.0

    #########################################################################################################
    #####  Init
    #########################################################################################################
    
    def __init__(self, max_workers: int, attempt_scheduler: Optional[Callable] = None) -> None:
        self.pending_tasks: Dict[str, Queue[UUID]] = {} # user_id -> List[PoolTask], most effecient I can think of, List[] #TODO: convert to Queue
        self.running_tasks: Dict[str, Set[UUID]] = {} # user_id -> List[PoolTask]

        self.task_futures: Dict[UUID, EnhancedFuture] = {} # task_id -> EnhancedFuture
        self.tasks: Dict[UUID, PoolTask] = {} # task_id -> PoolTask

        self.pool_utilization: _PoolUtilization = _PoolUtilization(max_workers)
        self.users: Set[str] = set()

        self.attempt_scheduler = attempt_scheduler

    #########################################################################################################
    #####  Priority Heuristics
    #########################################################################################################
    
    def _wait_cost_heuristic(self, wait_time: float, wait_max: float, cost_of_task: float, cost_max: float) -> float:
        # change to exponential increase after waiting for more than half the cost, otherwise linear, all in one equation
        # assume cost is in seconds to run task
        #UNIT_OF_TIME = 10 # 10 SECONDS
        #return (cost_of_task / UNIT_OF_TIME) + (wait_time // UNIT_OF_TIME + 1) * ((1.05) ** (wait_time / UNIT_OF_TIME))
        
        # example ranking
        # wait_time, cost
        # 1000, 50
        # 200, 10
        # 300, 40
        # 1500, 60
        # 800, 20
        COST_WEIGHT: float = 0.5
        WAIT_WEIGHT: float  = 0.5
        wait_score: float = WAIT_WEIGHT * (math.exp(wait_time / wait_max)) 
        cost_score: float = COST_WEIGHT * math.log10(cost_max / (cost_of_task + math.pow(10, -2)) + 1)
        score: float = wait_score + cost_score
        return score
    
    #########################################################################################################
    #####  Task Priority Helper Functons
    #########################################################################################################
    
    def _get_worker_usage(self, user_id: str) -> int:
        return len(self.running_tasks[user_id]) if user_id in self.running_tasks else 0

    def _get_running_cost_of_user(self, user_id: str) -> float:
        sum = 0
        if user_id in self.running_tasks:
            for task_id in self.running_tasks[user_id]:
                if self.tasks[task_id].cost is not None:
                    sum += self.tasks[task_id].get_cost()
        return sum
    
    def _get_longest_wait_time(self, user_id: str, compare_time: float = time.time()) -> float:
        return compare_time - self.tasks[self.pending_tasks[user_id].queue[0]].queue_time

    def _get_highest_cost_task_of_user(self, user_id: str) -> float:
        if user_id not in self.pending_tasks:
            return 0
        max_cost: float = 0
        for task_id in list(self.pending_tasks[user_id].queue):
            if self.tasks[task_id].cost is not None and self.tasks[task_id].get_cost() > max_cost:
                max_cost = self.tasks[task_id].get_cost()
        return max_cost
    
    #########################################################################################################
    #####  Priority Queue Pop Next Task
    #########################################################################################################
   
    def pop_next_task(self, set_task_status: bool = True, last_finisher: Optional[str] = None) -> Optional[UUID]:
        if len(self.pending_tasks) == 0:
            return None
        
        def is_current_worse(compare: str, current_best: str) -> bool:
            current_worker_usage: float = self._get_worker_usage(current_best)
            compare_worker_usage: float = self._get_worker_usage(compare)

            if compare_worker_usage != current_worker_usage:
                return compare_worker_usage < current_worker_usage
        
            highest_wait_time_across_all_users: float = max([self._get_longest_wait_time(user) for user in self.pending_tasks.keys()])
            highest_task_cost_across_all_users: float = max([self._get_highest_cost_task_of_user(user) for user in self.pending_tasks.keys()])

            current_user_cost: float = 0
            if self.tasks[self.pending_tasks[current_best].queue[0]].get_cost() is not None:
                current_user_cost = self.tasks[self.pending_tasks[current_best].queue[0]].get_cost()
            heuristic_score_current: float = self._wait_cost_heuristic(self._get_longest_wait_time(current_best), highest_wait_time_across_all_users, current_user_cost, highest_task_cost_across_all_users)

            compare_user_cost: float = 0
            if self.tasks[self.pending_tasks[compare].queue[0]].get_cost() is not None:
                compare_user_cost = self.tasks[self.pending_tasks[compare].queue[0]].get_cost()
            
            heuristic_score_compare: float = self._wait_cost_heuristic(self._get_longest_wait_time(compare), highest_wait_time_across_all_users, compare_user_cost, highest_task_cost_across_all_users)

            if abs(heuristic_score_compare - heuristic_score_current) < _PoolTaskQueueAndManager.EPSILON_HEURISTIC:
                return heuristic_score_compare > heuristic_score_current
            
            if self.pending_tasks[compare].qsize() != self.pending_tasks[current_best].qsize():
                return self.pending_tasks[compare].qsize() < self.pending_tasks[current_best].qsize()
            
            if last_finisher is not None:
                if last_finisher == current_best:
                    return True
                elif last_finisher == compare:
                    return False
            
            return compare < current_best #arbitrary tiebreaker
            
        # find user whose task should go next next

        user_to_retrieve_task: str = list(self.pending_tasks.keys())[0] #placeholder
        for user_id, _ in self.pending_tasks.items():
            if is_current_worse(user_id, user_to_retrieve_task):
                user_to_retrieve_task = user_id
        
        next_task: PoolTask = self.tasks[self.pending_tasks[user_to_retrieve_task].get_nowait()]
        if self.pending_tasks[user_to_retrieve_task].qsize() == 0:
            del self.pending_tasks[user_to_retrieve_task]
        if set_task_status:
            self.set_task_status(next_task.task_id, _TaskStatus.RUNNING)
            if next_task.user is not None:
                next_task.user.task_status_changed(next_task.pool_type, next_task.task_id, _TaskStatus.RUNNING)

        return next_task.task_id
    
    def pop_if_idle(self, set_task_status=True) -> Optional[UUID]:
        if self.task_can_be_scheduled():
            return self.pop_next_task(set_task_status=set_task_status)
        return None

    def assert_pop_task(self, set_next_task_status: bool = True) -> UUID:
        assert self.task_can_be_scheduled(), "Error Popping Task: No Task Can Be Scheduled"
        task_id: Optional[UUID] = self.pop_next_task(set_task_status=set_next_task_status)
        assert task_id is not None, "Error Popping Task: Task ID is None"
        return task_id

    #########################################################################################################
    #####  Add Task to Queue
    #########################################################################################################
   
    def add_task(self, task: PoolTask, try_schedule:bool=True) -> None:
        self.tasks[task.task_id] = task
        if task.user_id not in self.pending_tasks:
            self.pending_tasks[task.user_id] = Queue(maxsize=0)
        future = EnhancedFuture()
        self._set_task_future(task.task_id, future)
        # future.set_cost(task.cost)
        self.pending_tasks[task.user_id].put_nowait(task.task_id)

        if task.user is not None:
            task.user.task_status_changed(task.pool_type, task.task_id, _TaskStatus.PENDING)
        self.pool_utilization.process_changed(task.get_cost(), _TaskStatus.PENDING)

        if self.task_can_be_scheduled() and self.attempt_scheduler is not None and try_schedule:
             self.attempt_scheduler()
    
    def add_task_get_future(self, task: PoolTask, try_schedule: bool=True) -> EnhancedFuture:
        self.add_task(task, try_schedule)
        return self.get_task_future(task.task_id)
    
    async def aadd_task_wait_for_future(self, task: PoolTask, try_schedule:bool=True) -> EnhancedFuture:
        self.add_task(task, try_schedule)
        return await self.aget_task_result(task.task_id)
    #########################################################################################################
    #####  Task Status Changers
    #########################################################################################################

    def _set_task_running(self, task_id: UUID) -> None:
        task: PoolTask = self.tasks[task_id]
        user_id: str = task.user_id

        if user_id not in self.running_tasks:
            self.running_tasks[user_id] = set()
        
        task.set_start_time()
        
        self.running_tasks[user_id].add(task.task_id)
        self.pool_utilization.process_changed(task.get_cost(), _TaskStatus.RUNNING)
    
    def _set_task_finished(self, task_id: UUID) -> None:
        task_cost = self.tasks[task_id].get_cost()
        user_id: str = self.tasks[task_id].user_id
        self.tasks[task_id].set_end_time() #TODO: use elasped time?
        del self.tasks[task_id]
        # DO NOT DELTE TASK_FUTURE TO PREVENT RACE CONDITION #TODO: delete task future after 10s after it has been retrieved

        self.running_tasks[user_id].remove(task_id)

        if len(self.running_tasks[user_id]) == 0:
            del self.running_tasks[user_id]
        self.pool_utilization.process_changed(task_cost, _TaskStatus.COMPLETED)

    def set_task_status(self, task_id: UUID, status: _TaskStatus) -> None:
        if status == _TaskStatus.RUNNING:
            self._set_task_running(task_id)
        elif status == _TaskStatus.COMPLETED:
            self._set_task_finished(task_id)
        else:
            raise ValueError(f"Error Setting Task Status: {status} is not a valid task")

    def task_finished(self, task_id: UUID) -> None:
        task = self.tasks[task_id]
        self.set_task_status(task_id, _TaskStatus.COMPLETED)
        if task.user is not None:
            task.user.task_status_changed(task.pool_type, task_id, _TaskStatus.COMPLETED)

    #########################################################################################################
    #####  User Management Wrappers
    #########################################################################################################
    
    def add_user(self, user_id: str) -> None:
        self.users.add(user_id)
    
    def remove_user(self, user_id: str) -> None:
        if user_id in self.pending_tasks or user_id in self.running_tasks:
            raise ValueError(f"Error Removing User From Pool: User {user_id} has pending or running tasks")
        if user_id in self.users:
            self.users.remove(user_id)

    def get_user_count (self) -> int:
        return len(self.users)

    #########################################################################################################
    #####  Get and Set Task Futures
    #########################################################################################################

    def _set_task_future(self, task_id: UUID, future: EnhancedFuture) -> None:
        self.task_futures[task_id] = future
    
    def get_task_future(self, task_id: UUID) -> EnhancedFuture:
        return self.task_futures[task_id]

    def get_all_futures(self) -> ItemsView[UUID, EnhancedFuture]:
        return self.task_futures.items()
     
    async def aget_task_result(self, task_id: UUID) -> Any:
        if task_id not in self.task_futures:
            raise ValueError(f"Error Getting Task Result: Task {task_id} does not exist")
        return await self.get_task_future(task_id)

    def set_future_callback(self, task_id: UUID, callback) -> None:
        self.task_futures[task_id].add_done_callback(callback)

    def set_future_basic_callback(self, task_id: UUID, schedule_new_task: Optional[Callable] = None, add_callback: Optional[Callable] = None) -> None:
        def basic_callback(future: EnhancedFuture) -> None:
            result: Any = future.result() if not future.exception() else future.exception()
            if future.exception():
                print(f"Task {task_id} failed with error: {future.exception}")
            task_callback: Optional[Callable] = self.tasks[task_id].callback

            self.task_finished(task_id)

            if schedule_new_task is not None:
                schedule_new_task()

            if add_callback is not None:
                add_callback(result)
            
            if task_callback is not None:
                task_callback(result)
            
            
                

        self.set_future_callback(task_id, basic_callback)

    def schedule_task_with_runner(self, task_runner: Callable ) -> None:
        asyncio.ensure_future(task_runner())
    #########################################################################################################
    #####  Utilization Wrappers
    #########################################################################################################

    def get_worker_count(self) -> int:
        return self.pool_utilization.get_workers()
        
    def get_utilization(self) -> float:
        return self.pool_utilization.get_utilization()
    
    def get_pending_utilization(self) -> float:
        return self.pool_utilization.get_pending_utilization()

    def get_active_utilization(self) -> float:
        return self.pool_utilization.get_active_utilization()
    
    #########################################################################################################
    #####  Task and Worker Count Getters
    #########################################################################################################
   
    def get_idle_workers(self) -> int:
        return self.pool_utilization.idle_workers()

    def get_pending_task_count(self) -> int:
        return sum([self.pending_tasks[user_id].qsize() for user_id in self.pending_tasks.keys()])
    
    def get_active_task_count(self) -> int:
        return sum([len(self.running_tasks[user_id]) for user_id in self.running_tasks.keys()])
    
    def get_task_count(self):
        return self.get_pending_task_count() + self.get_active_task_count()
    
    def has_idle_workers(self) -> bool:
        return self.pool_utilization.has_idle_workers()

    def has_pending_tasks(self) -> bool:
        return len(self.pending_tasks) > 0

    def get_task(self, task_id: UUID) -> Optional[PoolTask]:
        return self.tasks.get(task_id) 
    
    def assert_get_task(self, task_id: UUID) -> PoolTask:
        task: Optional[PoolTask] = self.get_task(task_id)
        assert task is not None, f"Error Getting Task: Task {task_id} does not exist"
        return task

    def task_can_be_scheduled(self) -> bool:
        return self.has_idle_workers() and self.has_pending_tasks()

#impelment round robin
#look a thatchet
# implement for AI RAG specific 
# - for embeddings split into small cuhunks and distribute tasks
# rate liimiter + sliding window
# Batch Processing for Document Indexing: Hatchet can handle large-scale batch processing of documents, images, and other data and resume mid-job on failure.