from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(None, L)
    pre = dummy_head
    curr = L
    for _ in range(k):
        curr = curr.next
    while curr:
        pre = pre.next
        curr = curr.next
    pre.next = pre.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
