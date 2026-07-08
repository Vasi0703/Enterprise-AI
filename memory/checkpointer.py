import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver


class Checkpointer:

    def __init__(self):

        conn = sqlite3.connect(
            "checkpoints.db",
            check_same_thread=False
        )

        self.checkpointer = SqliteSaver(conn)

    def get(self):

        return self.checkpointer