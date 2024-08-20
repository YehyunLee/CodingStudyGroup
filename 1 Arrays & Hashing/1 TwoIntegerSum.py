def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    :param nums:
    :param target:
    :return:
    """
    # for i in range(0, len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    prevMap = {}  # value:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []

    # Use target (diff)


print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
