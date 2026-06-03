class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem: determine which two numbers in a list summed up equal the target number.
        avoid conducting it with permutations. Return the index position of each of the numbers as [i,j]
        1. create a dictionary storing each element in the list, where each element is the key
           and each value is that element's index position. since there may be duplicate elements
           store the value within a list. 
           e.g. given [4,2,5,4,7] the dict = {4: [0,3]}
        2. enumerate through the keys in the dict, subtract this number from the target number to
           produce the number to search for.
           e.g. given target = 9 with 4 being the first key in the dict 9 - 4 = x  (x=5)
        3. search dict for x
            - if found let i equal the popped index value (e.g. 4: [0, 3] --pop(0)--> returns 0 and leaves k,v pair as 4: [3])
                 - check the dict again for the x key and verify it's value length is greater than 0 to keep from re-identifying the same element and its index
                   if the key still has a list populated with a value then assign j the index position associated with the key
            - if not found continue...
        4. return as list [i,j]
        
        """
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
