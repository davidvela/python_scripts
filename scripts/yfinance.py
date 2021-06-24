
import yfinance as yf
# https://algotrading101.com/learn/yahoo-finance-api-guide/
# https://algotrading101.com/learn/yfinance-guide/

## 3modules: 
# yf.Tickers
# yf.download
# yf.pandas_datareader

def multiple_tickets():
    tickers = yf.Tickers('msft aapl goog')
    # ^ returns a named tuple of Ticker objects

    # access each ticker using (example)
    tickers.tickers.MSFT.info
    tickers.tickers.AAPL.history(period="1mo")
    tickers.tickers.GOOG.actions
    
    data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

def apple(): 
    apple= yf.Ticker("aapl")
    # show actions (dividends, splits)
    apple.actions
    # show dividends
    apple.dividends
    # show splits
    apple.splits

    # + other methods etc.

# QUICK START
def quick_start():
    msft = yf.Ticker("MSFT")

    # get stock info
    msft.info

    # get historical market data
    hist = msft.history(period="max")

    # show actions (dividends, splits)
    msft.actions

    # show dividends
    msft.dividends

    # show splits
    msft.splits

    # show financials
    msft.financials
    msft.quarterly_financials

    # show major holders
    msft.major_holders

    # show institutional holders
    msft.institutional_holders

    # show balance sheet
    msft.balance_sheet
    msft.quarterly_balance_sheet

    # show cashflow
    msft.cashflow
    msft.quarterly_cashflow

    # show earnings
    msft.earnings
    msft.quarterly_earnings

    # show sustainability
    msft.sustainability

    # show analysts recommendations
    msft.recommendations

    # show next event (earnings, etc)
    msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    msft.isin

    # show options expirations
    msft.options

    # get option chain for specific expiration
    opt = msft.option_chain('YYYY-MM-DD')
    # data available via: opt.calls, opt.puts




def main(): 
    print("main")