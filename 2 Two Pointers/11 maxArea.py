class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
        Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
        Notice that you may not slant the container.
        Example:
        Input: height = [1,7,2,5,4,7,3,6]
        Output: 36
        :param heights:
        :return:
        """
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