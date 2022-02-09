from discord import Webhook, RequestsWebhookAdapter


def url_chooser(coin_pair):
    if coin_pair == 'shibusdt':
        discord_url = 'https://discord.com/api/webhooks/940228095925968916/ULzHu2Ext7ik-k0VGh2Tb1TIcIPhE7uQN1VMLVelixKGW0y5ZOIZKQnFStVnmOSXb9Zd'
    elif coin_pair == 'ethusdt':
        discord_url = ''
    else:
        discord_url = 'INVALID DISCORD URL'
    return discord_url


def send_discord_msg(msg_list, crypto_pair):
    webhook = Webhook.from_url(url_chooser(crypto_pair), adapter=RequestsWebhookAdapter())
    for i in msg_list:
        webhook.send(i)
