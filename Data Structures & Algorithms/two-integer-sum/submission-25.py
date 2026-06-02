class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[1,3,4,2]
        # target = 6
        answer = []
        
        if len(nums) == 2:
            return [0,1]

        num_dict = {}
        for index, value in enumerate(nums):
            num_dict.setdefault(value, []).append(index)

        cur_i = 0
        print(num_dict)
        for value in num_dict.keys():
            print(value)
            x = target - value
            if x in num_dict:
                print("popping")
                i = num_dict[value].pop(0)
                print(num_dict)
                if len(num_dict[x]) > 0:
                    print(i)
                    print(x)
                    j = num_dict[x][0]
                    answer = [i, j]
                    print(answer)
                    break
           
            print("lkeep looking")
            cur_i += 1
        return answer
