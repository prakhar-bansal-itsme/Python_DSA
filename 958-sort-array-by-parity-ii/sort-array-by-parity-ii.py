class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        st = 0
        end = len(nums) - 1

        while st < len(nums) and end >= 0:

            # Skip correct even positions
            while st < len(nums) and nums[st] % 2 == 0:
                st += 2

            # Skip correct odd positions
            while end >= 0 and nums[end] % 2 == 1:
                end -= 2

            if st < len(nums) and end >= 0:
                nums[st], nums[end] = nums[end], nums[st]

        return nums