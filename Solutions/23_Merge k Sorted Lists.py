"""
Keys:
- heap
- heap store one node of each list in lists. (When the list still have node)
- To identify each node, the heap node need a property i which indicates its resourse.

Complexity:
Time: O(nlog(m))
Space: O(m)
* m equals to len(lists)
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        pre = ListNode(0)
        cur = pre
        heap = []

        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, index = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

        return pre.next
