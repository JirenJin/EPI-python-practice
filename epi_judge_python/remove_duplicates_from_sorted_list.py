from test_framework import generic_test
from list_node import ListNode


def remove_duplicates(L):
    pre = dummy_head = ListNode(None, L)
    while pre.next:
        if pre.next.data == pre.data:
            pre.next = pre.next.next
        else:
            pre = pre.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
