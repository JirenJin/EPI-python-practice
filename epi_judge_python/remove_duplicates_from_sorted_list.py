from test_framework import generic_test
from list_node import ListNode


def remove_duplicates(L):
    curr = L
    while curr:
        while curr.next and curr.next.data == curr.data:
            curr.next = curr.next.next
        curr = curr.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
