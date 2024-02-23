from functools import reduce
from typing import Optional


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

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # str_value = ""
        # current = head
        #
        # while current is not None:
        #     str_value += str(current.val)
        #     current = current.next
        #
        # double_value = int(str_value) * 2
        # if double_value == 0:
        #     return ListNode(0)
        #
        # final_node = None
        # merge_data = []
        # while double_value > 0:
        #     digit_number = double_value % 10
        #     double_value = double_value // 10
        #
        #     merge_data.append(digit_number)
        #
        # merge_data.reverse()
        # final_node = ListNode(merge_data[0])
        # for data in merge_data[1:]:
        #     current_build = final_node
        #     while current_build.next is not None:
        #         current_build = current_build.next
        #     current_build.next = ListNode(data)
        #
        # return final_node
        arr_value = []
        current = head

        while current is not None:
            arr_value.append(current.val)
            current = current.next

        merged_value = reduce(lambda x, y: x * 10 + y, arr_value)
        double_value = merged_value * 2
        if double_value == 0:
            return ListNode(0)

        # double_value = str(double_value)
        final_node = None
        if final_node is None:
            final_node = ListNode()
        #
        # current_node = final_node
        # for data in double_value[1:]:
        #     while current_node.next is not None:
        #         current_node = current_node.next
        #     current_node.next = ListNode(int(data))
        #
        # return final_node

        while double_value > 0:
            digit_number = double_value % 10
            double_value = double_value // 10

            if final_node is None:
                final_node = ListNode(digit_number)
            else:
                current_build = final_node
                while current_build.next is not None:
                    current_build = current_build.next
                current_build.next = ListNode(digit_number)

        current_reverse = final_node.next
        reversed_node = None

        while current_reverse is not None:
            next_temp = current_reverse.next
            current_reverse.next = reversed_node
            reversed_node = current_reverse
            current_reverse = next_temp

        return reversed_node


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(8)
    c = ListNode(9)

    a.next = b
    b.next = c
    c.next = None

    solultion = Solution()
    re = solultion.doubleIt(a)
    solultion.print(re)
    # num = ([3, 4, 3, 2, 1])
    # print(reduce(lambda x, y: x * 10 + y, num))



