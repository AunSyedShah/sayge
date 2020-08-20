DAILY_SUMMARY_SQL = """
    select
        location_code,
        royalty_sales,
        total_orders,
        average_delivery_time,
        percentageofordersinsingles,
        ifc,
        labor,
        food,
        system_date
    from
        landing.dwd_rep_daily_summary
    where
        {where}
"""

IDEAL_LABOR_SUMMARY_SQL = """
    select
        location_code,
        ideallaboramount,
        system_date
    from
        landing.dwd_lnd_ideallaborsummary
    where
        {where}
"""

TIME_CLOCK_SQL = """
    select
        location_code,
        position_code,
        time_in,
        time_out,
        system_date
    from
        landing.dwd_lnd_time_clock
    where
        {where}
"""

ORDERS_SQL = """
    select
        location_code,
        sum(orderroyaltysales) as orderroyaltysales
    from
        landing.dwd_lnd_orders
    where
        {where}
    group by
        location_code
"""
