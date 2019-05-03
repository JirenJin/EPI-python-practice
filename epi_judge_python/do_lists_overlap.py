import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0, l1):
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                s1 = head
                s2 = slow
                while s1 is not s2:
                    s1, s2 = s1.next, s2.next
                return s1
        return None

    def list_len(head, terminate=None):
        count = 0
        while head is not terminate:
            count += 1
            head = head.next
        return count

    def is_overlap(l0, l1, t1=None, t2=None):
        len1, len2 = list_len(l0, t1), list_len(l1, t2)
        if len1 > len2:
            for _ in range(len1 - len2):
                l0 = l0.next
        else:
            for _ in range(len2 - len1):
                l1 = l1.next
        while l0 is not t1:
            if l0 is l1:
                return l0
            l0, l1 = l0.next, l1.next
        return None
        

    c1 = has_cycle(l0)
    c2 = has_cycle(l1)
    if c1 is None and c2 is None:
        return is_overlap(l0, l1)
    elif c1 is None and c2 or c1 and c2 is None:
        return None
    else:
        cand = is_overlap(l0, l1, c1, c2)
        if cand:
            return cand
        else:
            if c1 is c2:
                return c2
            it = c2.next
            while it and it is not c2:
                if it is c1:
                    return c2
                it = it.next
            return None


        


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
