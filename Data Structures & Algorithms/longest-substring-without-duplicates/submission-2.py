class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        check = set()
        longest = 0
        i = 0
        while i < len(s):
            if substr == "":
                substr += s[i]
                check.add(s[i])
                if len(substr) > longest:
                    longest = len(substr)
                i += 1
            elif s[i] in check:
                if len(substr) > longest:
                    longest = len(substr)
                temp = substr.index(s[i])
                substr = substr[temp + 1::]
                substr += s[i]
                check = set(substr)
                i += 1
            else:
                substr += s[i]
                check.add(s[i])
                if len(substr) > longest:
                    longest = len(substr)
                i += 1
        return longest