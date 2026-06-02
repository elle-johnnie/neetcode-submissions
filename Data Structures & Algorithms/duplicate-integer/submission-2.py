class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_dup = False
        nums_set = set(nums)
        if len(nums) > len(nums_set):
            is_dup = True
        return is_dup
        