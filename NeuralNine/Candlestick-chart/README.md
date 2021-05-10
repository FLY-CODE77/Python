# Candlestick-chart with python

![Figure_1](https://user-images.githubusercontent.com/72845895/117599115-2802be80-b184-11eb-8740-c30f0af6b983.png)


> package we need 
- pip install mpl-finance
- pip install pandas-datareader
- pip install matplotlib
- numpy, padas ..

> ticker 
- ticker mean stock name 
- AAPL is Apple 

> pandas-datareader 
- pandas-datareader.Datareader(ticker, APi, start date, end date)

> matplotlib.dates 
- matplotlib.dates.date2num
- data["Date"].map(mdates.date2num)
- make date to num 
- ex) 2020-10-04 --> 8901123

> candlestick_ohlc
- pakage from mpl-finance
- candlestick_ohlc(ax, data.values, width, colorup)
- data["Date"] values must int format 
- why i convert Date to number

> Visualization
- ax.xais_date() 
- make num date to date time again