from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def getSize(self, head: Optional[ListNode]) -> int:
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return ListNode()


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    solution = Solution()
    l = solution.getSize(a)
    print(l)