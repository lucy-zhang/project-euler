import math, itertools, operator

def primes_less_than(n):
    if n < 2:
        raise StopIteration

    prime_list = [True] * n
    prime_list[0] = False
    prime_list[1] = False

    for (k, k_is_prime) in enumerate(prime_list):
        if k_is_prime:
            yield k
            for i in xrange(k**2, n, k):
                prime_list[i] = False

def prime_factors(n):
    if n < 2:
        return []

    primes = primes_less_than(int(math.sqrt(n)))
    factors = []
    dividend = n
    for p in primes:
        multiplicity = 0
        while dividend % p == 0:
            multiplicity += 1
            dividend = dividend / p
        if multiplicity > 0:
            factors.append((p, multiplicity))

    if not factors:
        factors.append((n, 1))

    return factors

def all_divisors(n):
    divisors = [1]
    for factor, multiplicity in prime_factors(n):
        curr_known_divisors = divisors[:]
        for m in xrange(1, multiplicity + 1):
            divisors += [d * (factor ** m) for d in curr_known_divisors]

    return sorted(divisors)

def gcd(a, b):
    x, y = max(a, b), min(a, b)
    while y > 0:
        x, y = y, x % y

    return x

def bezout_coefficients(a, b):
    """Return a triple (gcd(a, b), c, d) where c*a + d*b = gcd(a, b)."""

    # extended Euclidean algorithm
    x, y = max(a, b), min(a, b)
    s, s_next = 1, 0
    t, t_next = 0, 1
    while y > 0:
        quotient, remainder = divmod(x, y)
        x, y = y, remainder
        s, s_next = s_next, s - quotient * s_next
        t, t_next = t_next, t - quotient * t_next

    if a >= b:
        return (x, s, t)
    else:
        return (x, t, s)

def chinese_remainder(r1, n1, r2, n2):
    """Return the unique n in [0, a*b) such that n = r1 (mod n1) = r2 (mod n2)."""

    gcd, n1_coeff, n2_coeff = bezout_coefficients(n1, n2)
    if gcd > 1:
        raise ValueError("{} and {} are not coprime".format(n1, n2))
    # TODO: could this be more efficient?
    return (n1_coeff * n1 * r2 + n2_coeff * n2 * r1) % (n1 * n2)

def count_elts_in_range(range_min, range_max, diff, a0):
    return (range_max - a0 - 1) / diff - (range_min - a0 - 1) / diff

def power_set(iterable):
    # straight from https://docs.python.org/2.7/library/itertools.html#recipes
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
