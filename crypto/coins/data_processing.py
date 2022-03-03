import requests
# import plotly.express as px
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

def create_plot(x,y):
    pass


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
