# Current Project Modules
from pylang.logger import Logger
from pylang.utils.Utils import *
from service.RAGService import *

logger = Logger.get_root_logger()

HOT_NEWS_FILE = "resources/hot_news.txt"

def init_rag_service():
    rag_service_impl = RAGService("ai4p")
    hot_news_file = join_paths(current_dir(), HOT_NEWS_FILE)
    rag_service_impl.load_documents("txt", hot_news_file)
    logger.info(f"导入1份新闻资料完成！资料名称：{hot_news_file}")
    return rag_service_impl

def start_chat_session(rs: RAGService):
    while True:
        question = ""
        try:
            print("\n")
            question = question + input("请输入您想咨询的问题：")
            related_knowledge_list = rs.search_knowledge(question)
            print(knowledge_summary(related_knowledge_list))
        except Exception as e:
            print(e)
            print('你竟然一个问题把我问倒了....')
            logger.critical(f"问题：\"{question}\" [{type(e).__name__}] {e.args}")


def knowledge_summary(knowledge_list: list) -> str:
    knowledge_count = len(knowledge_list)

    if knowledge_count == 0:
        summary = '\n' + repeat_star(128) + '\n'
        return summary + '抱歉，没有找到相关的新闻资料！\n'

    summary = '\n已经为您找到 ' + str(knowledge_count) + ' 条相关的新闻。如下所示：'
    summary = summary + '\n' + repeat_star(128) + '\n'
    for (index, knowledge) in enumerate(knowledge_list):
        summary = summary + '【第 ' + str(index + 1) + ' 条新闻】'
        summary = summary + knowledge.page_content + '\n\n'

    return summary + repeat_star(128) + '\n>> 所有相关的新闻已经全部显示完毕。' + current_datetime()

# Main: Hello, this is AI for Python Developers!
if __name__ == "__main__":
    rsi = init_rag_service()
    start_chat_session(rsi)