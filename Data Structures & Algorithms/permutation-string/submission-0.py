class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        desiredPerm = {}
        for c in s1:
            if c not in desiredPerm:
                desiredPerm[c] = 0
            desiredPerm[c] += 1

        windowLetters = {}
        left = 0 - len(s1)

        for c in s2:
            # Add the right letter
            if c not in windowLetters:
                windowLetters[c] = 0
            windowLetters[c] += 1

            # remove the left letter to keep the window
            if left >= 0:
                windowLetters[s2[left]] -= 1
                if windowLetters[s2[left]] == 0:
                    windowLetters.pop(s2[left])
            left += 1

            # check for correctness
            if desiredPerm == windowLetters:
                return True

        return False

            
        