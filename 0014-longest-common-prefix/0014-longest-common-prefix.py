class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        least = strs[0]
        
        # 가장 짧은 단어
        for str in strs:
            if len(least) > len(str):
                least = str
        
        words = []
        
        for n in range(len(strs)):
            count = 0
            for m in range(len(least)):
                if strs[n][m] == least[m]:
                    count += 1
                else:
                    break
            words.append(count)
            
            
        if min(words) == 0:
            return ""
        else:
            return strs[0][:min(words)]
            