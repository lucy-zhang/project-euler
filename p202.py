import utils, itertools

# use the usual trick where counting bounces is the same as counting
# intersections in a triangle lattice, then do linear transformation into
# integer lattice

# number of integer lattice pts (x, y) with x > 0, y > 0, 2x+2y-3 = n,
# x-y = 0 mod 3, gcd(x,y) = 1
def num_lattice_points_slow(n):
    if n == 1:
        return 1

    if (n + 3) % 2 == 1:
        return 0

    a = (n + 3) / 2
    half_a = (a - 1) / 2
    first_lattice_point_x = 3 - (a % 3)

    prime_factors_a = [p for p, m in utils.prime_factors(a)]
    print prime_factors_a

    # count by looping
    num_lattice_points_half = 0
    for x in xrange(first_lattice_point_x, half_a + 1, 3):
        x_y_relatively_prime = True
        for p in prime_factors_a:
            if (x % p == 0):
                x_y_relatively_prime = False
                break

        if x_y_relatively_prime:
            num_lattice_points_half += 1

    result = 2 * num_lattice_points_half
    return result

def num_lattice_points_fast(n):
    # count with inclusion-exclusion
    if n == 1:
        return 1

    if (n + 3) % 2 == 1:
        return 0

    a = (n + 3) / 2
    half_a = (a - 1) / 2
    first_lattice_point_x = 3 - (a % 3)

    prime_factors_a = [p for p, m in utils.prime_factors(a)]

    # A is every 3rd point on the line in the lattice, B1 is all points w/ x
    # coord divisible by prime factor i
    # #(A and not B) = #A - #(A and (B1 or B2 or ...))
    # = #A - #((A and B1) or (A and B2) or ..)
    # = #A - (#(A and B1) + #(A and B2) + ... - #(A and B1 and B2) - ...)
    num_lattice_points_half = 0
    factor_sets = utils.power_set(prime_factors_a)
    for factors in factor_sets:
        sign = 1 if (len(factors) % 2 == 0) else -1
        pr = [(3, first_lattice_point_x)] + [(f, 0) for f in factors]
        num_lattice_points_half += sign * count_elts_in_range_with_remainders(first_lattice_point_x, half_a + 1, pr)

    return num_lattice_points_half * 2

def count_elts_in_range_with_remainders(range_min, range_max, pr):
    p_all, r_all = pr[0]
    for (p, r) in pr[1:]:
        p_all, r_all = p_all * p, utils.chinese_remainder(r_all, p_all, r, p)
    return utils.count_elts_in_range(range_min, range_max, p_all, r_all)

def main():
    print num_lattice_points_slow(1000001)
    print num_lattice_points_fast(1000001)
    print num_lattice_points_fast(12017639147)

if __name__ == '__main__':
    main()
