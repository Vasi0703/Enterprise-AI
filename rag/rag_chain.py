from typer import prompt

from llm.llm_manager import LLMManager

from utils.logger import logger


class RAGChain:

    def __init__(self, retriever):

        self.retriever = retriever

        self.llm = LLMManager()

    def ask(self, question: str):

        logger.info("Searching similar chunks...")

        documents = self.retriever.invoke(question)

        logger.info(f"Retrieved {len(documents)} relevant chunks.")

        print("\n========== RETRIEVED DOCUMENTS ==========\n")

        for i, doc in enumerate(documents):

            print(f"\n----- Chunk {i+1} -----\n")

            print(doc.page_content)

            print("\nMetadata:")

            print(doc.metadata)

            print("\n---------------------------------------")

        print("\n========================================\n")

        logger.info(f"Retrieved {len(documents)} relevant chunks.")

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        logger.info("Building prompt...")

        prompt = f"""
You are an Enterprise AI Assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, answer:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}
"""

        logger.info("Sending prompt to Llama...")

        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n=============================\n")

        response = self.llm.ask(prompt)

        logger.info("LLM response received.")

        return response