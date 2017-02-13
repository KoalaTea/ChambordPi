//$(document).ready(function()){
function reload_orders(){
    $('#output').replaceWith("<h1>fuck</h1>");
    $.ajax({
        url: '/current_orders',
        type: 'GET', // GET or POST
        data: parameters,
        success: function(data) { // data is the response from your php script
            // This function is called if your AJAX query was successful
            $('#output').replaceWith(data);
        },
        error: function() {
            // This callback is called if your AJAX query has failed
            alert("Error!");
        }
    });
});
