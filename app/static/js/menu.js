function selectDrink(drinkname) {
  window.location = "review_order/"+drinkname;
}

function cancelDrink(orderid) {
  $.post({
    url: "/cancel_drink",
    data: {
      order: orderid,
    }
  });
  location.reload(false);
}
