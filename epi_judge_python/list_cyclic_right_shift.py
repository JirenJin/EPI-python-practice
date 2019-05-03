from test_framework import generic_test
from list_node import ListNode


def cyclically_right_shift_list(L, k):
    if not L:
        return None
    def list_len(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    k %= list_len(L)
    if k == 0:
        return L

    pre = dummy_head = ListNode(None, L)
    curr = pre
    for _ in range(k):
        curr = curr.next
    while curr.next:
        curr = curr.next
        pre = pre.next
    head = pre.next
    pre.next = None
    curr.next = dummy_head.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
