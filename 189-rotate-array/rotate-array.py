class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        
        n = len(nums)
        k = k % n

        Storage = []

        for i in range((n-k), n):
            Storage.append(nums[i])

        for i in range((n-k-1), -1, -1):
            nums[i+k] = nums[i]
        
        for i in range(0, k):
            nums[i] = Storage[i]

        



        