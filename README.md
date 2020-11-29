# 📈 Freqtrade Strategies That Work
Crypto Trading Strategies for the [freqtrade.io](https://www.freqtrade.io/) trading bot

## Disclaimer
*WARNING* These strategies are highly experimental and for educational purposes only. Use at your own risk. The author assumes no responsibility for your trading results.
## Installation

Copy and paste the strategies into `./user_data/strategies` in your freqtrade repository.

Run them accordign to description. The strategies come with recommended settings.

## Strategy Results

The strategies were tested on the `1h` timeframe, from 2018-03-01 to 2020-03-01 on the following set of assets:
```
[
    "BTC/USDT",
    "LTC/USDT",
    "ETH/USDT",
    "XRP/USDT",
    "ADA/USDT",
    "XLM/USDT",
    "XMR/USDT",
    "DASH/USDT"
]
```


|  Strategy | Buy count | AVG profit % | Total profit % | Timeframe | Backtest period |
|-----------|-----------|--------------|----------------|--------------|-----------------|
| [EMAPriceCrossoverWithThreshold.py](https://github.com/paulcpk/freqtrade-strategies-that-work/blob/main/EMAPriceCrossoverWithThreshold.py) | 272 | 1.31 | 118.53 |  1h | 2018-03-01 to 2020-03-01 |
| [DoubleEMACrossoverWithTrend.py](https://github.com/paulcpk/freqtrade-strategies-that-work/blob/main/DoubleEMACrossoverWithTrend.py) | 655 | 0.56 | 122.50 |  1h | 2018-03-01 to 2020-03-01 |
| [MACDCrossoverWithTrend.py](https://github.com/paulcpk/freqtrade-strategies-that-work/blob/main/MACDCrossoverWithTrend.py) | 300 | 0.49 | 49.42 |  1h | 2018-03-01 to 2020-03-01 |
| [RSIDirectionalWithTrendSlow.py](https://github.com/paulcpk/freqtrade-strategies-that-work/blob/main/RSIDirectionalWithTrendSlow.py) | 108 | 0.91 | 32.75 |  1h | 2018-03-01 to 2020-03-01 |
| [RSIDirectionalWithTrend.py](https://github.com/paulcpk/freqtrade-strategies-that-work/blob/main/RSIDirectionalWithTrend.py) | 181 | 0.27 | 16.16 |  1h | 2018-03-01 to 2020-03-01 |

## Credits

Some of the strategies were inspired by these amazing YouTube Channels:
- [TRADING RUSH](https://www.youtube.com/channel/UCgY_eHY4NCTcRnU6CCZXWng)
- [UKspreadbetting](https://www.youtube.com/user/ukspreadbetting)
- [The Secret Mindset ](https://www.youtube.com/channel/UC9yk_6ks1g1ipJJsxtLKLcA)

For more strategy inspiration and reference, try the official freqtrade strategy repo:
- [freqtrade/freqtrade-strategies](https://github.com/freqtrade/freqtrade-strategies)

## Support

If this was of help to you, consider buying me a cup of coffee.
Support is much appreciated as it helps me to publish more stuff like this.

- BTC: `1KAa2twgCYz8g5Y4fFkercG7criWHi5Bxa`
- ETH: `0xd91d1615c7Bc766A4AF5E9ee0684aE325bEC2261`
- XLM: `GCSFATTGKQYIYGMHU57ACEQLYROPHJRNIIECEBSWWOZTGTAWHIAOV5ES`