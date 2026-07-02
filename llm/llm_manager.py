from langchain_ollama import ChatOllama

from config.settings import MODEL_NAME, TEMPERATURE


class LLMManager:

    def __init__(self):
        self.llm = ChatOllama(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def ask(self, prompt):
        return self.llm.invoke(prompt)

    def get_llm(self):
        return self.llm
