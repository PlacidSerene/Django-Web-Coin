from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests

def index(request):
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    data = response.json()
    # status = data['status']
    return render(request, 'coins/home.html', {
        'coins': data
    })