def df(rate, years):
    """
    Calculate discount factor which is same as present value

    :param rate: Series with rate
    :param years: Series with years
    :return: Present value
    """
    return 1 / (1 + rate).pow(years)


def pv(rate, years):
    """
    Calculate present value

    :param rate: Series with rate
    :param years: Series with years
    :return: Present value
    """
    return df(rate, years)


def fv(rate, years):
    """
    Calculate future value

    :param rate: Series with rate
    :param years: Series with years
    :return: Series with future values
    """
    return 1 / df(rate, years)


def money_market_interest(rate, days=None, denominator=None, years=None):
    """
    calculate interest earned for money-market instrument.

    Either (days, and denominator) or years must be passed.

    :param rate: Series with rate
    :param days: number of days
    :param denominator: denominator
    :param years: Series with Years
    :return: Series with calculated interest
    """
    if years is None:
        return money_market_interest(rate, days / denominator)
    else:
        return 1.0 + rate * years


def money_market_fv(rate, days=None, denominator=None, years=None):
    return money_market_interest(rate, days, denominator, years)


def money_market_pv(rate, days=None, denominator=None, years=None):
    return 1.0 / money_market_interest(rate, days, denominator, years)
