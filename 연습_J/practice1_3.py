# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution(object):
    def __init__(self):
        self.tmplist = []

    def push(self, value):
        self.tmplist.append(value)

    def top(self):
        # 스택이 비어있지 않다면
        if not len(self.tmplist) == 0:
            # 제거하지 않고 맨위 요소 반환
            return self.tmplist[-1]
        # 스택이 비어있으면
        else:
            # 0 반환
            return 0

    def pop(self):
        # 스택이 비어있지 않다면
        if not len(self.tmplist) == 0:
            # pop하여 맨위 요소 제거
            return self.tmplist.pop()

    def begin(self):
        pass

    def rollback(self):
        if not len(self.tmplist) == 0:
            return True
        else:
            return False

    def commit(self):
        if not len(self.tmplist) == 0:
            return True
        else:
            return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"


test()