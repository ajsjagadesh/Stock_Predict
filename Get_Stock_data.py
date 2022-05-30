import pandas_datareader as pdr
import datetime

nvda = pdr.get_data_yahoo('AMD',
                           start=datetime.datetime(2014, 1,2),
                           end=datetime.datetime(2022,5,28))

nvda.to_csv("AMD.csv")