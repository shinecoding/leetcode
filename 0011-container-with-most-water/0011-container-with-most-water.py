class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[r], height[l]) * (r - l)
            res = max(res, area)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res
