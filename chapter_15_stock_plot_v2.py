import numpy as np
import matplotlib.pyplot as plt
from chapter_15_stock_load import load_stock

def  makeplot(stock_df,field,my_str):
    column=getattr(stock_df,field)
    column=np.array(column,dtype='float')
    plt.plot(stock_df.Date,column,label=my_str)
    plt.legend()

def do_duo_plot(stock1_df,stock2_df,name1,name2):
    makeplot(stock1_df,'Close',name1)
    makeplot(stock2_df,'Close',name2)
    plt.title(name1+' vs '+name2)
    plt.show()

if __name__ == '__main__':
    stock1_df = load_stock('MSFT')
    stock2_df = load_stock('AAPL')
    do_duo_plot(stock1_df, stock2_df, 'MSFT','AAPL')