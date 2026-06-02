class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_ana = True
        str_one_dict = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for char in s:
            str_one_dict[char] += 1

        for letter in t:
            if letter in str_one_dict and str_one_dict[letter] >= 1:
                str_one_dict[letter] -= 1
            else:
                is_ana = False
                break

        for v in str_one_dict.values():
            if v > 0:
                is_ana = False
                break

        return is_ana
        



        

        