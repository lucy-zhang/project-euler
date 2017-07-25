def modular_add(x, y):
    return (x + y) % 10 ** 6

def partition_function_slow():
    pnk = [[1]]

    def get_pnk(n, k):
        if n == 0 and k == 0:
            return 1
        elif n <= 0 or k <= 0 or k > n:
            return 0
        else:
            return pnk[n][k]

    yield 1
    n = 1
    while True:
        pnk.append([0] * (n + 1))
        for k in xrange(1, n + 1):
            pnk[n][k] = modular_add(get_pnk(n - k, k), get_pnk(n - 1, k - 1))
        yield reduce(modular_add, pnk[n])
        n += 1

def pentagonal_numbers():
    k = 1
    sign = 1
    while True:
        yield (sign, k * (3 * k - 1) / 2)
        yield (sign, k * (3 * k + 1) / 2)
        k += 1
        sign = -sign

def partition_function_fast():
    p = [1]
    n = 0
    pentagonal_generator = pentagonal_numbers()
    pentagonal_list = [pentagonal_generator.next()]

    while True:
        yield p[n]
        n += 1

        if pentagonal_list[-1][1] < n:
            pentagonal_list.append(pentagonal_generator.next())

        p.append(0)
        for sign, m in pentagonal_list:
            if m > n:
                break
            p[n] = modular_add(p[n], sign * p[n - m])

def find_n():
    for n, p in enumerate(partition_function_fast()):
        if p == 0:
            return n

if __name__ == '__main__':
    print find_n()
