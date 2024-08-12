import pytest
import pandas as pd
import datetime as dt
from QuantTraderLib.getdata.get_data import get_vn_index, get_vn_derivative, get_vnstock, get_forex, get_crypto

def test_get_vn_index_input_types():
    # Kiểm tra loại dữ liệu của các tham số đầu vào
    assert isinstance(get_vn_index('VNINDEX', '2023-01-01'), pd.DataFrame)
    assert isinstance(get_vn_index('VNINDEX', dt.datetime(2023, 1, 1)), pd.DataFrame)
    assert isinstance(get_vn_index('VNINDEX', '2023-01-01', end_date='2023-01-10'), pd.DataFrame)
    assert isinstance(get_vn_index('VNINDEX', '2023-01-01', end_date=dt.datetime(2023, 1, 10)), pd.DataFrame)

def test_get_vn_derivative_input_types():
    # Kiểm tra loại dữ liệu của các tham số đầu vào
    assert isinstance(get_vn_derivative('VN30F1M', '2024-01-01'), pd.DataFrame)
    assert isinstance(get_vn_derivative('VN30F1M', dt.datetime(2024, 1, 1)), pd.DataFrame)
    assert isinstance(get_vn_derivative('VN30F1M', '2024-01-01', end_date='2024-01-10'), pd.DataFrame)
    assert isinstance(get_vn_derivative('VN30F1M', '2024-01-01', end_date=dt.datetime(2024, 1, 10)), pd.DataFrame)

# def test_get_vnstock_input_types():
#     # Kiểm tra loại dữ liệu của các tham số đầu vào
#     assert isinstance(get_vnstock('VCB', '2023-01-01'), pd.DataFrame)
#     assert isinstance(get_vnstock('VCB', dt.datetime(2023, 1, 1), '1D'), pd.DataFrame)
#     assert isinstance(get_vnstock('VCB', '2023-01-01', '1H', end_date='2023-01-10'), pd.DataFrame)
#     assert isinstance(get_vnstock('VCB', '2023-01-01', '1H', end_date=dt.datetime(2023, 1, 10)), pd.DataFrame)

def test_get_forex_input_types():
    # Kiểm tra loại dữ liệu của các tham số đầu vào
    assert isinstance(get_forex('EURUSD', '2023-01-01', '2023-01-10'), pd.DataFrame)
    assert isinstance(get_forex('EURUSD', dt.datetime(2023, 1, 1), dt.datetime(2023, 1, 10)), pd.DataFrame)
    assert isinstance(get_forex('EURUSD', '2023-01-01', '2023-01-10', login='your_login', password='your_password', server='your_server'), pd.DataFrame)

def test_get_crypto_input_types():
    # Kiểm tra loại dữ liệu của các tham số đầu vào
    assert isinstance(get_crypto('BTC-USD', '2023-01-01'), pd.DataFrame)
    assert isinstance(get_crypto('BTC', dt.datetime(2023,1,1)), pd.DataFrame)
    assert isinstance(get_crypto('BTC-USD', '2023-01-01', end_date='2023-01-10'), pd.DataFrame)
    assert isinstance(get_crypto('BTC-USD', '2023-01-01', end_date=dt.datetime(2023, 1, 10)), pd.DataFrame)
