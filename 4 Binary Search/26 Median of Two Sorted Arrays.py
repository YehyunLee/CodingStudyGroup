class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Init
        A, B = nums1, nums2  # Lists
        total = len(nums1) + len(nums2)  # Total length combined
        half = total // 2  # Half length

        if len(B) < len(A):
            A, B = B, A
            # Ensure A is the shorter list

        # Assume A is smaller List
        # For example A: [1, 2], B: [3, 4, 5]
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Midpoint of A
            j = half - i - 2  # - 2 because 2 lists

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
