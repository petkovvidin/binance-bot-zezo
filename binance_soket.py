import websocket
import json


class BinanceSocket:
    def __init__(self, crypto_pair):
        self.socket_url = f'wss://stream.binance.com:9443/ws/{crypto_pair}@trade'
        self.pair_price = 0

    def pair_price_atm(self):
        def on_message(ws, message):
            price_list = json.loads(message)
            pair_price = price_list['p']
            self.pair_price = pair_price
            ws.close()

        ws = websocket.WebSocketApp(self.socket_url, on_message=on_message)
        ws.run_forever()

    def show_price(self):
        self.pair_price_atm()
        return float(self.pair_price)
