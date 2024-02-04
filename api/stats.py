import numpy as np
from api.models import Company, StockData, Tendency



def get_tendency(company, period, year):
    """
    Calculates the tendency of a stock data adj close

    param : company : <Company>
    param : period <int>
    param : year <int>

    return : tuple : (tendency, intercept)
    """
    stocks = StockData.objects.filter(
        company__id=company.id,
        datetime__year=year,
        datetime__month=period
    )
    values = [stock.adj_close for stock in stocks]
    if not values:
        return
    return np.polyfit(list(range(len(values))), values, 1)


def populate_tendencies(c, periodos, anos):
    for i in c:
        for p in periodos:
            for y in anos:
                tb = get_tendency(i, p, y)
                if tb is None:
                    continue
                t, b = tb
                td = Tendency.objects.create(company=i, period=p, year=y, tendency=t, intercept=b)
                td.save()
