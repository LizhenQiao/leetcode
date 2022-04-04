"""
Keys:
- Could be solved by either recursion or iteration.
- Iteration solution is similar to reverse linked list for each k.
- Reverse every two elements in the linked list, from the description of the question, it is clear that there exists
  recursion relationship.

Complexity:

Recursive:
Time: O(n)
Space: O(n)

Iterative:
Time: O(n)
Space: O(1)
"""

# Recursion:


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


# Iteration:
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        pre = ListNode(0)
        pre.next = head
        cur = pre

        step = 0
        cur0 = head
        while cur0:
            cur0 = cur0.next
            step += 1

        for _ in range(step // 2):
            cur0 = cur.next
            pre0 = None
            for _ in range(2):
                cur0.next, pre0, cur0 = pre0, cur0, cur0.next

            # Core of the code. We need to keep cur always points to the pre of next fragment.
            # Apart from above, also need to be familiar with what cur0 and pre0 would be after a normal linked list reverse operation.
            tmp = cur.next
            cur.next.next = cur0
            cur.next = pre0
            cur = tmp

        return pre.next
