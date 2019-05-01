from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    curr = dummy = ListNode()
    dummy.next = L
    for _ in range(start - 1):
        curr = curr.next
    sublist_head = curr
    sublist_tail = sublist_head.next
    for _ in range(finish - start):
        next_next = sublist_tail.next
        sublist_tail.next = next_next.next
        next_next.next = sublist_head.next
        sublist_head.next = next_next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
