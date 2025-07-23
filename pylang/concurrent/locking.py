import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from pylang.concurrent.multi_threading import create_thread_pool, start_thread_pool, wait_terminate


# ************************* Unsafe Region *********************
unsafe_total = 0
def sum_unsafe(limit: int):
    global unsafe_total
    for i in range(limit):
        unsafe_total += 1

# ************************* Safe Region ************************
mutex = Lock()
safe_total = 0
def sum(limit: int):
    mutex.acquire()
    try:
        global safe_total
        for i in range(limit):
            safe_total += 1
    finally:
        mutex.release()


if __name__ == "__main__":

    while True:
        # Safe
        thread_pool_for_safe = ThreadPoolExecutor(
            max_workers=16,
            thread_name_prefix='my-pool-thread-',
            initializer=None,
            initargs=()
        )
        thread_pool_for_safe.submit(sum, 10000000)
        thread_pool_for_safe.shutdown(wait=True)
        print(f"Global safe total: {safe_total}")

        # Unsafe
        thread_pool_for_unsafe = ThreadPoolExecutor(
            max_workers=16,
            thread_name_prefix='my-pool-thread-',
            initializer=None,
            initargs=()
        )
        thread_pool_for_unsafe.submit(sum_unsafe, 10000000)
        thread_pool_for_unsafe.shutdown(wait=True)
        print(f"Global unsafe total: {unsafe_total}")