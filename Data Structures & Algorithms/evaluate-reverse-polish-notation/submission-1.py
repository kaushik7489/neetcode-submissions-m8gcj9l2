class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ("+", "-", "*", "/")
        nums = []
        for i in tokens:
            if i not in op:
                nums.append(i)
            elif i in op:
                if i == "+":
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(y+x)
                elif i == "-":
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(y-x)
                elif i == "*":
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(y*x)
                elif i == "/":
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(int(y/x))
        return int(nums.pop())
        