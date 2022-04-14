function simpleTemplating(data) {
  var html = "<ul>";
  $.each(data, function (index, item) {
    html += "<li>" + item + "</li>";
  });
  html += "</ul>";
  return html;
}
async function getData(total_pages) {
  let allData = [];
  for (let i = 1; i < total_pages + 1; i++) {
    const response = await fetch(
      `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=${i}&sparkline=false`
    );
    let data = await response.json();
    data.forEach((e) => allData.push(e));
  }
  console.log(allData);
}

$("#pagination-container").pagination({
  dataSource: function (done) {
    let allData = [];
    for (let i = 1; i < 6 + 1; i++) {
    const response = await fetch(
      `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=${i}&sparkline=false`
    );
    let data = await response.json();
    data.forEach((e) => allData.push(e));
  }
    done(allData);
  },
  callback: function (data, pagination) {
    var html = simpleTemplating(data);
    $("#data-container").html(html);
  },
});
