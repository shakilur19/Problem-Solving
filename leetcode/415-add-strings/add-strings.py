class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))

        num1 = f"{num1:0>{max_len}}"
        num2 = f"{num2:0>{max_len}}"
        print(num1, num2)
        i = max_len -1
        str_ans = ""
        value = 0

        while i != -1:
            a = int(num1[i])
            b = int(num2[i])
            value += a + b
            value, reminder = divmod(value, 10)
            i -= 1
            str_ans += str(reminder)

        while value > 0:
            value, reminder = divmod(value, 10)
            str_ans += str(reminder)

        return str_ans[::-1]