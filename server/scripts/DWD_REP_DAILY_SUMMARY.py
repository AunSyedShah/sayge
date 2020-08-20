#!/usr/bin/env python
from snowflake_utils import connect, setup_cursor
from stores.snowflake_sql import SALES_SECTION_SQL, COST_SECTION_SQL
import pandas as pd


connection = connect()
cursor = connection.cursor()
setup_cursor(cursor)

try:
    date = '2020-06-28'
    sql = SALES_SECTION_SQL.format(date=date)
    cursor.execute(sql)
    data = cursor.fetchall()
    output = pd.DataFrame(
        data,
        columns=[
            'Store',
            'Royalty Sales',
            'Orders',
            'Average Delivery Time',
            'Percentage of orders in singles',
            'Date'
        ]
    )
    print(output)

    sql = COST_SECTION_SQL.format(date=date)
    cursor.execute(sql)
    data = cursor.fetchall()
    output = pd.DataFrame(
        data,
        columns=[
            'Store',
            'Food',
            'Royalty Sales',
            'IFC',
            'Labor',
            'Date',
            'Ideal Labor Amount',
        ]
    )
    print(output)

    import ipdb;ipdb.set_trace()  # noqa: ignore

finally:
    cursor.close()

connection.close()
