from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
# serializtion
from django.core import serializers
# Create your views here.
import requests
# from .data_processing import get_data
# from plotly.offline import plot
# import plotly.graph_objects as go

# model
from .models import User, Payment, Asset

def index(request):
    return render(request, 'coins/index.html')

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "coins/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'coins/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "coins/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            fund = Fund.objects.create(user)
            fund.save()
        except IntegrityError:
            return render(request, "coins/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "coins/register.html")

def add_asset_item(user, coin, coin_receive):
    Asset.objects.create(user=user, coin_name=coin, coin_amount=coin_receive)

@login_required
def asset(request, user_id):
    if request.user.is_authenticated:
        user_asset = serializers.serialize('json', request.user.asset.all())
    return render(request, 'coins/asset.html', {
        "user_asset":user_asset
    })


def buying(request, user_id):
    if request.method == 'POST':
        coin = request.POST['coin_name'] 
        amount = int(request.POST['amount'])
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        current_coin_price = data[coin]['usd']
        user = User.objects.get(id=user_id)
        
        coin_receive = amount/current_coin_price
        fund = user.balance - amount
        if fund < 0:
            return render(request, "coins/buying.html", {
            'message': 'insufficient fund'
        })
        else:
            user.balance = fund
            user.save()
            Payment.objects.create(user=request.user, price=amount, coin_name=coin, coin_receive=coin_receive)
            add_asset_item(request.user, coin, coin_receive)
        return render(request, "coins/buying.html", {
            'message': f'You just bought {coin_receive} {coin}'
        })
    return render(request, "coins/buying.html")

def selling(request, user_id):
    if request.method == 'POST':
        coin = request.POST['coin_name'] 
        amount = int(request.POST['amount'])
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        current_coin_price = data[coin]['usd']
        user = User.objects.get(id=user_id)
        
        coin_receive = amount/current_coin_price
        fund = user.fund.fund - amount
        if fund < 0:
            return render(request, "coins/buying.html", {
            'message': 'insufficient fund'
        })
        else:
            user.fund = fund
            user.save()
            Payment.objects.create(user=request.user, price=amount, coin_name=coin, coin_receive=coin_receive)
            add_asset_item(request.user, coin, coin_receive)
        return render(request, "coins/buying.html", {
            'message': f'You just bought {coin_receive} {coin}'
        })
    return render(request, 'coins/buying.html')
    
def test(request):
    # testing js
    return render(request, 'coins/test.html')


def landing(request):
    return render(request, 'coins/landing.html')

def details(request):
    return render(request, 'coins/details.html')

def market(request):
    return render(request, 'coins/market.html')