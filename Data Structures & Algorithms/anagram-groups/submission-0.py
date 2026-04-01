class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for s in strs:
            count = [0] * 26
            for x in s:
                index = ord(x) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in freq:
                freq[key].append(s)
            else:
                freq[key] = [s]
        return list(freq.values())

        