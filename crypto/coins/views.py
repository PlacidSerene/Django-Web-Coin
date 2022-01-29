from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from .data_processing import get_data

def index(request):
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C3d%2C7d%2C30d')
    data = response.json()
    # status = data['status']
    chart = data.price
    return render(request, 'coins/home.html', {
        'coins': data
    })

def test(request):
    get_data()