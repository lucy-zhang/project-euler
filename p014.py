CHAIN_LENGTH = {}

def chain_length(n):
    if n in CHAIN_LENGTH:
        return CHAIN_LENGTH[n];
    else:
        if n == 1:
            l = 1
        elif n % 2 == 0:
            l = 1 + chain_length(n / 2)
        else:
            l = 1 + chain_length(3 * n + 1)
        CHAIN_LENGTH[n] = l
        return l

def main():
    max_chain_length = 1
    start_number = 1
    for i in xrange(2, 10**6):
        if chain_length(i) > max_chain_length:
            max_chain_length = chain_length(i)
            start_number = i
    print start_number


if __name__ == '__main__':
    main()
