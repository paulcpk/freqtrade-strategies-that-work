from freqtrade.strategy import IStrategy, merge_informative_pair
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from freqtrade.exchange import timeframe_to_minutes
import numpy  # noqa


class RSIDirectionalWithTrend(IStrategy):

    """
    RSIDirectionalWithTrend
    author@: Paul Csapak
    github@: https://github.com/paulcpk/freqtrade-strategies-that-work

    How to use it?

    > freqtrade download-data --timeframes 1h --timerange=20180301-20200301
    > freqtrade backtesting --export trades -s DoubleEMACrossoverWithTrend --timeframe 1h --timerange=20180301-20200301
    > freqtrade plot-dataframe -s DoubleEMACrossoverWithTrend --indicators1 ema100 --timeframe 1h --timerange=20180301-20200301

    """

    # Optimal timeframe for the strategy
    timeframe = '1h'

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"

    # timeframe_mins = timeframe_to_minutes(timeframe)
    # minimal_roi = {
    #     "0": 0.08,                       # 5% for the first 3 candles
    #     str(timeframe_mins * 12): 0.04,  # 2% after 3 candles
    #     str(timeframe_mins * 24): 0.02,  # 1% After 6 candles
    # }

    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -0.1

    # trailing stoploss
    trailing_stop = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=4)
        dataframe['ema100'] = ta.EMA(dataframe, timeperiod=100)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                # RSI crosses above 30
                (qtpylib.crossed_above(dataframe['rsi'], 15)) &
                (dataframe['low'] > dataframe['ema100']) &  # Candle low is above EMA
                # Ensure this candle had volume (important for backtesting)
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                # RSI crosses above 70
                (qtpylib.crossed_above(dataframe['rsi'], 85)) |
                 # OR price is below trend ema
                (dataframe['low'] < dataframe['ema100'])
            ),
            'sell'] = 1
        return dataframe
