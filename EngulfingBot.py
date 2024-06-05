import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Download Bitcoin data 
data = yf.download("BTC-USD", start='2024-05-01',
        end='2024-06-01', interval='1d')
data.iloc[:,:]

# Engulfing trading strategy
def engulfing_signal(df):
    # Current candle
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    # Previous candle
    p_open = df.Open.iloc[-2]
    p_close = df.Close.iloc[-2]

# Bearish signal, current candlestick opened above or same level
# as previous and closed below previous open
    if (open>close and p_open<p_close and 
        close<p_open and open>=p_close): 
        return 1
    
# Bullish signal, current candlestick opened below or same level
# as previous and closed above previous open
    elif (open<close and p_open>p_close and
          close>p_open and open<=p_close):
        return 2
    
# No clear pattern
    else:
        return 0

signal = []
signal.append(0)

# Loop over all the rows of dataframe, check for engulfing candles
for i in range(1, len(data)):
    df = data[i-1:i+1]
    signal.append(engulfing_signal(df))

# Add signal column to dataframe
data['Signal'] = signal

buy_signals = data[data['Signal'] == 2]
sell_signals = data[data['Signal'] == 1]

print(data) # DataFrame output


# Graphing output
plt.figure(figsize=(14,7))
plt.plot(data.index, data['Open'], label='Price', linewidth=2)
plt.scatter(buy_signals.index, buy_signals['Open'], marker='^', color='g', s=100, label='Buy')
plt.scatter(sell_signals.index, sell_signals['Open'], marker='v', color='r', s=100, label='Sell')
plt.title('Engulfing Bot')
plt.xlabel('Date')
plt.ylabel('BTC Price (USD)')
plt.legend()
plt.show()
