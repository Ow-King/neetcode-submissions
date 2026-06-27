class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        f_num = {}
        output = 0

        for num in nums:
            f_num[num] = True

        for num in nums:
            if not f_num.get(num-1):
                i = 0
                streak = 0
                while f_num.get(num + i):
                    streak += 1
                    i += 1
                if streak > output:
                    output = streak
                streak = 0
        return output
        
