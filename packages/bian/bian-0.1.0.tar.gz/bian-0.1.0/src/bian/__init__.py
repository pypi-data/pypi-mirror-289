from logging import getLogger
import pandas as pd
from binance.client import Client

logger = getLogger(__name__)


client = Client

def get_from_api(asset_type, symbol, timeframe, start, end):
    klines = client.get_historical_klines(symbol, timeframe, start, end)

    # Convert to DataFrame
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    df = pd.DataFrame(klines, columns=columns)

    # Save to CSV
    df.to_csv('klines.csv', index=False)

    print("Kline data saved to klines.csv")

get_from_api()