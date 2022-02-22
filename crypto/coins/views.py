from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
# Create your views here.
import requests
# from .data_processing import get_data
from plotly.offline import plot
import plotly.graph_objects as go

# model
from .models import User

def index(request):
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C3d%2C7d%2C30d')
    data = response.json()
    # status = data['status']
    return render(request, 'coins/index.html', {
        'coins': data
    })
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, ":", type(username), password, ":", type(password))
        user = authenticate(request, username=username, password=password)
        print(user)
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
        except IntegrityError:
            return render(request, "coins/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "coins/register.html")

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
        user.fund = user.fund - amount
        user.save()
        print(user.fund)
        return render(request, "coins/buying.html", {
            'message': f'You just bought {coin_receive} {coin}'
        })
    return render(request, "coins/buying.html")

def test(request):
    # Generating some data for plots.
    x = [i for i in range(-10, 11)]
    y1 = [3*i for i in x]
    y2 = [i**2 for i in x]
    y3 = [10*abs(i) for i in x]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    # Adding scatter plot of y2 vs. x. 
    # Size of markers defined by y2 value.
    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                   marker_size=y2, name='Scatter y2')
    )

    # Adding bar plot of y3 vs x.
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    # Setting layout of the figure.
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'coins/test.html', 
                  context={'plot_div': plot_div})