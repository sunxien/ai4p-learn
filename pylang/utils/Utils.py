import os
import time

def repeat_star(count: int):
    return "*" * count

def current_datetime():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', local_time)

def current_dir():
    return os.path.abspath('.')

def parent_dir(current_path: str):
    return os.path.abspath(os.path.join(current_path, os.pardir))

def join_paths(path1, *paths: str):
    return os.path.join(path1, *paths)

def filedir(file: str):
    return os.path.dirname(file)

def filepath(file: str):
    return os.path.abspath(file)

def filename(file: str):
    script_path = filepath(file)
    return os.path.basename(script_path)

if __name__ == "__main__":
    print(f"now(yyy-MM-dd HH:mm:ss): {current_datetime()}")
    print(f"utils(current): {current_dir()}")
    print(f"utils.py(__file__): {filename(__file__)}")
    print(f"utils.py(__file__): {filepath(__file__)}")
    print(f"utils.py(__file__): {filedir(__file__)}")
    print(f"utils.py(repeat): {repeat_star(16)}")