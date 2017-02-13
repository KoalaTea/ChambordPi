//$(document).ready(function()){
function reload_orders(){
    $.ajax({
        url: '/current_orders',
        type: 'GET', // GET or POST
        success: function(data) { // data is the response from your php script
            $('#output').html(data);
        },
        error: function() {
            // This callback is called if your AJAX query has failed
            alert("Error!");
        }
    });
};

function order_complete( orderid ){
    $.ajax({
        url: "/order_complete",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ _id : orderid }), 
        success: function(data) {
             $('#output').html(data);
       },
        error: function(data) {
            alert("ERROR");
        }
    });
};

window.setInterval(function(){
    reload_orders();
}, 5000);

