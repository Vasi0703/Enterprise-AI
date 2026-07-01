from langchain_ollama import ChatOllama
from agent.tools import calculator

from config.settings import MODEL_NAME, TEMPERATURE


class LLMManager:

    def __init__(self):

        self.llm = ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
        ).bind_tools([calculator])

    def ask(self, prompt: str):

        return self.llm.invoke(prompt)