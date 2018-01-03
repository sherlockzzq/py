import random

class Stocks:
    
    def __init__(self, company_name, ticker_symbol):
        self.company_name = company_name
        self.ticker_symbol = ticker_symbol
        self.bid_price = 0
        self.ask_price = 0

    @property
    def midmarket_value(self):
        return (self.bid_price + self.ask_price) / 2

class Exchange:
    securities = {}
    def __init__(self, name):
        self.name = name
        

    def add_security(self, Stock):
        self.securities[Stock.ticker_symbol] = Stock

    def set_prices(self):
        for key, val in self.securities.items():
            ask_price =  random.uniform(0, 1000)
            val.ask_price = ask_price
            val.bid_price = ask_price * (100 - random.uniform(0.5, 2.0))/100

class Broker:

    def __init__(self, name, per_share_commission_amount):
        self.name = name
        self.per_share_commission_amount = per_share_commission_amount

class Portfolio:

    def __init__(self, name):
        self.name = name
        self.holdings = {}

    @staticmethod
    def get_bid_price(ticker_symbol):
        return exchange.securities[ticker_symbol].bid_price

    @staticmethod
    def get_ask_price(ticker_symbol):
        return exchange.securities[ticker_symbol].ask_price

    def update_position(self, ticker_symbol, share_purchased):
        if ticker_symbol in self.holdings.keys():
            self.holdings[ticker_symbol] += share_purchased
        else:
            self.holdings[ticker_symbol] = share_purchased

    def current_value(self):
        sum_val = 0
        for key, val in self.holdings.items():
            if val > 0:
                sum_val += self.get_ask_price(key) * val
            else:
                sum_val += self.get_bid_price(key) * val
        return sum_val


class Investor:

    def __init__(self, name, cash_balance):
        self.name = name
        self.cash_balance = cash_balance
        self.portfolios = {}

    def execute_trade(self, broker, ticker_symbol, portfolio_name, quantity, exchange):
        commission = broker.per_share_commission_amount
        self.portfolios[portfolio_name].update_position(ticker_symbol, quantity)
        if quantity >= 0: 
            self.cash_balance -= (Portfolio.get_ask_price(ticker_symbol) + commission) * quantity
        else:
            self.cash_balance -= (Portfolio.get_bid_price(ticker_symbol) - commission) * quantity

    def net_worth(self):
        net = 0
        for name, portfolio in self.portfolios.items():
            net += portfolio.current_value()
        return net

exchange = Exchange('CHX')








