# Engulfing-trading-bot
This repo includes a personal project about the engulfing candle trading strategy. The project entails reading the price range of a stock or crypto, in this case BTC, in a desired range of time, creating a table and graph and sending buy or sell signals depending on what the trading bot returns.

# The Strategy:
The engulfing candlestick trading strategy involves identifying a two-candle pattern where a smaller candle is followed by a larger candle that completely "engulfs" the smaller one. In a bullish engulfing pattern, a small bearish candle is followed by a larger bullish candle, signaling a potential upward trend. In a bearish engulfing pattern, a small bullish candle is followed by a larger bearish candle, indicating a potential downward trend.

Example of a bullish engulfing candlestick: 
![image](https://github.com/kyledecamargo/engulfing-trading-bot/assets/142937783/bbad2cc5-4a28-41a6-baac-be2aff48ff51)

Example of a bearish engulfing candlestick:
![image](https://github.com/kyledecamargo/engulfing-trading-bot/assets/142937783/12b40385-67a8-443b-a7b6-3b5879e206fe)

# Files:
  EngulfingBot.py: main code containing the libraries, strategy and outputs.

# Outputs:
  ![image](https://github.com/kyledecamargo/engulfing-trading-bot/assets/142937783/53e66f01-4704-4cd0-9aa3-83753929fb4c)
  
  Graph containing buy signals (green arrows) and sell signals (red arrows) in a monthly range from 05-01-2024 and 06-01-2024 for Bitcoin.

![image](https://github.com/kyledecamargo/engulfing-trading-bot/assets/142937783/60db5951-98fa-4651-8755-9c85178aecd1)
  
  DataFrame version of the graph showing the daioly open, high, low, close, adj close and volume of the candlesticks as well as the buy signals (2), sell signals (1), or no clear signal (0).
