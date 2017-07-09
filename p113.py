import math

def bouncy(n):
    # first term is number of increasing numbers, second is number of
    # decreasing numbers, third is number of both inc. and dec. numbers (i.e.
    # numbers of the form xx...x)
    return (choose(n+9, 9) - 1) + (choose(n+10, 10) - n - 1) - (9 * n)

# TODO: this should probably be a util method
def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

if __name__ == '__main__':
    print bouncy(100)
