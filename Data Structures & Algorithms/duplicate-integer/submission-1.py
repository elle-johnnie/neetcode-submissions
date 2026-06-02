class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_dup = False
        num_dict = dict()
        count = 0
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                is_dup = True
                break
        
        return is_dup

        