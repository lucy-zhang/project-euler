import operator as op
import itertools

def sub2(x, y):
    return y - x

def truediv2(x, y):
    return op.truediv(y, x)

all_digit_sets = list(itertools.combinations(xrange(0, 10), 4))
operator_orderings = list(itertools.product([op.add, op.sub, op.mul, op.truediv, sub2, truediv2], repeat=3))

def tree1(nums, ops):
    a, b, c, d = nums
    o1, o2, o3 = ops
    # print "{} {} ({} {} ({} {} {}))".format(a, o1, b, o2, c, o3, d)
    return o1(a, o2(b, o3(c, d)))

def tree2(nums, ops):
    a, b, c, d = nums
    o1, o2, o3 = ops
    # print "({} {} {}) {} ({} {} {})".format(a, o2, b, o1, c, o3, d)
    return o1(o2(a, b), o3(c, d))

def is_positive_integer(n):
    return (isinstance(n, int) or n.is_integer()) and n > 0

def all_integers_generated(digits):
    digit_orderings = itertools.permutations(digits)
    result = set([])
    all_results = set([])
    for do in digit_orderings:
        # print do
        for oo in operator_orderings:
            try:
                r1 = tree1(do, oo)
                all_results.add(r1)
                if is_positive_integer(r1):
                    result.add(r1)
            except ZeroDivisionError:
                pass
            try:
                r2 = tree2(do, oo)
                all_results.add(r2)
                if is_positive_integer(r2):
                    result.add(r2)
            except ZeroDivisionError:
                pass
    return all_results, result

def largest_in_range(nums):
    max_num = max(nums)
    for i in xrange(1, max_num):
        if i not in nums:
            return i - 1
    return max_num

def process_all():
    largest_in_all = 0
    best = None
    for ds in all_digit_sets:
        print ds,
        all_results, result = all_integers_generated(ds)
        largest = largest_in_range(result)
        print largest
        if largest > largest_in_all:
            largest_in_all = largest
            best = ds
    return largest_in_all, best
