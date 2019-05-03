from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    count = 0
    dummy_head = ListNode(None)
    dummy_head.next = L
    target = dummy_head
    while L:
        if count < k:
            count += 1
        else:
            target = target.next
        L = L.next
    target.next = target.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
