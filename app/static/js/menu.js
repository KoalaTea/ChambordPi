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
function order_drink( drinkname ){
    $.ajax({
        url: "/order_drink",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ name : drinkname }),
        success: function(data) {
            alert("Response is: " + data);
        },
        error: function(data) {
            alert("ERROR");
        }
    });
};
