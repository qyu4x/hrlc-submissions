from typing import Optional

#Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def print(self, head: Optional[ListNode]):
        current = head
        while current is not None:
            print(current.val)
            current = current.next


    def get_length(self, head: Optional[ListNode]):
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head

        count = self.get_length(head)
        if k == 0:
            return head

        reverse_node = None
        if k == count:
            while current is not None:
                temp_next = current.next
                current.next = reverse_node
                reverse_node = current
                current = temp_next
            return reverse_node

        pv_node = None
        final_node = None
        next_current = final_node
        counter = 0
        while current is not None:
            stop = False
            if not stop:
                if counter < k:
                    next_node = current.next
                    current.next = pv_node
                    pv_node = current
                    current = next_node
                    counter += 1
                elif counter >= k:
                    if next_current is None:
                        next_current = pv_node
                    else:
                        nc = next_current
                        while nc.next is not None:
                            nc = nc.next
                        nc.next = pv_node
                    pv_node = None

                    counter = 0
                    next_counter = 0
                    current_node = current
                    while current_node is not None:
                        next_counter += 1
                        current_node = current_node.next

                    if next_counter >= k:
                        stop = False
                    else:
                        stop = True
                        end_current = next_current

                        while end_current.next is not None:
                            end_current = end_current.next
                        end_current.next = current
                        return next_current

        nc = next_current
        while nc.next is not None:
            nc = nc.next
        nc.next = pv_node
        return next_current


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    h = ListNode(8)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h

    solution = Solution()
    re = solution.reverseKGroup(a, 4)
    solution.print(re)
