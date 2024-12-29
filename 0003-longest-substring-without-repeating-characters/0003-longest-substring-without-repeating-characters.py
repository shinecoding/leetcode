class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # 이미 set에 있으면 중복 나온 지점까지 다 제거
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # 없으면 넣기
            charSet.add(s[r])
            # 최대값
            res = max(res, r - l + 1)

        return res