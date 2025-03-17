class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                ans.append(cur.copy())
                return
            if cur_sum > target or i>= len(candidates): 
                return
            # i를 넣는 경우
            cur.append(candidates[i])
            dfs(i, cur, cur_sum+candidates[i])
            # i를 안 넣는 경우
            cur.pop()
            dfs(i+1, cur, cur_sum)
        
        dfs(0,[],0)
        return ans