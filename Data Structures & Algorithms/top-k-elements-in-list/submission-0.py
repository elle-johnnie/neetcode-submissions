from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. create a counter dict from list of nums where k is num and v is number of occurences
        2. use in Counter.most_common(k) to get the k most common values
        3. return list of k values from list of sorted tuples using index 0
        """
        freq_list = []
        num_freq_counter = Counter(nums)
        freqs = num_freq_counter.most_common(k)
        
        for value in freqs:
            freq_list.append(value[0])

        return freq_list
        