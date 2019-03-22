

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

