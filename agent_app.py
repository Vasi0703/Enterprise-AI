from agent.agent import EnterpriseAgent


def main():

    agent = EnterpriseAgent()

    print("\nEnterprise Agent Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        response = agent.ask(question)

        print("\nAssistant:\n")

        print(response.content)

        print()


if __name__ == "__main__":
    main()