from binance import Client
import config


class BinanceBot:
    def __init__(self, coin: str, fiat_coin: str):
        self.bot_client = Client(config.API_KEY, config.API_SECRET)
        self.coin = coin
        self.fiat_coin = fiat_coin

    def get_balance_info(self):
        balance_coin = self.bot_client.get_asset_balance(self.coin)['free']
        balance_fiat = self.bot_client.get_asset_balance(self.fiat_coin)['free']
        return balance_fiat, balance_coin

    def buy_coin(self, fiat_balance, percent_buy, coin_price, precision):
        how_much = fiat_balance * (percent_buy / 100)
        if how_much >= 10:
            quantity = round((1 / coin_price) * how_much, precision)
            self.bot_client.order_market_buy(
                symbol=f'{self.coin.upper()}{self.fiat_coin.upper()}',
                quantity=quantity)

    def sell_coin(self, coin_balance, percent_sell, coin_price, precision):
        if coin_balance > 1:
            how_much = round(coin_balance * (percent_sell / 100), precision)
            min_notional = coin_price * how_much
            if min_notional >= 10:
                self.bot_client.order_market_sell(
                    symbol=f'{self.coin.upper()}{self.fiat_coin.upper()}',
                    quantity=how_much)
