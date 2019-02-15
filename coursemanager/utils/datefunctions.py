"""
datefunctions.py.

Utility date function library.

SAB 15/02/2019

"""
import datetime

def get_week(dt=datetime.datetime.today()):
    """
    Returns a tuple of (wk_start: datetime, wk_end: datetime) of the parameter dt,
    defaulting to the execution date.

    Note: the end of the period is 7 days - 1 second.

    :param dt: As at date
    :return: (wk_start: datetime, wk_end: datetime)
    """
    assert (type(dt) == datetime.datetime), "Valid datetime object required."

    iso_week = datetime.datetime.today().isocalendar()

    period_start = datetime.datetime(dt.year, dt.month, (dt - datetime.timedelta(days=iso_week[2] - 1)).day)
    period_end = period_start + datetime.timedelta(days=7, seconds=-1)

    assert (type(period_start) == datetime.datetime)
    assert (type(period_end) == datetime.datetime)

    return(period_start, period_end)


def get_month(dt=datetime.datetime.today()):
    """
    Returns a tuple of (mnth_start: datetime, mnth_end: datetime) of the parameter dt,
    defaulting to the execution date.

    Note: the end of the period is Month end - 1 second.

    :param dt: As at date
    :return: (mnth_start: datetime, mnth_end: datetime)

    :param dt:
    :return:
    """
    assert (type(dt) == datetime.datetime), "Valid datetime object required."

    period_start = datetime.datetime(dt.year, dt.month, 1)
    if dt.month == 12:
        period_end = datetime.datetime(dt.year + 1, 1, 1) - datetime.timedelta(seconds=1)
    else:
        period_end = datetime.datetime(dt.year, dt.month + 1, 1) - datetime.timedelta(seconds=1)

    assert (type(period_start) == datetime.datetime)
    assert (type(period_end) == datetime.datetime)

    return (period_start, period_end)
