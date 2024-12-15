class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[none_zero] = nums[i]
                none_zero += 1
        for i in range(none_zero, len(nums)):
            nums[i] = 0