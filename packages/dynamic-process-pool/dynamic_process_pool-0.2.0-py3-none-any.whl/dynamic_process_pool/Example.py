import asyncio
import time
import multiprocessing as mp
from PoolType import PoolType
from DynamicProcessPoolManager import DynamicProcessPoolManager
from DynamicPoolConfig import DynamicPoolConfig
from PoolTask import PoolTask


# Example usage
def example_sync_task(x):
    time.sleep(3)
    # print(x ** x)
    print(x)

async def example_async_task(x):
    await asyncio.sleep(3)
    print(x * x)
    return 0

async def async_task():
    for i in range(1000000):
        pass
    # await asyncio.sleep(0.01)

def func():
    for i in range(1000000):
        pass
    # time.sleep(0.01)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

async def limit_test():
    config: DynamicPoolConfig = DynamicPoolConfig()
    config.set_config(PoolType.HEAVY, 1, 8)
    manager: DynamicProcessPoolManager = DynamicProcessPoolManager(config=config)

    import time

    start = time.time()
    ROUNDS = 1500 #10K is MUCHH Slower, create batches??
    BATCH_SIZE = 20
    for i in range((ROUNDS // BATCH_SIZE)):
        tasks = [async_task() for i in range(BATCH_SIZE)]
        await asyncio.gather(*tasks)
    
    end = time.time()
    default_time = end - start

    print("Default time: ", round(default_time, 2)  , "s")

    start = time.time()


    for i in range(ROUNDS // BATCH_SIZE):
        tasks = [manager.add_task(PoolTask("user1", PoolType.HEAVY, None, func, None)) for i in range(BATCH_SIZE)]
        await asyncio.gather(*tasks)
        await manager.wait_on_all_futures_of_user("user1")
    end = time.time()
    pool_time = end - start

    print("Pool time: ", round(pool_time, 2) , "s")
    print("")

    if pool_time > default_time:
        print("BENCHMARK: Pool is " + bcolors.FAIL + "SLOWER" + bcolors.ENDC + " than default")
        print("Overhead: ", str(round(pool_time - default_time, 2)) + "s")
        print("Overhead per call: ", str(round((pool_time - default_time) / ROUNDS, 2)) + "s")
        print("Overhead ratio", str(round(pool_time / default_time, 2)) +"x")
    else:
        print("BENCHMARK: Pool is " + bcolors.OKGREEN + "FASTER" + bcolors.ENDC + " than default")
        print("Speedup: ", str(round(pool_time - default_time, 2)) + "s")
        print("Speedup per call: ", str(round((default_time - pool_time) / ROUNDS, 2)) + "s")
        print("Speedup ratio", str(round(default_time / pool_time, 2)) + "x")

async def main() -> None:
    config: DynamicPoolConfig = DynamicPoolConfig()
    config.set_config(PoolType.HEAVY, 3, 2)
    config.set_config(PoolType.EXPRESS, 1, 2)
    manager: DynamicProcessPoolManager = DynamicProcessPoolManager(config=config)
    CPU_COUNT: int = mp.cpu_count()

    # await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 5))
    # await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 5))
    # await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 5))
    # await manager.add_task(PoolTask("user2", PoolType.HEAVY, None, example_sync_task, None, 5))

    await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 1))
    await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 1))
    await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 1))
    await manager.add_task(PoolTask("user1", PoolType.HEAVY, None, example_sync_task, None, 1))

    await manager.add_task(PoolTask("user2", PoolType.HEAVY, None, example_sync_task, None, 2))
    await manager.add_task(PoolTask("user2", PoolType.HEAVY, None, example_sync_task, None, 2))

    await manager.add_task(PoolTask("user3", PoolType.HEAVY, None, example_sync_task, None, 3))
    await manager.add_task(PoolTask("user3", PoolType.HEAVY, None, example_sync_task, None, 3))

    await manager.add_task(PoolTask("user4", PoolType.HEAVY, None, example_sync_task, None, 4))

    # await manager.add_task(PoolTask("user10", PoolType.EXPRESS, None, example_sync_task, None, 10))
    # await manager.add_task(PoolTask("user11", PoolType.EXPRESS, None, example_sync_task, None, 11))
    # await manager.add_task(PoolTask("user12", PoolType.EXPRESS, None, example_sync_task, None, 12))

    await manager.close_all_pools()


    # await asyncio.sleep(10)



if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(limit_test())


