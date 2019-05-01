from list_node import ListNode
from test_framework import generic_test

def merge_two_sorted_lists(L1, L2):
    dummy = ListNode()
    curr = dummy
    while L1 and L2:
        if L1.data < L2.data:
            curr.next = L1
            L1 = L1.next
        else:
            curr.next = L2
            L2 = L2.next
        curr = curr.next
    if L1:
        curr.next = L1
    if L2:
        curr.next = L2
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
