import datetime as dt 
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Define Time frame

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

#Load Data

ticker = "AAPL"
data = web.DataReader(ticker, 'yahoo', start, end) #Tickle name of apple, api name, startdate, end date

print(data)

# Restructure Data

data = data[["Open", "High", "Low", "Close"]]

data.reset_index(inplace=True)
data["Date"] = data["Date"].map(mdates.date2num) # map function to use for date 2 num

# Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title("{} Share Price".format(ticker), color='white')
ax.set_facecolor('black') # chart color
ax.figure.set_facecolor('#121212') # suround chart color
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width= 0.6, colorup='#00ff00')
plt.show()
