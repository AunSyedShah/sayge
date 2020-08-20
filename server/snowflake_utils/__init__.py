import os
import pandas as pd
import snowflake.connector
from stores.snowflake_sql import (
    DAILY_SUMMARY_SQL,
    IDEAL_LABOR_SUMMARY_SQL,
    TIME_CLOCK_SQL,
    ORDERS_SQL
)


def connect():
    return snowflake.connector.connect(
        user=os.environ['SNOWFLAKE_USER'],
        password=os.environ['SNOWFLAKE_PASSWORD'],
        account=os.environ['SNOWFLAKE_ACCOUNT']
    )


def setup_cursor(cursor):
    cursor.execute("use role data_access")
    cursor.execute("use warehouse compute_wh")
    cursor.execute("use database sayge_dwh_cdm")


def general_information(connection):
    cursor = connection.cursor()
    setup_cursor(cursor)

    try:
        cursor.execute("show roles")
        for role in cursor.fetchall():
            print('ROLE:', role[1], f'({role[9]})')
        print('- - -')

        cursor.execute("show schemas")
        for schema in cursor.fetchall():
            print('SCHEMA:', schema[1])
        print('- - -')

        cursor.execute("show warehouses")
        for warehouse in cursor.fetchall():
            print('WAREHOUSE:', warehouse[0])
        print('- - -')

        cursor.execute('show databases')
        for database in cursor.fetchall():
            print('DATABASE:', database[1], f'({database[6]})')
        print('- - -')

        current_information = [
            'CURRENT_ACCOUNT',
            'CURRENT_CLIENT',
            'CURRENT_DATABASE',
            'CURRENT_DATE',
            'CURRENT_REGION',
            'CURRENT_ROLE',
            'CURRENT_SCHEMA',
            'CURRENT_SCHEMAS',
            'CURRENT_SESSION',
            'CURRENT_STATEMENT',
            'CURRENT_TIME',
            'CURRENT_TIMESTAMP',
            'CURRENT_TRANSACTION',
            'CURRENT_USER',
            'CURRENT_VERSION',
            'CURRENT_WAREHOUSE',
        ]
        for info in current_information:
            cursor.execute(f"SELECT {info}()")
            one_row = cursor.fetchone()
            print(info, one_row[0])

    finally:
        cursor.close()


def _where_for_date_and_store(date, store, date_column=None):
    if not date and not store:
        raise Exception('Filter argument needed')

    date = date.strftime('%F')
    date_column = date_column or 'system_date'

    if date and not store:
        where = f"to_date({date_column})=to_date('{date}', 'Y-M-D')"
    elif not date and store:
        where = f"location_code={store}"
    else:
        where = f"to_date({date_column})=to_date('{date}', 'Y-M-D') and location_code={store}"

    return where


def get_company_snapshot(date=None, store=None):
    connection = connect()
    cursor = connection.cursor()
    setup_cursor(cursor)

    where = _where_for_date_and_store(date, store)
    sql = DAILY_SUMMARY_SQL.format(where=where)

    cursor.execute(sql)
    data = cursor.fetchall()
    df = pd.DataFrame(
        data,
        columns=[
            'store',
            'royalty_sales',
            'orders',
            'average_delivery_time',
            'percentage_of_orders_in_singles',
            'ifc',
            'labor',
            'food',
            'date'
        ]
    )
    return df


def get_ideal_labor_summary(date=None, store=None):
    connection = connect()
    cursor = connection.cursor()
    setup_cursor(cursor)

    where = _where_for_date_and_store(date, store)
    sql = IDEAL_LABOR_SUMMARY_SQL.format(where=where)
    cursor.execute(sql)
    data = cursor.fetchall()
    return pd.DataFrame(
        data,
        columns=[
            'store',
            'ideal_labor_amount',
            'date'
        ]
    )


def get_time_clock(date=None, store=None):
    connection = connect()
    cursor = connection.cursor()
    setup_cursor(cursor)

    where = _where_for_date_and_store(date, store)
    where += " and position_code in (10, 30, 50, 51, 53, 54)"

    sql = TIME_CLOCK_SQL.format(where=where)
    cursor.execute(sql)
    data = cursor.fetchall()
    return pd.DataFrame(
        data,
        columns=[
            'store',
            'position_code',
            'time_in',
            'time_out',
            'date'
        ]
    )


def get_orders(date=None, store=None):
    connection = connect()
    cursor = connection.cursor()
    setup_cursor(cursor)

    where = _where_for_date_and_store(date, store, date_column='order_date')
    where += " and order_status_code='99'"

    sql = ORDERS_SQL.format(where=where)
    cursor.execute(sql)
    data = cursor.fetchall()
    return pd.DataFrame(
        data,
        columns=[
            'store',
            'order_royalty_sales',
        ]
    )
