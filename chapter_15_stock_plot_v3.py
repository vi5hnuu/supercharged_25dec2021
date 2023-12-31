import numpy as np
import matplotlib.pyplot as plt
from chapter_15_stock_load import load_stock

def do_highlow_plot(stock_df,name_str):
    makeplot(stock_df,'High','Daily high')
    makeplot(stock_df,'Low','Daily low')
    plt.title('High low plice for '+name_str)
    plt.show()

def do_split_plot(stock_df,name_str):
    plt.subplot(2,1,1)
    makeplot(stock_df,'Close','price')
    plt.title(name_str+' price/volume')
    plt.subplot(2,1,2)
    makeplot(stock_df,'Volume','volume')
    plt.show()

def makeplot(stock_df,field,my_str):
    column=getattr(stock_df,field)
    column=np.array(column,dtype='float')
    plt.plot(stock_df.Date,column,label=my_str)
    plt.legend()

if __name__=='__main__':
    stock_df=load_stock('msft')
    # do_highlow_plot(stock_df,'MSFT')
    do_split_plot(stock_df,'MSFT')