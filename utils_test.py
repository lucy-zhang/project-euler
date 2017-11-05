import pytest
import utils

class TestPrimesLessThan(object):
    def test_primes_less_than_19(self):
        primes_gen = utils.primes_less_than(19)
        assert list(primes_gen) == [2, 3, 5, 7, 11, 13, 17]

    def test_primes_less_than_19(self):
        primes_gen = utils.primes_less_than(2)
        assert list(primes_gen) == []

class TestPrimeFactors(object):
    def test_prime_factors_120(self):
        assert utils.prime_factors(120) == [(2, 3), (3, 1), (5, 1)]

    def test_prime_factors_17(self):
        assert utils.prime_factors(17) == [(17, 1)]

    def test_prime_factors_2(self):
        assert utils.prime_factors(2) == [(2, 1)]

class TestAllDivisors(object):
    def test_all_divisors_24(self):
        assert utils.all_divisors(24) == [1, 2, 3, 4, 6, 8, 12, 24]

    def test_all_divisors_17(self):
        assert utils.all_divisors(17) == [1, 17]

class TestGcd(object):
    def test_gcd_27_6(self):
        assert utils.gcd(27, 6) == 3

    def test_gcd_6_27(self):
        assert utils.gcd(6, 27) == 3

    def test_gcd_5_27(self):
        assert utils.gcd(5, 27) == 1

class TestBezoutCoefficients(object):
    def test_bezout_coefficients_27_6(self):
        gcd, c, d = utils.bezout_coefficients(27, 6)
        assert gcd == 3
        assert 27 * c + 6 * d == gcd

    def test_bezout_coefficients_6_27(self):
        gcd, c, d = utils.bezout_coefficients(6, 27)
        assert gcd == 3
        assert 6 * c + 27 * d == gcd

    def test_bezout_coefficients_5_27(self):
        gcd, c, d = utils.bezout_coefficients(5, 27)
        assert gcd == 1
        assert 5 * c + 27 * d == gcd

class TestChineseRemainder(object):
    def test_chinese_remainder(self):
        remainder = utils.chinese_remainder(3, 5, 4, 7)
        assert remainder >= 0
        assert remainder < 5 * 7
        assert remainder % 5 == 3
        assert remainder % 7 == 4

class TestCountEltsInRange(object):
    def test_count_elts_in_range_1(self):
        assert utils.count_elts_in_range(0, 10, 3, 0) == 4

    def test_count_elts_in_range_2(self):
        assert utils.count_elts_in_range(0, 9, 3, 0) == 3

    def test_count_elts_in_range_3(self):
        assert utils.count_elts_in_range(0, 8, 3, 0) == 3

    def test_count_elts_in_range_4(self):
        assert utils.count_elts_in_range(1, 10, 3, 0) == 3

    def test_count_elts_in_range_5(self):
        assert utils.count_elts_in_range(2, 10, 3, 0) == 3

    def test_count_elts_in_range_5(self):
        assert utils.count_elts_in_range(2, 10, 3, 0) == 3

class TestPowerSet(object):
    def test_power_set(self):
        assert list(utils.power_set([1, 2, 3])) == [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
