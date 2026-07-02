from urllib import response

from agents.enterprise_agent import EnterpriseAgent
from utils.logger import logger
from utils.trace import trace


def main():
    agent = EnterpriseAgent()

    print("\nEnterprise Multi-Agent Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        trace("USER")
        logger.info(f"Question: {question}")

        if question.lower() == "exit":
            break

        response = agent.ask(question)

        trace("FINAL RESPONSE")
        logger.info(response.content)

        print("\nAssistant:\n")
        print(response.content)
        print()


if __name__ == "__main__":
    main()
