# Yahoo_fin has two modules- stock_info and options.

## stock_info:
# get_analysts_info()
# get_balance_sheet()
# get_cash_flow()
# get_data()
# get_day_gainers()
# get_day_losers()
# get_day_most_active()
# get_holders()
# get_income_statement()
# get_live_price()
# get_quote_table()
# get_top_crypto()   <---
# get_stats()
# get_stats_valuation()
# tickers_dow()
# tickers_nasdaq()
# tickers_other()
# tickers_sp500()

## options:
# get_calls()
# get_expiration_dates()
# get_options_chain()
# get_puts()

## info: 
# {“1d”, “1wk”, “1mo”}
# date = mm/dd/yyyy

from yahoo_fin.stock_info import get_data
get_data(ticker, start_date = None, end_date = None, index_as_date = True, interval = "1d")
amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")

ticker_list = ["amzn", "aapl", "ba"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)
historical_datas["aapl"]

# Dow Jones data:
import yahoo_fin.stock_info as si
dow_list = si.tickers_dow()
print("Tickers in Dow Jones:", len(dow_list))
dow_list[0:10]
#['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD']
dow_historical = {}
for ticker in dow_list:
    dow_historical[ticker] = si.get_data(ticker, start_date="01/01/2020", end_date="01/03/2020", interval="1d")
dow_historical
# Nasdaq: tickers_nasdaq()
# S&P500: tickers_sp500()
# Others: tickers_other()
