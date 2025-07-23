import concurrent.futures
import multiprocessing
import os
import time

def worker(index):
    pid = os.getpid()
    print(f"Process: [pid:{pid}] args: {index} is starting....")
    time.sleep(100)
    # print(f"Process: [pid: {pid}] args: {index} is finished")
    return pid


def run_subprocess(process_count: int):
    with concurrent.futures.ProcessPoolExecutor(
            max_workers=5,
            # mp_context=None,
            # initializer=None,
            # initargs=()
    ) as executor:
        futures = [executor.submit(worker, i) for i in range(process_count)]
        concurrent.futures.wait(futures)
        print("All processes are finished")
        # executor.shutdown(wait=True)

def map_subprocess(process_count: int):
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(worker, range(process_count))
        print(f"PIDs: [{results}]")

# The "freeze_support()" line can be omitted if the program is not going to be frozen to produce an executable.
# Solution 1:  add freeze_support()
if __name__ == "__main__":
    # from multiprocessing import freeze_support
    # freeze_support()
    # run_subprocess(5)
    map_subprocess(5)


# # The "freeze_support()" line can be omitted if the program is not going to be frozen to produce an executable.
# # Solution 2:  move code block into `if __name__ == '__main__':` scope
# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor(
#             max_workers=5,
#             # mp_context=None,
#             # initializer=None,
#             # initargs=()
#     ) as executor:
#         futures = [executor.submit(worker, i) for i in range(2)]
#         concurrent.futures.wait(futures)
#         print("All processes are finished")