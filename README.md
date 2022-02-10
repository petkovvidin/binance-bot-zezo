# Binance bot zezotrade

This bot automatically buys and sells.

## Installation

You need to make venv in empty folder, after that paste the bot folder and then with pip install the rerequirements

```bash
python3 -m venv .
pip install -r requirements.txt
```

## Usage

Before starting the bot you need to paste your api keys from binance in config.py . After that in discord_msg.py you need to paste your webhook from discord.

The usage is very simple:

on the first line you need to input the coin (make shure it staked in binance)

on the second line you have to enter the fiat coin with which you will buy

on the third line the percentage with which you will buy

on the third line the percentage with which you will sell

on the last line the percentage of price movement

## Short story
On the first iteration the bot takes the current price and the next iteration it begins to monitor whether the price has moved by the set percentage. When the movement its UP it buys with the set percentage and if its DOWN it sells the set percentage.

## Contributing

I want to read that I am new to programming and I still have no experience with bots. for this reason please apologize if there is an error or the code is wrong in general.

Also pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Disclaimer:

 I am not a financial advisor. Do not take anything on here as financial advice, ever.
