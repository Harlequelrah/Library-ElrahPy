from datetime import datetime

from dateutil.relativedelta import relativedelta


def is_bisectile(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_interval(
    start_date:datetime,
    interval_type: str = None,
    end_date: datetime | None = None,
):
    today = datetime.today() if end_date is None else end_date
    interval = relativedelta(today, start_date)
    y_itvl = interval.years
    m_itvl = y_itvl * 12 + interval.months
    d_itvl = (today - start_date).days
    itvl_type = (
        interval_type.lower() if isinstance(interval_type, str) else interval_type
    )
    match itvl_type:
        case "year" | "y" :
            return y_itvl
        case "month" | "m":
            return m_itvl
        case "day" | "d":
            return d_itvl
        case _:
            return (d_itvl, m_itvl, y_itvl)
