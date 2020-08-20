from decimal import ROUND_UP
from rest_framework import serializers


class CompanySnapshotSerializer(serializers.Serializer):
    store = serializers.IntegerField()
    royalty_sales = serializers.IntegerField()
    royalty_sales_year_ago = serializers.IntegerField()
    pcya_royalty_sales = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    total_orders = serializers.IntegerField()
    total_orders_year_ago = serializers.IntegerField()
    pcya_total_orders = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    average_ticket = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    actual_food = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    food_variance = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    actual_labor = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    labor_variance = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    sales_per_labor_hour = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
    bad_orders = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP, allow_null=True)
    bad_orders_percent = serializers.DecimalField(
        max_digits=19, decimal_places=4, rounding=ROUND_UP)
