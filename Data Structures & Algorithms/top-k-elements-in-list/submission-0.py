class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqList = [[] for i in range(len(nums) + 1)]

        for element in nums:
            count[element] = 1 + count.get(element, 0)
        for num, cnt in count.items():
            freqList[cnt].append(num)

        res = []
        for freq in range(len(freqList) - 1, 0, -1):
            for num in freqList[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        