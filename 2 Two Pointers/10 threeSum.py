class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
        Example:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        :param nums:
        :return:
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Since we sorted, we need to stop, if number goes beyond 0
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:  # We skip i==0, s.t. we ensure left index exists
                # We skip duplicates
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Important
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # reason we do this is because we want to skip duplicates
                    # so that we void having the same triplet list in the result
                    # We won't get into edge case as we are sorting the list
        return res

        # Time complexity: O(n^2) + O(nlogn) => O(n^2)
        # Space complexity: O(1)

        # Conduct operations on sorted list till positive value
        # Two pointer & target usage and avoid duplicates
