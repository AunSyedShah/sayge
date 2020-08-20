#!/usr/bin/env python
import os
import snowflake.connector


general_information = [
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

ctx = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT']
)

cs = ctx.cursor()
try:
    for info in general_information:
        cs.execute(f"SELECT {info}()")
        one_row = cs.fetchone()
        print(info, one_row[0])
finally:
    cs.close()

ctx.close()
