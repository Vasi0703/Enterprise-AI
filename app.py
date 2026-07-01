from rag.rag_pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline("data/pdfs/hr.pdf")

    pipeline.build()

    print("\nEnterprise AI Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        response = pipeline.ask(question)

        print("\nAssistant:\n")

        print(response.content)

        print()


if __name__ == "__main__":
    main()