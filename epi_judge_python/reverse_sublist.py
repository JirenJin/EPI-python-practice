from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    if not L:
        return L
    curr = dummy = ListNode()
    dummy.next = L
    for _ in range(start - 1):
        curr = curr.next
    begin = curr
    stack = []
    for _ in range(finish - start + 1):
        stack.append(curr.next)
        curr = curr.next
    end = curr.next
    for node in reversed(stack):
        begin.next = node
        begin = begin.next
    begin.next = end
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
