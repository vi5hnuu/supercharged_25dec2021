'''Does the work of loafing a stockm given its ticker symbol
depends on files :none
'''

import  pandas_datareader as web

def load_stock(ticker_str):
    '''load stock  function.
    givem a string, ticker_str, load information
    for the indicated stock, such as MSFT into a pandas data frame and return it.
    '''

    df=web.DataReader(ticker_str,'yahoo')
    df=df.reset_index()
    return  df


if __name__ == '__main__':
    stock_df=load_stock('MSFT')
    print(stock_df)
    print(stock_df.columns)