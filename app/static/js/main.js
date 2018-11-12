$(document).ready(function() {
     $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/reference/13",
        success: function(data) {
             console.log('success'.data);
        },
        error: function(error){
             console.log('SJM Error');
      }
  });
});
