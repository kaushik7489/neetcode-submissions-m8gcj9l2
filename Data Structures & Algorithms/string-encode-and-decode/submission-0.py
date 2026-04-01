class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            result += str(len(x))
            result += "#"
            result += x
        return result

            

    def decode(self, s: str) -> List[str]:
        temp1 = 0
        count = 0
        i = 0
        result = []
        while i < len(s):
            if s[i] == "#":
                count = int(s[temp1:i])
                result.append(s[i+1:i+count+1])
                temp1 = i + count + 1
                i = i + count + 1
            else:
                i += 1
        return result



        