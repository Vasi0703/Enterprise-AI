from langchain_core.messages import HumanMessage

from agent.graph import AgentGraph


class EnterpriseAgent:

    def __init__(self):

        self.graph = AgentGraph()

    def ask(self, question: str):

        config = {
            "configurable": {
                "thread_id": "enterprise-chat"
            }
        }

        response = self.graph.invoke(
            [
                HumanMessage(content=question)
            ],
            config=config
        )

        return response["messages"][-1]