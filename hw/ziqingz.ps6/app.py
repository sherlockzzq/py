from brokerage import *
## Assumption: one portfolio can contains stocks from the same exchange

USG = Stocks('Usg Corp','USG')
Xerox = Stocks('Xerox Corp - Comm','XRX')
Brunswick = Stocks('Brunswick Corp - Comm','BC')
Idex = Stocks('Idex Corp - Comm','IEX')
Three_M = Stocks('3m Co - Comm','MMM')
Vistra = Stocks('Vistra Energy Corp.','VST')
Whirlpool = Stocks('Whirlpool Corp', 'WHR')
Abbvie = Stocks('Abbvie Inc','ABBC')
Aar = Stocks('Aar Corp - Comm','AIR')

CHX_companies = [USG, Xerox, Brunswick, Idex, Three_M, Vistra, Whirlpool, Abbvie, Aar]
for company in CHX_companies:
    exchange.add_security(company)

Zhang = Investor('Ziqing Zhang',30000)
broker = Broker('Jason',0.002)
Zhang.portfolios['1 Investment'] = Portfolio('1 Investment')
Zhang.portfolios['2 Investment'] = Portfolio('2 Investment')
l = ['1 Investment', '2 Investment']

res = [] # res saves all the current_value. 
price = {} # price saves all the midmarket price for given trading days.
for i in CHX_companies:
    price[i] = []

# trade for 20 trading days
for i in range(20):
    exchange.set_prices()
    for j in CHX_companies:
        price[j].append(j.midmarket_value)
    ticker_symbol = random.choice(CHX_companies).ticker_symbol
    if Zhang.cash_balance > 0:
        n = random.choice(l)
        Zhang.execute_trade(broker, ticker_symbol, n, random.randint(0,30), exchange)
        val = Zhang.portfolios[n].current_value()
        print('current value for {} = {}'.format(n, val))
        print('remaining cash balance = {}'.format(Zhang.cash_balance))
        print('Zhang\'s net worth = {}'.format(Zhang.net_worth()))
        res.append(val)
