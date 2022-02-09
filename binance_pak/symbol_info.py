import json
import re
from binance import Client
import config


def symbol_precision(crypro_pair):
    new_client = Client(config.API_KEY, config.API_SECRET)
    info = json.dumps(new_client.get_symbol_info(symbol=str(crypro_pair)))
    tick_size_reg = r'(?:\"tickSize\": \"\d.\d+\")'
    step_size_reg = r'(?:\"stepSize\": \"\d.\d+\")'
    step_size = re.findall(step_size_reg, info)[0]
    tick_size = re.findall(tick_size_reg, info)[0]
    step_size_nums = (step_size.split(' ')[-1]).split('.')[-1]
    tick_size_nums = (tick_size.split(" ")[-1]).split(".")[-1]
    try:
        return step_size_nums.index('1'), tick_size_nums.index('1') + 1
    except ValueError:
        return 0, tick_size_nums.index('1') + 1
