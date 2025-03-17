# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev # 현재 포인터의 방향 반대로 바꾸기
            prev = curr # 포인터 이동
            curr = temp # 포인터 이동
        return prev