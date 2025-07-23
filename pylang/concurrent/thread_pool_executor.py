import random
import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep

thread_pool = ThreadPoolExecutor(
    max_workers=5,
    thread_name_prefix='my-pool-thread-',
    initializer=None,
    initargs=()
)

def execute(args:()):
    t_name = threading.current_thread().name
    # print(threading.current_thread().daemon)
    # print(f"Thread: [{t_name}] (args: {args}) is starting....")
    sleep(random.randint(1,2)+1)
    print(f"Thread: [{t_name}] (args: {args}) is finished")
    return str(args[0]).upper()

future = thread_pool.submit(execute, ("Bye", ))
print(f"Result: {future.result()}")

# map-reduce
group_args = [("China",), ("America",), ("Russia",)]
results = thread_pool.map(execute, group_args)
for result in results:
    print(f"Result: {result}")

thread_pool.shutdown(wait=True)
print(f"Thread pool is shutdown")

# RuntimeError: cannot schedule new futures after shutdown
# future = thread_pool.submit(execute, ("Bye", ))
