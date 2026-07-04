class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = set(nums1)
        nums4 = set(nums2)
        dict1 = nums3.intersection(nums4)
        dict1 = list(dict1)
        return dict1
        