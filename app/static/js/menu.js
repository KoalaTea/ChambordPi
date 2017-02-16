function selectDrink(drinkname) {
  window.location = "review_order/"+drinkname;
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
