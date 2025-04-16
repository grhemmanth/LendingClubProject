import pytest 
from lib.Utils import get_spark_session
from lib.DataReader import read_customers, read_orders

def test_read_customers_df():
    spark=get_spark_session("LOCAL")
    customers_count = read_customers(spark, "LOCAL").count()
    assert customers_count == 12435
def test_read_orders_df():
    spark=get_spark_session("LOCAL")
    orders_count = read_orders(spark, "LOCAL").count()
    assert orders_count == 68884
