import datetime as dt
import yfinance as yfin
import pandas as pd
import MetaTrader5 as mt5
from vnstock import stock_historical_data
from pandas_datareader import data as pdr
import sys

def get_vn_index(symbol, start_date, resolution='1D', end_date=None):
    """
    Truy xuất dữ liệu lịch sử của chỉ số VN từ thị trường chứng khoán Việt Nam.

    Tham số:
        symbol (str): Ký hiệu của chỉ số VN.
        start_date (str hoặc datetime): Ngày bắt đầu cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        resolution (str, tùy chọn): Độ phân giải của dữ liệu. Ví dụ: '1D' cho hàng ngày. Mặc định là '1D'.
        end_date (str hoặc datetime, tùy chọn): Ngày kết thúc cho dữ liệu lịch sử. Nếu không được cung cấp, mặc định là ngày hiện tại.

    Trả về:
        pandas.DataFrame: DataFrame chứa dữ liệu lịch sử của chỉ số VN với các cột 'Date', 'Open', 'High', 'Low', 'Close'.
    """
    if end_date is None:
        end_date = dt.datetime.now()
    df = stock_historical_data(symbol=symbol,
                            start_date=str(start_date)[0:10],
                            end_date=str(end_date)[0:10], resolution=resolution, type='index', beautify=False, decor=False, source='DNSE')
    if 'time' in df.columns:
        df.rename(columns={'time': 'Date', 'open': 'Open', 'high':'High', 'low':'Low', 'close':'Close',}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])

    # Chỉ giữ lại các cột OHLC
    ohlc_columns = ['Date', 'Open', 'High', 'Low', 'Close']
    df = df[ohlc_columns]
    return df

def get_vn_derivative(symbol, start_date, resolution='1D', end_date=None):
    """
    Truy xuất dữ liệu lịch sử của các hợp đồng phái sinh VN từ thị trường chứng khoán Việt Nam.

    Tham số:
        symbol (str): Ký hiệu của hợp đồng phái sinh VN.
        start_date (str hoặc datetime): Ngày bắt đầu cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        resolution (str, tùy chọn): Độ phân giải của dữ liệu. Ví dụ: '1D' cho hàng ngày. Mặc định là '1D'.
        end_date (str hoặc datetime, tùy chọn): Ngày kết thúc cho dữ liệu lịch sử. Nếu không được cung cấp, mặc định là ngày hiện tại.

    Trả về:
        pandas.DataFrame: DataFrame chứa dữ liệu lịch sử của các hợp đồng phái sinh VN với các cột 'Date', 'Open', 'High', 'Low', 'Close'.
    """
    if end_date is None:
        end_date = dt.datetime.now()
    df = stock_historical_data(symbol=symbol,
                            start_date=str(start_date)[0:10],
                            end_date=str(end_date)[0:10], resolution=resolution, type='derivative', beautify=False, decor=False, source='DNSE')
    if 'time' in df.columns:
        df.rename(columns={'time': 'Date', 'open': 'Open', 'high':'High', 'low':'Low', 'close':'Close',}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])

    # Chỉ giữ lại các cột OHLC
    ohlc_columns = ['Date', 'Open', 'High', 'Low', 'Close']
    df = df[ohlc_columns]
    return df

def get_vnstock(symbol, start_date, resolution='1D', end_date=None):
    """
    Truy xuất dữ liệu lịch sử của cổ phiếu VN từ thị trường chứng khoán Việt Nam.

    Tham số:
        symbol (str): Ký hiệu của cổ phiếu VN.
        start_date (str hoặc datetime): Ngày bắt đầu cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        resolution (str, tùy chọn): Độ phân giải của dữ liệu. Ví dụ: '1D' cho hàng ngày. Mặc định là '1D'.
        end_date (str hoặc datetime, tùy chọn): Ngày kết thúc cho dữ liệu lịch sử. Nếu không được cung cấp, mặc định là ngày hiện tại.

    Trả về:
        pandas.DataFrame: DataFrame chứa dữ liệu lịch sử của cổ phiếu VN với các cột 'Date', 'Open', 'High', 'Low', 'Close'.
    """
    if end_date is None:
        end_date = dt.datetime.now() 
    df = None
    df =  stock_historical_data(symbol=symbol,
                            start_date=str(start_date)[0:10],
                            end_date=str(end_date)[0:10], resolution=resolution, type='stock', beautify=False, decor=False, source='DNSE')
    if 'time' in df.columns:
        df.rename(columns={'time': 'Date', 'open': 'Open', 'high':'High', 'low':'Low', 'close':'Close',}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])

    # Chỉ giữ lại các cột OHLC
    ohlc_columns = ['Date', 'Open', 'High', 'Low', 'Close']
    df = df[ohlc_columns]
    return df


def get_forex(pair, start_date, end_date, login=None, password=None, server=None):
    """
    Truy xuất dữ liệu lịch sử cho một cặp tiền từ nền tảng MetaTrader 5.

    Tham số:
        pair (str): Ký hiệu cặp tiền. Ví dụ: 'EURUSD'.
        start_date (str hoặc datetime): Ngày bắt đầu cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        end_date (str hoặc datetime): Ngày kết thúc cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        login (str, tùy chọn): ID đăng nhập của MetaTrader 5. Yêu cầu nếu password và server được cung cấp.
        password (str, tùy chọn): Mật khẩu tài khoản MetaTrader 5. Yêu cầu nếu login và server được cung cấp.
        server (str, tùy chọn): Tên máy chủ MetaTrader 5. Yêu cầu nếu login và password được cung cấp.
        
    Trả về:
        pandas.DataFrame: DataFrame chứa dữ liệu lịch sử của forex.
    """
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        sys.exit() 
    if login and password and server:
        mt5.login(login, password, server)
    rates = mt5.copy_rates_range(pair, mt5.TIMEFRAME_M15, start_date, end_date)
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df = df.rename(columns={'time': 'Date', 'open': 'Open',
                   'low': 'Low', 'close': 'Close', 'high': 'High', 'tick_volume': 'Volume'})
    mt5.shutdown()
    return df

def get_crypto(crypto_currency, start_date, end_date=None):
    """
    Truy xuất dữ liệu lịch sử cho một loại tiền điện tử cụ thể trong đơn vị USD từ Yahoo Finance.
    
    Tham số:
        crypto_currency (str): Ký hiệu hoặc tên của tiền điện tử.
        start_date (str hoặc datetime): Ngày bắt đầu cho dữ liệu lịch sử. Định dạng: 'YYYY-MM-DD'.
        end_date (str hoặc datetime, tùy chọn): Ngày kết thúc cho dữ liệu lịch sử. Nếu không được cung cấp, mặc định là ngày hiện tại.
        
    Trả về:
        pandas.DataFrame: DataFrame chứa dữ liệu lịch sử của tiền điện tử.
    """
    if end_date is None:
        end_date = dt.datetime.now()
    
    # Convert start_date and end_date to datetime if they are strings
    if isinstance(start_date, str):
        start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')
    
    # Use yfinance to get data
    df = None
    df = yfin.download(crypto_currency, start=start_date, end=end_date)
    return df