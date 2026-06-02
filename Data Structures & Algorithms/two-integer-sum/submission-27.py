class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        num_dict = {}
        for index, value in enumerate(nums):
            num_dict.setdefault(value, []).append(index)

        for value in num_dict.keys():
            x = target - value
            if x in num_dict:
                i = num_dict[value].pop(0)
                if len(num_dict[x]) > 0:
                    j = num_dict[x][0]
                    answer = [i, j]
                    break
           
         
        return answer
