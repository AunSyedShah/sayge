import math
from datetime import datetime
from decimal import Decimal
import pandas as pd
from snowflake_utils import (
    get_company_snapshot,
    get_ideal_labor_summary,
    get_time_clock,
    get_orders
)


def company_snapshot(date):
    daily_summary = get_company_snapshot(date=date)
    if daily_summary.empty:
        return []

    ideal_labor_summary = get_ideal_labor_summary(date=date)
    time_clock = get_time_clock(date=date)

    time_clock = time_clock\
        .assign(labor_hours=lambda c: c['time_out'] - c['time_in'])\
        .drop(columns=['position_code', 'time_in', 'time_out', 'date'])
    time_clock = time_clock.groupby('store', as_index=False).sum()

    mixed = pd.merge(
        daily_summary, ideal_labor_summary,
        on=['store'],
        how='left'
    )

    mixed = pd.merge(
        mixed, time_clock,
        on=['store'],
        how='left'
    )

    orders = get_orders(date=date)
    mixed = pd.merge(
        mixed, orders,
        on=['store'],
        how='left'
    )

    try:
        year_ago = datetime(date.year - 1, date.month, date.day)
    except ValueError:
        year_ago = datetime(date.year - 1, date.month, date.day - 1)
    daily_summary_year_ago = get_company_snapshot(date=year_ago)

    stores = {}
    for index, item in mixed.iterrows():
        # FIXME: invalid data
        if math.isnan(item['order_royalty_sales']):
            bad_orders = '0.0'
            bad_orders_percent = '0.0'
        else:
            bad_orders = Decimal(item['order_royalty_sales'])
            bad_orders_percent = round(
                Decimal(item['order_royalty_sales']) / item['royalty_sales'], 4)

        stores[item['store']] = {
            'store': item['store'],
            'royalty_sales': item['royalty_sales'],
            'total_orders': item['orders'],
            'actual_food': round(item['food'] / item['royalty_sales'], 4),
            'food_variance': round((item['food'] - item['ifc']) / item['royalty_sales'], 4),
            'actual_labor': round(item['labor'] / item['royalty_sales'], 4),
            'labor_variance': round(
                (item['labor'] - item['ideal_labor_amount']) / item['royalty_sales'], 4),
            'sales_per_labor_hour': round(
                item['royalty_sales'] / Decimal(item['labor_hours'] / pd.Timedelta('1 hour')), 4),
            'labor_hours': item['labor_hours'],
            'bad_orders': bad_orders,
            'bad_orders_percent': bad_orders_percent,
        }

    for index, item in daily_summary_year_ago.iterrows():
        stores[item['store']].update({
            'store': item['store'],
            'royalty_sales_year_ago': item['royalty_sales'],
            'total_orders_year_ago': item['orders'],
        })

    for store, item in stores.items():
        item['pcya_royalty_sales'] = round(
            (item['royalty_sales'] / item['royalty_sales_year_ago']) - 1, 4)

        item['pcya_total_orders'] = round(
            (item['total_orders'] / item['total_orders_year_ago']) - 1, 4)
        item['average_ticket'] = round(item['royalty_sales'] / item['total_orders'], 4)

    return sorted(
        [item for k, item in stores.items()],
        key=lambda x: x['store']
    )
