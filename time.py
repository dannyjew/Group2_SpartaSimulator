def date(months):
    from dateutil.relativedelta import relativedelta
    from datetime import date
    date = date.today()
    months = relativedelta(months=months)
    date = date + months

    return date



