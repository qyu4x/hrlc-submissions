from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def print(self, head: Optional[ListNode]) -> None:
        current = head
        while current is not None:
            print(current.val)
            current = current.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        current = head.next

        result_node = head
        result_node.next = None

        while current is not None:
            current_node = result_node

            if prev.val == current.val:
                current = current.next
            elif prev.val != current.val:
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = ListNode(current.val)
                prev = current
        return result_node





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    # d = ListNode(3)
    # e = ListNode(3)

    a.next = b
    b.next = c
    # c.next = d
    # d.next = e

    solution = Solution()
    re = solution.deleteDuplicates(a)
    solution.print(re)