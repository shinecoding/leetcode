# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # reverse할 뒤쪽의 노드들
        prev = slow.next = None # 앞쪽 노드 끊어주기, prev도 널
        
        while second: # 2번째 파트 리버스
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # 합치기
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second # 첫번째 뒤에 두번째꺼 통째로 붙임
            second.next = tmp1 # 두번째 다음꺼를 첫번째 다음거로 바꿔줌
            first, second = tmp1, tmp2 # 포인터 이동
            