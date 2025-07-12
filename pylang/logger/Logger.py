import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s:%(thread)d] %(levelname)s %(filename)s[:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    # filename="ai4p-learn.log"
)

def get_root_logger():
    return logging

def get_logger(logger_name: str):
    return logging.getLogger(logger_name)

if __name__ == "__main__":
    logger = get_root_logger()
    logger.info("Hello World")