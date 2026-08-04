class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterMaxs = {}
        for i in range(len(s)):
            char = s[i]
            letterMaxs[char] = i

        output = []
        lastIndex = 0
        start = 0

        for i in range(len(s)):
            char = s[i]
            lastIndex = max(lastIndex, letterMaxs[char])

            if i == lastIndex:
                output.append(lastIndex - start + 1)
                start = i + 1
            
        return output
            
