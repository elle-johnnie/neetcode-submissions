class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_ana = True

        for letter in s:
            if letter in t:
                t = t.replace(letter, "", 1)
            else:
                is_ana = False
                break
       
        if t:
            is_ana = False

        return is_ana