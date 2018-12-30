import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    x10, y10, w1, h1 = R1
    x11, y11 = x10 + w1, y10 + h1
    x20, y20, w2, h2 = R2
    x21, y21 = x20 + w2, y20 + h2
    x00 = max(x10, x20)
    x01 = min(x11, x21)
    y00 = max(y10, y20)
    y01 = min(y11, y21)
    if x00 <= x01 and y00 <= y01:
        return Rectangle(x00, y00, x01-x00, y01-y00)
    else:
        return Rectangle(0, 0, -1, -1)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
