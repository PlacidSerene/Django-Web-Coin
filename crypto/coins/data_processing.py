import requests
import plotly.express as px
import pandas as pd

# from plotly.graph_objs import Scatter

def get_data():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C3d%2C7d%2C30d')
    data = response.json()
    # Create chart for each crypto

    # for coin in data[:2]:
    print(data[0]['id'])
    print(len(data[0]['sparkline_in_7d']['price']))
    df = pd.DataFrame(dict(
    x = [i for i in range(len(data[0]['sparkline_in_7d']['price']))],
    y = data[0]['sparkline_in_7d']['price']
))
    fig = px.line(df, x="x", y="y", title="Unsorted Input") 
    fig.show()