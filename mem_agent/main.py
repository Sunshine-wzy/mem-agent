from mem_agent.chat import user_chat
from . import memory


class MemAgent:
    def __init__(self):
        self.memory = memory


def main():
    user_chat()
