from freqtrade.strategy import IStrategy, merge_informative_pair
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy  # noqa


class EMAPriceCrossoverWithThreshold(IStrategy):

    """
    EMAPriceCrossoverWithThreshold
    author@: Paul Csapak
    github@: https://github.com/paulcpk/freqtrade-strategies-that-work

    How to use it?

    > freqtrade download-data --timeframes 1h --timerange=20180301-20200301
    > freqtrade backtesting --export trades -s EMAPriceCrossoverWithThreshold --timeframe 1h --timerange=20180301-20200301
    > freqtrade plot-dataframe -s EMAPriceCrossoverWithThreshold --indicators1 ema800 --timeframe 1h --timerange=20180301-20200301

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
    stoploss = -0.15

    # Optimal timeframe for the strategy
    timeframe = '1h'

    # trailing stoploss
    trailing_stop = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        threshold_percentage = 1
        dataframe['ema800'] = ta.EMA(dataframe, timeperiod=800)
        dataframe['ema_threshold'] = dataframe['ema800'] * (100 - threshold_percentage) / 100

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                # Close price crossed above EMA
                (qtpylib.crossed_above(dataframe['close'], dataframe['ema800'])) &
                # Ensure this candle had volume (important for backtesting)
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                # Close price crossed below EMA threshold
                (qtpylib.crossed_below(dataframe['close'], dataframe['ema_threshold']))
            ),
            'sell'] = 1
        return dataframe
