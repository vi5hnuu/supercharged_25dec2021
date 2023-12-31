'''Does the minimum to plot the closing price
of wo fixed stocks. depends on file chapter_15_stock_load.py
'''

import numpy as np
import matplotlib.pyplot as plt
from chapter_15_stock_load import load_stock


#
# def do_plot(stock_df):
#     '''Do plot function.
#     use stock_df, a stock dataframe reade from the web
#     '''
#     column=stock_df.Close
#     column=np.array(column,dtype='float')
#     # plt.plot(stock_df.Date,column);
#     plt.plot(stock_df.Date,column,label='Closing price')
#     plt.legend()
#     plt.title('MSFT stock price')
#     plt.show()
#
# if __name__=='__main__':
#     stock_df=load_stock('msft')
#     do_plot(stock_df)
#     # stock_df=load_stock('AAPL')
#     # do_plot(stock_df)


####################################################################
# def  makeplot(stock_df,field,my_str):
#     column=getattr(stock_df,field)
#     column=np.array(column,dtype='float')
#     plt.plot(stock_df.Date,column,label=my_str)
#     plt.legend()
# def do_plot(stock_df,name_str):
#     makeplot(stock_df,'Close','Closing price')
#     plt.title(name_str + ' stock price')
#     plt.show()
#
# if __name__=='__main__':
#     stock_df=load_stock('msft')
#     do_plot(stock_df,'MSFT')
#     # stock_df=load_stock('AAPL')
#     # do_plot(stock_df)

###################################################################

def  makeplot(stock_df,field,my_str):
    column=getattr(stock_df,field)
    column=np.array(column,dtype='float')
    plt.plot(stock_df.Date,column,label=my_str)
    plt.legend()
def do_plot(stock_df,name_str):
    makeplot(stock_df,'Close','Closing price')
    plt.title(name_str + ' stock price')
    plt.show()

def do_duo_plot(stock_df1,stock_df2):
    makeplot(stock_df1,'Close','MSFT')
    makeplot(stock_df2,'Close','AAPL')
    plt.title('MSFT VS AAPL')
    plt.show()
if __name__=='__main__':
    stock1_df=load_stock('msft')
    stock2_df=load_stock('AAPL')
    do_duo_plot(stock1_df,stock2_df)