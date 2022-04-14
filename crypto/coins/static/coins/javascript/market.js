async function getData(total_pages) {
  let allData = [];
  for (let i = 1; i < total_pages + 1; i++) {
    const response = await fetch(
      `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=${i}&sparkline=false`
    );
    let data = await response.json();
    data.forEach((e) => allData.push(e));
  }
  $("#example").DataTable({
    ordering: false,
    data: allData,
    columns: [
      {
        data: "image",
        render: function (data, type, row, meta) {
          return '<img class="img-icon" src="' + data + '">';
        },
      },
      {
        data: "current_price",
      },
      { data: "price_change_percentage_24h" },
      {
        data: null,
        render: function (data, type, row, meta) {
          return '<button type="button" class="btn btn-primary">Primary</button>';
        },
      },
    ],
  });
}

getData(20);
