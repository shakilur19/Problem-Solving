class Solution:
    def isOpen(self, s: str) -> bool:
        return s in ['(', '{', '[']

    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', '}': '{', ']': '['}
        if not self.isOpen(s[0]):
            return False

        for i in range(len(s)):
            if self.isOpen(s[i]):
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == map.get(s[i]):
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
        