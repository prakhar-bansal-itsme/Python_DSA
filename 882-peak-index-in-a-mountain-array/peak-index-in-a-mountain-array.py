class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            # We are on the increasing slope
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            # We are on the decreasing slope or at the peak
            else:
                r = mid

        return l