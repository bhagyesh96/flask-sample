
function renderData(data){
    console.log(data)
    $("#table_body").empty()
    $.each(data, function( index, value ) {
       console.log(value[0]);
       $("#table_body").append("<tr><td>"+index+"</td><td>"+value[0]+"</td><td>"+value[1]+"</td></tr>")
       
      })
    }

function getJobData(jonId){
    $.get("result/"+jonId, function(data, status){
        
        renderData(data)
        

      });

}

$( "#analyze" ).click(function() {
    $("#loader").css("display", "");
    var url_data = {
        url : $("#url").val()
    }
    $.ajax({
        url: '/analyze',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            $("#loader").css("display", "none");
            getJobData(data.jonId)
        },
        data: JSON.stringify(url_data)
    });



    

});