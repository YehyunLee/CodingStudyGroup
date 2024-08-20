def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    Input: nums = [1,1,1,2,2,3,3,3,3], k = 3
    Output: [3,1,2]
    :param nums:
    :param k:
    :return:
    """
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]  # bucket sort

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # Reusing value as res
