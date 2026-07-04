class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create a max heap
        heap = []
        maxOutput = []
        for i in range(len(nums)):
            # Initialize the window 
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                maxOutput.append(-heap[0][0])

        return maxOutput
