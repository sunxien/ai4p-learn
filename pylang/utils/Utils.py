import os
import time

def repeat_star(count: int):
    return "*" * count

def current_datetime():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', local_time)

def current_path():
    return os.path.abspath('.')

def filedir(file: str):
    return os.path.dirname(file)

def filepath(file: str):
    return os.path.abspath(file)

def filename(file: str):
    script_path = filepath(file)
    return os.path.basename(script_path)

if __name__ == "__main__":
    print(f"now(yyy-MM-dd HH:mm:ss): {current_datetime()}")
    print(f"utils(current): {current_path()}")
    print(f"utils.py(__file__): {filename(__file__)}")
    print(f"utils.py(__file__): {filepath(__file__)}")
    print(f"utils.py(__file__): {filedir(__file__)}")
    print(f"utils.py(repeat): {repeat_star(16)}")