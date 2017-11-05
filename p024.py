import math

NUM_DIGITS = 10

def nth_permutation(n):
    remainder = n - 1
    not_used = range(0, NUM_DIGITS)
    digits = []
    for i in xrange(NUM_DIGITS, 0, -1):
        q, remainder = divmod(remainder, math.factorial(i-1))
        digit = not_used[q]
        not_used.remove(digit)
        digits.append(digit)
    return ''.join([str(d) for d in digits])

def main():
    print nth_permutation(10 ** 6)

if __name__ == '__main__':
    main()
