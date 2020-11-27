from freqtrade.strategy import IStrategy, merge_informative_pair
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy  # noqa


class MACDCrossoverWithTrend(IStrategy):

    """
    How to use it?

    > freqtrade download-data --timeframes 30m --timerange=20200301-
    > freqtrade backtesting --export trades -s MACDCrossoverWithTrend --timeframe 30m --timerange=20200301-
    > freqtrade plot-dataframe -s MACDCrossoverWithTrend --indicators1 ema200 --timeframe 30m --timerange=20200301-

    Courtesy to https://www.youtube.com/watch?v=RzGIdibpo8Q
    """

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"
    # minimal_roi = {
    #     "40": 0.0,
    #     "30": 0.01,
    #     "20": 0.02,
    #     "0": 0.04
    # }

    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -0.10

    # Optimal timeframe for the strategy
    timeframe = '30m'

    # trailing stoploss
    trailing_stop = False
    trailing_stop_positive = 0.03
    trailing_stop_positive_offset = 0.04

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']

        dataframe['ema50'] = ta.EMA(dataframe, timeperiod=50)
        dataframe['ema100'] = ta.EMA(dataframe, timeperiod=100)
        dataframe['ema200'] = ta.EMA(dataframe, timeperiod=200)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                (dataframe['macd'] < 0) &  # MACD is below zero
                # Signal crosses above MACD
                (qtpylib.crossed_above(dataframe['macd'], dataframe['macdsignal'])) &
                (dataframe['low'] > dataframe['ema100']) &  # Candle low is above EMA
                # Ensure this candle had volume (important for backtesting)
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                # MACD crosses above Signal
                (qtpylib.crossed_below(dataframe['macd'], 0)) | 
                (dataframe['low'] < dataframe['ema100'])
            ),
            'sell'] = 1
        return dataframe
