from agents.supervisor.graph import SupervisorGraph
from langchain_core.messages import HumanMessage


class EnterpriseAgent:

    def __init__(self):
        self.graph = SupervisorGraph()

    def ask(self, question: str):
        config = {
            "configurable": {
                "thread_id": "enterprise-assistant"
            }
        }

        response = self.graph.invoke(
            [HumanMessage(content=question)],
            config=config
        )

        return response["messages"][-1]
