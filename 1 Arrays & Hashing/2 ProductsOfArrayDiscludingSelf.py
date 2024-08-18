def productExceptSelf(nums: list[int]) -> list[int]:
    # final = [1] * len(nums)  # len nums = 5; final len 5 [1, 1, ..]
    # for number in range(0, len(nums)):
    #     for others in range(0, len(nums)):
    #         if number != others:
    #             final[number] *= nums[others]
    # return final

    # final = [1] * len(nums)
    # for i in range(len(nums)):
    #     prefix = 1
    #     for j in range(0, i):
    #         prefix *= nums[j]
    #     postfix = 1
    #     for k in range(i + 1, len(nums)):
    #         postfix *= nums[k]
    #     final[i] = prefix * postfix
    # return final

    final = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        final[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        final[i] *= postfix
        postfix *= nums[i]
    return final

    # Prefix and postfix


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
