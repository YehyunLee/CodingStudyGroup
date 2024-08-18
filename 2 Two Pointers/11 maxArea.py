class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))  # height * width
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1

        return res

        # Use max()

        # Time complexity: O(n)
        # Space complexity: O(1)