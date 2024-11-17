class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        number_indices = {}

        for i, num in enumerate(nums):
            if num in number_indices and i - number_indices[num] <= k:
                return True
            number_indices[num] = i

        return False
        