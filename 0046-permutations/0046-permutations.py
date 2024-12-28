class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr):
            # 완료조건
            if len(curr) == len(nums):
                ans.append(curr[:])
                return 
            
            # for loop
            for num in nums:
            # 조건
                if num not in curr:
            # append
                    curr.append(num)
            # backtrack()
                    backtrack(curr)
            # pop()
                    curr.pop()

        ans = []
        backtrack([])
        return ans