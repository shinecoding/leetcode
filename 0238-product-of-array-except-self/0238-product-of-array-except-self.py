class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        # 해당 숫자의 좌측과 우측을 나눠서 계산
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right # 이미 곱해져있는 값에다가 곱하기
            right *= nums[i]

        return res