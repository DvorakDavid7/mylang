from typing import List


class Stack:

    def __init__(self) -> None:
        self.data: List[str] = []

    def top(self) -> str:
        if self.data:
            return self.data[len(self.data) - 1]
        return ""

    def pop(self) -> str:
        top_value = self.top()
        self.data = self.data[:-1]
        return top_value

    def push(self, value: str):
        self.data.append(value)

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __repr__(self) -> str:
        res = ""
        for i, val in enumerate(self.data):
            res += val if i == len(self.data) - 1 else val + "\n"
        return res
