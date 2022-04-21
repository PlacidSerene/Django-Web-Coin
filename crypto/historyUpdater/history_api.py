import requests
from coins.models import Asset, User


def update_history():
    user = User.objects.get(id=1)
    assets = Asset.objects.filter(user=user)
    total = 0
    user_balance = user.balance
    for asset in assets:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={asset.coin_name}&vs_currencies=usd'
        r = request.get(url)
        data = response.json()
        current_coin_price = data[asset.coin_name]['usd']
        total += asset.coin_amount*current_coin_price
    total += user_balance
    History.objects.create(user=user, total=total)