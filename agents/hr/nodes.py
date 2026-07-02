from langchain_core.messages import AIMessage

from agents.hr.state import HRState
from agents.hr.tools import search_company_policy


def answer_hr_question(state: HRState):
    question = state["messages"][-1].content

    answer = search_company_policy.invoke(
        {
            "question": question
        }
    )

    return {
        "messages": [
            AIMessage(content=answer)
        ]
    }
