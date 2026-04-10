class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev = digits[::-1]
        arr = []
        next = True
        for i in range(len(rev)):
            if rev[i] == 9 and next:
                arr.append(0)
                next = True
            elif rev[i] < 9 and next:
                arr.append(rev[i] + 1)
                next = False
            else:
                arr.append(rev[i])
        if next:
            arr.append(1)
        return arr[::-1]