class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """
        Assume the input is sorted
        Given an array of integers numbers that is already sorted in non-decreasing order,
        find two numbers such that they add up to a specific target number.
        Example:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        :param numbers:
        :param target:
        :return:
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        # Space complexity: O(1)
        # Time complexity: O(n)

        # Calc. target and inc. l or dec. r
