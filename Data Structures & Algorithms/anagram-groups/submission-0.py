class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_keys_dict.setdefault(sorted_word, []).append(word)

        answer = []
        for values in sorted_keys_dict.values():
            answer.append(values)
        return answer