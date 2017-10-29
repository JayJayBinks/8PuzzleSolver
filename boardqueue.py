from collections import deque

class BoardQueue(deque):
    def pop(self):
        return self.popleft()

    def empty(self):
        return len(self) == 0
