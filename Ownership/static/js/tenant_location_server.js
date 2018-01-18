$(document).ready(function(){

        $('#edit_server_button').click(function(){

          $('.server-toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.server-input').removeAttr('disabled');
        });

        $('#cancel_server_button').click(function(){
            $('.server-toggle').attr('hidden', 'true');
            $('#edit_server_button').removeAttr('hidden');
            $('.server-input').attr('disabled', 'true');
        });


        $('#update_server_button').click(function(){

                var isValid = validate(".server-required");
                console.log(isValid);

                if(!isValid){
                    return;
                }
           $('.server-form-group').each(function(index, value){

                console.log(this);

                var serverTag = $(this).find('.server-tag-input').val();
                var startDate = formatDate($(this).find('.server-start-date').val());
                var endDate = formatDate($(this).find('.server-end-date').val());
                console.log(serverTag);
                console.log(startDate);
                console.log(endDate);

                var serverItem = {
                    'server': serverTag,
                    'startDate': startDate,
                    'endDate': endDate
                }

                serversToAdd.push(serverItem);




           });

            var update = {
                    "servers": serversToAdd,
                    "location": locationID
                };



                console.log(update);

                 var json = JSON.stringify(update)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/tenantlocation/server",
                    data: json,
                    contentType: "application/json",
                    success: handleResponse
                 });

                function handleResponse(data){
                    $('#update-message').text("server ownerships successfully updated");
                    $( "#dialog-updated" ).dialog( "open" );
                    console.log(data);
                }



      });


});



function addServer(){


      var div = document.createElement('div');
      div.className = "row form-inline server-form-group"
      var input =   '<div class="form-group mb-2">'+
                      '<input type="text"  class="form-control server-tag-input server-required" placeholder="Server Tag No">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker server-start-date server-required"  placeholder="start date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker server-end-date server-required"  placeholder="end date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<button class="btn btn-danger" onclick="removeServer(this)"> remove </button>'+
                    '</div>';


      div.innerHTML = input;

      $('.server-form').append(div);

      var n = $('.server-form-group').length;
      console.log(n);

      if(n>1){

        $('.remove').removeAttr('disabled');
      }

        serverBind();
 }

 function serverBind(){

        $('.server-tag-input').autocomplete({
                 source : function(request, response){
                    $.ajax({
                        url: 'http://127.0.0.1:8000/api/server/autocomplete',
                        type: 'post',
                        dataType : "json",
                        data : {
                            search : request.term
                        },
                        success : function(data){
                            console.log(data);
                            response(data);
                        },
                        select : function(event, ui){
                            console.log(event);
                            console.log(ui.item.label);
                            $('#search').val(ui.item.label);
                            return false;
                        }
                    });
                 },
                 delay : 500,
                 minLength : 2
        });

        $('.datepicker').datepicker({
            dateFormat: 'yy-mm-dd'
        });

    }

 function removeServer(element){
  var  parent = $(element).parent();
   var root = $(parent).parent();

  console.log(root);
  var server = $(root).find('.server-tag-input').val();
  console.log(server);
  var n = $('.server-form-group').length;


      removeServerRequest(server, n, root);



}


 function removeServerRequest(tag, n, parent){

       var form_group = $(parent).parent();
        console.log(n);


       var data = {
           'server': tag
       };

       var json = JSON.stringify(data);

       if(tag){
         $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/tenantlocation/server",
                    data: json,
                    contentType: "application/json",
                    success: handleResponse
        });
       }else {
        handleResponse(null);
       }


        function handleResponse(data){

            console.log(data);
           if(n>1){

               $(parent).remove();
           }else {
                $(parent).find("input").val("");
           }


        }

}

