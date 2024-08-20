from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    :param strs:
    :return:
    """
    ans = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1  # Such that every index is 0~25
        ans[tuple(count)].append(s)
    return ans.values()

    # Use ord substraction

    # run time is O(m * n)
