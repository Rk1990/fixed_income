"""
Classic compounding formula
"""


def fv(rate, n_years):
    """
    return future value of $1 for given annual rate in n years.

    :param rate: annual rate
    :param n_years: number of years
    :return: future value
    """
    return pow(1 + rate, n_years)


def pv(rate, n_years):
    """
    return present value of $1 future value for given annual rate in n years.

    :param rate: annual rate
    :param n_years: number of years
    :return: future value
    """
    return 1 / fv(rate, n_years)
