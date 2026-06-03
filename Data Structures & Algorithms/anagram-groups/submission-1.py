class Solution:
    """
    1. create a dict that stores each strings sorted letters as the key and the value contains the unsorted string within a list 
    2. enumerate the given list of strings/words sort each word and combine back to a single string
    3. create a new key or append to the dict if that sorted group of words already exists 
       e.g. [cat, act, stop] --> {act: [cat,act], opst: [stop]}
    4. create an empty list and then enumerate the final dict's values and append each to the list
    4. return the list of lists

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_keys_dict.setdefault(sorted_word, []).append(word)

        answer = []
        for values in sorted_keys_dict.values():
            answer.append(values)
        return answer