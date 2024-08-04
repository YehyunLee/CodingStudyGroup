class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # Time complexity: O(n) HOW?? I was thinking of O(n^2)
        # This is because we only enter the while loop when we find the start of a sequence
        # Because of (n - 1) not in numSet

        # Space complexity: O(n)

        # Core idea is to check if n - 1 is in the set and while loop of n + length in set
