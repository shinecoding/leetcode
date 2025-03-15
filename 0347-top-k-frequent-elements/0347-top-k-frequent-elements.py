from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).most_common()[:k]
        ans = [x[0] for x in c]
            
        return ans
        
        
