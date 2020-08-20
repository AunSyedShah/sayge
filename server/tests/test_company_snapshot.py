from collections import OrderedDict
from datetime import datetime, timedelta
from decimal import Decimal
import pandas as pd
from django.urls import reverse
import stores.snowflake_data
from stores.serializers import CompanySnapshotSerializer
from freezegun import freeze_time


def fake_company_snapshot(**kwargs):
    data = [
        (
            '1',  # Store
            Decimal('10000.0000'),  # Royalty Sales
            500,  # Orders
            10.00,  # Average Delivery Time
            90.00,  # Percentage of orders in singles
            Decimal('1.0000'),  # IFC
            Decimal('1.0000'),  # Labor
            Decimal('1.0000'),  # Food
            datetime(2020, 2, 1, 0, 0),  # Date
        ),
        (
            '1',  # Store (data year ago)
            Decimal('5000.0000'),  # Royalty Sales
            100,  # Orders
            10.00,  # Average Delivery Time
            90.00,  # Percentage of orders in singles
            Decimal('1.0000'),  # IFC
            Decimal('1.0000'),  # Labor
            Decimal('1.0000'),  # Food
            datetime(2019, 2, 1, 0, 0),  # Date
        ),
    ]
    columns = [
        'store',
        'royalty_sales',
        'orders',
        'average_delivery_time',
        'percentage_of_orders_in_singles',
        'ifc',
        'labor',
        'food',
        'date',
    ]
    yield pd.DataFrame([data[0]], columns=columns)
    yield pd.DataFrame([data[1]], columns=columns)


def fake_ideal_labor_summary(**kwargs):
    data = [
        (
            '1',  # Store
            Decimal('300.0000'),  # Ideal Labor Amount
            datetime(2020, 2, 1, 0, 0),  # Date
        ),
        (
            '2',  # Store
            Decimal('200.0000'),  # Ideal Labor Amount
            datetime(2019, 2, 1, 0, 0),  # Date
        ),
    ]
    columns = [
        'store',
        'ideal_labor_amount',
        'date',
    ]
    yield pd.DataFrame([data[0]], columns=columns)
    yield pd.DataFrame([data[1]], columns=columns)


def fake_time_clock(**kwargs):
    data = [
        (
            '1',  # Store
            timedelta(days=1, hours=2),  # Labor hours
            # 10,  # Position Code
            # datetime(2020, 2, 1, 11, 0),  # Time In
            # datetime(2020, 2, 1, 12, 0),  # Time Out
            # datetime(2020, 2, 1, 0, 0),  # Date
        ),
        (
            '2',  # Store
            timedelta(days=1, hours=4),  # Labor hours
            # 10,  # Position Code
            # datetime(2020, 2, 1, 11, 0),  # Time In
            # datetime(2020, 2, 1, 12, 0),  # Time Out
            # datetime(2020, 2, 1, 0, 0),  # Date
        ),
    ]
    columns = [
        'store',
        'labor_hours',
        # 'position_code',
        # 'time_in',
        # 'time_out',
        # 'date',
    ]

    def fake_data():
        yield pd.DataFrame([data[0]], columns=columns)
        yield pd.DataFrame([data[1]], columns=columns)

    def fake_method(*args, **kwargs):
        return obj

    g = fake_data()

    obj = type('FakeDataFrame', (object,), {
        'assign': fake_method, 'drop': fake_method, 'groupby': fake_method,
        'sum': lambda: next(g)
    })

    return obj


def fake_orders_data(**kwargs):
    data = [
        (
            '1',  # Store
            Decimal('123.0000'),  # Ideal Labor Amount
            # datetime(2020, 2, 1, 0, 0),  # Date
        ),
        (
            '2',  # Store
            Decimal('456.0000'),  # Ideal Labor Amount
            # datetime(2019, 2, 1, 0, 0),  # Date
        ),
    ]
    columns = [
        'store',
        'order_royalty_sales',
    ]
    return pd.DataFrame([data[0]], columns=columns)
    # yield pd.DataFrame([data[1]], columns=columns)


def _patch_data(monkeypatch):
    fake_data = fake_company_snapshot()
    monkeypatch.setattr(
        stores.snowflake_data,
        'get_company_snapshot',
        lambda date: next(fake_data)
    )

    fake_ils_data = fake_ideal_labor_summary()
    monkeypatch.setattr(
        stores.snowflake_data,
        'get_ideal_labor_summary',
        lambda date: next(fake_ils_data)
    )

    monkeypatch.setattr(
        stores.snowflake_data,
        'get_time_clock',
        fake_time_clock
    )

    monkeypatch.setattr(
        stores.snowflake_data,
        'get_orders',
        fake_orders_data
    )


def test_company_snapshot(monkeypatch):
    _patch_data(monkeypatch)

    date = datetime(2020, 2, 1)
    data = stores.snowflake_data.company_snapshot(date)

    serializer = CompanySnapshotSerializer(data=data, many=True)
    assert serializer.is_valid() is True
    assert serializer.data == [
        OrderedDict([
            ('store', 1),
            ('royalty_sales', 10000),
            ('royalty_sales_year_ago', 5000),
            ('pcya_royalty_sales', '1.0000'),
            ('total_orders', 500),
            ('total_orders_year_ago', 100),
            ('pcya_total_orders', '4.0000'),
            ('average_ticket', '20.0000'),
            ('actual_food', '0.0001'),
            ('food_variance', '0.0000'),
            ('actual_labor', '0.0001'),
            ('labor_variance', '-0.0299'),
            ('sales_per_labor_hour', '384.6154'),
            ('bad_orders', '123.0000'),
            ('bad_orders_percent', '0.0123'),
        ])
    ]
    assert serializer.errors == []


@freeze_time("2020-02-01")
def test_company_snapshot_api(roles, monkeypatch):
    url = reverse('api-stores-company-snapshot')
    _patch_data(monkeypatch)

    response = roles.anonymous.get(url)
    assert response.status_code == 403

    response = roles.client.get(url)
    assert response.status_code == 200
