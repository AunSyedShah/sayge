#
# Note: THIS IS FOR R&D
#
# - tests with "snowflake_production" in function name will be skipped
# - add `export SNOWFLAKE_PRODUCTION_TESTS_ENABLED=true` to enable

import pandas as pd
from datetime import datetime
from snowflake_utils import (
    get_company_snapshot, get_ideal_labor_summary, get_time_clock
)

_DEFAULT_DATE_FOR_FILTERING = datetime(2020, 2, 1)


def test_snowflake_production_customer_snapshot():
    kwargs = dict(
        date=_DEFAULT_DATE_FOR_FILTERING,
        store=5379,
    )

    daily_summary = get_company_snapshot(**kwargs)
    # print(daily_summary.T)
    # print('- ' * 20)

    ideal_labor_summary = get_ideal_labor_summary(**kwargs)
    # print(ideal_labor_summary.T)
    # print('- ' * 20)

    mixed = pd.merge(
        daily_summary, ideal_labor_summary
    )
    # print(mixed.T)

    time_clock = get_time_clock(**kwargs)\
        .assign(labor_hours=lambda c: c['time_out'] - c['time_in'])\
        .drop(columns=['position_code', 'time_in', 'time_out', 'date'])
    time_clock = time_clock.groupby('store', as_index=False).sum()
    # print(time_clock.T)
    # print('- ' * 20)
    # print(time_clock)
    # print('- ' * 20)

    mixed = pd.merge(
        mixed, time_clock,
        on=['store'],
        how='inner'
    )
    # print(mixed.T)

    assert False
