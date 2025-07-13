# Current Project Modules
from pylang.logger import Logger

logger = Logger.get_root_logger()

def start_chat():
    while True:
        try:
            question = input("请输入您想咨询的问题：")
            # TODO

            print(f"您咨询的问题是：\"{question}\"，但是我还没有完成后续的开发工作。。。")
        except Exception as e:
            print(f"[{type(e).__name__}] 你竟然一个问题把我问倒了。。。{e.args}")

# Main: Hello, this is AI for Python Developers!
if __name__ == "__main__":
    start_chat()