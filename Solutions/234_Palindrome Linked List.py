"""
Keys:
- To accomplish it in O(n) time and O(1) space.
- 1.Use two-cursor to find mid. 
- 2.Reverse one of the half linked-list.
- 3. Compare two of the half linked-lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findmid(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            pre = None
            cur = head
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        mid = findmid(head)
        secondHalf = reverse(mid)

        cur1 = head
        cur2 = secondHalf
        while cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
