from binance_pak import binance_information
from discord_msg import discord_msg
from binance_pak import symbol_info
import binance_soket

# bot settings
COIN = str(input('COIN?: (SHIB, ETH ...) '))
FIAT = str(input('FIAT?: (USDT ....) '))
PERCENT_BUY = float(input("percent buy?: "))
PERCENT_SELL = float(input("percent sell?: "))
PERCENT_CHANGE = float(input('percent change?: '))

# if last_movement is True that means the price goes UP with 'PERCENT_CHANGE' percents
# if it is False the price goes DOWN with 'PERCENT_CHANGE' percents
previous_price = None
last_movement = None
trades_counter = 0
discord_stack = []

crypto_pair = f'{COIN.lower()}{FIAT.lower()}'

binance_price_socket = binance_soket.BinanceSocket(crypto_pair)
symbol_precision, symbol_tick_size = symbol_info.symbol_precision(crypto_pair)
print(symbol_precision, symbol_tick_size)

binance_info = binance_information.BinanceBot(COIN, FIAT)

if __name__ == "__main__":
    while True:
        print(f'Trade number: {trades_counter}')
        discord_stack.append(f'trade number: {trades_counter}')

        if previous_price is None:
            previous_price = binance_price_socket.show_price()
        else:
            while True:
                new_price = binance_price_socket.show_price()
                difference = ((new_price - previous_price) / abs(previous_price)) * 100
                print(difference)
                if difference > 0:
                    last_movement = True
                else:
                    last_movement = False
                if abs(difference) >= PERCENT_CHANGE:
                    print(f'percent change complete, diff:{difference}')
                    previous_price = new_price
                    break

        fiat_balance, coin_balance = binance_info.get_balance_info()

        if trades_counter != 0:
            if last_movement:
                binance_info.buy_coin(float(fiat_balance), PERCENT_BUY, float(previous_price), symbol_precision)
                print(f'bought some coins')
            elif last_movement is False:
                binance_info.sell_coin(float(coin_balance), PERCENT_SELL, float(previous_price), symbol_precision)
                print('sold some coins')
            else:
                print('NOR SOLD OR BOUGHT')

            fiat_balance, coin_balance = binance_info.get_balance_info()
            print(fiat_balance, coin_balance)
            discord_stack.append(
                f'fiat balance: {fiat_balance}, coin balance: {coin_balance}, last bar: {last_movement}, '
                f'price atm: {previous_price}')

            discord_msg.send_discord_msg(discord_stack, crypto_pair)
            discord_stack = []

        trades_counter += 1