const coin = $("h3").text().toLowerCase();
const ctx = document.getElementById("myChart").getContext("2d");
const myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: coin,
        fill: {
          target: "origin",
          below: "rgb(131, 189, 117)",
        },
        backgroundColor: "rgb(131, 189, 117)",
        borderColor: "rgb(131, 189, 117)",
        data: [],
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      x: {
        ticks: {
          display: true,
          autoSkip: true,
          maxTicksLimit: 8,
        },
      },
    },
  },
});

async function fetchDataDefault(coin) {
  let prices = [];
  let times = [];
  const response = await fetch(
    `https://api.coingecko.com/api/v3/coins/${coin}/market_chart?vs_currency=usd&days=90&interval=daily`
  );
  // waits until the request completes...
  const data = await response.json();
  data.prices.map((price) => {
    let date = new Date(price[0]);
    date = date.toLocaleDateString("en-US");
    times.push(date);
    prices.push(price[1]);
  });
  return { prices: prices, times: times };
}

async function fetchDataAndUpdate(coin, day, interval, times, prices) {
  url = `https://api.coingecko.com/api/v3/coins/${coin}/market_chart?vs_currency=usd&days=${day}&interval=${interval}`;
  const response = await fetch(url);
  // waits until the request completes...
  const new_data = await response.json();
  new_data.prices.map((price) => {
    let date = new Date(price[0]);
    date = date.toLocaleDateString("en-US");
    times.push(date);
    prices.push(price[1]);
  });
  myChart.config.data.labels = times;
  myChart.data.datasets[0].data = prices;
  myChart.update();
}

fetchDataDefault(coin).then((data) => {
  myChart.config.data.labels = data.times;
  myChart.data.datasets[0].data = data.prices;
  myChart.update();
});

// chartIt(coin);

$("select").on("change", async function (e) {
  let interval = "daily";
  if (e.target.value === "1") {
    interval = "hourly";
  } else {
    interval = "daily";
  }

  await fetchDataAndUpdate(
    coin,
    e.target.value,
    interval,
    (times = []),
    (prices = [])
  );
});
