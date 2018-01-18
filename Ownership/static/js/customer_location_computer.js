  $(document).ready(function(){

        $('#edit_button').click(function(){

          $('.toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.input').removeAttr('disabled');
        });

        $('#cancel_button').click(function(){
            $('.toggle').attr('hidden', 'true');
            $('#edit_button').removeAttr('hidden');
            $('.input').attr('disabled', 'true');
        });


        $('#update_button').click(function(){

          var isValid = validate(".computer-required");
                console.log(isValid);

                if(!isValid){
                    return;
                }
           $('.computer-form-group').each(function(index, value){

                console.log(this);

                var pcTag = $(this).find('.computer-tag-input').val();
                var startDate = formatDate($(this).find('.start-date').val());
                var endDate = formatDate($(this).find('.end-date').val());
                console.log(pcTag);
                console.log(startDate);
                console.log(endDate);

                var computerItem = {
                    'pcTagNo': pcTag,
                    'startDate': startDate,
                    'endDate': endDate
                }

                computersToAdd.push(computerItem);

                var update = {
                    "computers": computersToAdd,
                    "location": locationID
                };



                console.log(update);



                 var json = JSON.stringify(update)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation",
                    data: json,
                    contentType: "application/json",
                    success: handleResponse
                 });

                function handleResponse(data){
                    console.log(data);
                     $('#update-message').text("computer ownerships successfully updated");
                    $( "#dialog-updated" ).dialog( "open" );
                }




           });


      });


    });


    function date_format(date){

        var format = Date.parse(date);


    }

    function add(){


      var div = document.createElement('div');
      div.className = "row form-inline computer-form-group"
      var input =   '<div class="form-group mb-2">'+
                      '<input type="text"  class="form-control computer-tag-input computer-required" placeholder="Computer Tag No">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker start-date computer-required"  placeholder="start date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker end-date computer-required"  placeholder="end date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<button class="btn btn-danger" onclick="remove(this)"> remove </button>'+
                    '</div>';


      div.innerHTML = input;

      var parent = document.getElementsByClassName('computer-form');
      $('.computer-form').append(div);

      var n = $('.computer-form-group').length;
      console.log(n);

      if(n>1){

        $('.remove').removeAttr('disabled');
      }

        computerBind();
    }


    function remove(element){
      var  parent = $(element).parent();
       var root = $(parent).parent();

      console.log(root);
      var computer = $(root).find('.computer-tag-input').val();
      console.log(computer);
      var n = $('.computer-form-group').length;


          removeComputer(computer, n, root);



    }





    function computerBind(){
    console.log("bind");

        $('.computer-tag-input').autocomplete({
                 source : function(request, response){
                    $.ajax({
                        url: 'http://127.0.0.1:8000/api/computer/autocomplete',
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


    function removeComputer(tag, n, parent){

       var form_group = $(parent).parent();
        console.log(n);

       var json = JSON.stringify(computer);


       var computer = {
           'computer': tag
       };

       var json = JSON.stringify(computer);

       if(tag){
         $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/customerlocation",
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









