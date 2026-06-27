class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordHash = defaultdict(list)

        for word in strs:
            freqLetter = [0] * 26
            for letter in word:
                freqLetter[ord(letter) - ord('a')] += 1

            wordHash[tuple(freqLetter)].append(word)

        return list(wordHash.values())