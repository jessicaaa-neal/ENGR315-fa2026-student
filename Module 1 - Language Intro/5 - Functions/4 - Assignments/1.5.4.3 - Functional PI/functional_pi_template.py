import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a = 1.0
    b = 1.0 / math.sqrt(2.0)
    t = 0.25
    p = 1.0

    while True:
        next_a = (a + b) / 2.0
        next_b = math.sqrt(a * b)
        next_t = t - p * (a - next_a) ** 2
        next_p = 2.0 * p

        approximation = (next_a + next_b) ** 2 / (4.0 * next_t)
        if abs(math.pi - approximation) < abs(target_error):
            return approximation

        a, b, t, p = next_a, next_b, next_t, next_p




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
