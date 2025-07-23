import random
import threading
from time import sleep


def execute(args:()):
    t_name = threading.current_thread().name
    # print(threading.current_thread().daemon)
    # print(f"Thread: [{t_name}] (args: {args}) is starting....")
    sleep(random.randint(1,2)+1)
    print(f"Thread: [{t_name}] (args: {args}) is finished")

def create_thread_pool(pool_size: int, thread_name_prefix: str, func: callable, *args):
    if not thread_name_prefix or thread_name_prefix.strip() == "":
        thread_name_prefix = "thread-"
    elif not thread_name_prefix.strip().endswith("-"):
        thread_name_prefix = thread_name_prefix.strip() + "-"

    threads = []
    for i in range(0, pool_size):
        thread = threading.Thread(
            target=func,
            name=f"{thread_name_prefix}{i}",
            args=args,  # This is a tuple
            daemon=False
        )
        threads.append(thread)
    return threads

def start_thread_pool(threads: list[threading.Thread]):
    for index, thread in enumerate(threads):
        thread.start()
        print(f"Thread: [{thread.name}] is started")

def wait_terminate(threads: list[threading.Thread]):
    for index, thread in enumerate(threads):
        thread.join()
        print(f"Thread: [{thread.name}] is finished")

def shutdown_thread_pool(threads: list[threading.Thread]):
    for index, thread in enumerate(threads):
        if thread.is_alive():

            print(f"Thread: [{thread.name}] is shutdown")
        else:
            print(f"Ignore shutdown thread: [{thread.name}] as it's dead")

# 1. 停止线程，使用全局变量
# 2. 停止线程，传递threading.Event参数到被调用函数
if __name__ == "__main__":
    new_threads = create_thread_pool(5, None, execute, ("Hello", ))
    start_thread_pool(new_threads)
    wait_terminate(new_threads)