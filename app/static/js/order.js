$(document).ready(function()){
    $.ajax({
        url: '/current_orders',
        type: 'GET', // GET or POST
        success: function(data) { // data is the response from your php script
            // This function is called if your AJAX query was successful
            $('#output').append(data);
        },
        error: function() {
            // This callback is called if your AJAX query has failed
            alert("Error!");
        }
    });
});
