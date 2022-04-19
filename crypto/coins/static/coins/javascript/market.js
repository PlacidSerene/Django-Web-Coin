$(".price-change").each(function () {
  let priceChanges = $(this).text().slice(0, -2);
  priceChanges = parseFloat(priceChanges);
  if (priceChanges >= 0) {
    $(this).text("▲" + $(this).text());
    $(this).css("color", "#019267");
  } else {
    $(this).text("▼" + $(this).text());
    $(this).css("color", "#E83A14");
  }
});
