class Solution:
    def trap(self, height: List[int]) -> int:
        opt = []
        grb = [] # Greatest value to the right of a column
        grb_val = 0

        for x in range(len(height)):
            grb.insert(0, grb_val)
            if height[len(height) - 1 - x] > grb_val:
                grb_val = height[len(height) - 1 - x]
                

        result = 0
        for x in range(len(height) - 1):
            if x == 0:
                opt.append(0)
                continue
            water = max(0, height[x-1] + opt[x-1] - height[x])

            # Check if there is something to bound on the right
            if (height[x] + water) > grb[x]:
                water = max(0, grb[x] - height[x])

            opt.append(water)
            result = result + water
        
        return result

            
            