import os

from dotenv import load_dotenv

load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

from langchain.agents import create_agent
from langchain_openai.chat_models import ChatOpenAI


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


model = ChatOpenAI(
    model="deepseek-chat",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

agent = create_agent(
    model=model,
    # tools=[get_weather],
    system_prompt="You are a helpful document assistant who can answer questions based on the documents specified by users. "
                  "If you can't answer a question, "
                  "just say you don't know. "
                  "Don't answer randomly."
                  "Answer in Chinese.",
)

state = [
    {"role": "assistant", "content": "承运商应付月结审核成功发送数据生产分摊数据处理，在分摊数据处理页面点击生成分摊账单，"
                                     "即发送消息，后台任务监听到该消息后执行生成分摊账单任务，最后保存分摊账单"}
]


# state.append({"role": "user", "content": "派件费是如何产生的？"})
# state.append({"role": "user", "content": "你还挺专业嘛"})

def call_llm(input):
    state.append({"role": "user", "content": input})
    for token, metadata in agent.stream(
            {"messages": state},
            stream_mode="messages",
    ):
        for content in token.content_blocks:
            if content:
                yield content['text']
