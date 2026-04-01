class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        valid = []
        opened = ["(", "{", "["]
        closed = [")", "}", "]"]
        pairs = {"(" : ")",
        "{" : "}",
        "[" : "]"    
        }
        while i < len(s):
            if s[i] in opened:
                valid.append(s[i])
                i += 1
            elif s[i] in closed:
                if len(valid) == 0:
                    return False
                elif pairs[valid[-1]] == s[i]:
                    valid.pop()
                    i += 1
                else:
                    return False
            else:
                return False
        return len(valid) == 0

        