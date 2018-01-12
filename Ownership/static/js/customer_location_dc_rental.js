$(document).ready(function(){

        $('#edit_dc_button').click(function(){

          $('.dc-toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.dc-input').removeAttr('disabled');
        });

        $('#cancel_dc_button').click(function(){
            $('.dc-toggle').attr('hidden', 'true');
            $('#edit_dc_button').removeAttr('hidden');
            $('.dc-input').attr('disabled', 'true');
        });


        $('#update_dc_button').click(function(){

            var dcToAdd = [];
           $('.dc-form-group').each(function(index, value){

                console.log(this);

                var dc_loc = $(this).find('.dc-loc-input').val();
                var no_of_rack = $(this).find('.no-of-rack-input').val();

                var startDate = $(this).find('.dc-start-date').val();
                var endDate = $(this).find('.dc-end-date').val();
                var rental_id = $(this).find('.rental-id').val();
                console.log(dc_loc);
                console.log(no_of_rack);
                console.log(startDate);

                console.log(endDate);

                var dcItem = {
                    'rental_id': rental_id,
                    'dc_location': dc_loc,
                    'number_of_racks': no_of_rack,
                    'startDate': startDate,
                    'endDate': endDate
                }

                dcToAdd.push(dcItem);







           });



            var update = {
                "dc": dcToAdd,
                "location": locationID
            };



            console.log(update);



             var json = JSON.stringify(update)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/datacenter",
                    data: json,
                    contentType: "application/json",
                    success: handleResponse
                 });

                function handleResponse(data){

                    console.log(data);
                }


      });


    });


    function addDataCenter(){


      var div = document.createElement('div');
      div.className = "row form-inline dc-form-group"
      var input =   '<div class="form-group mx-sm-3 mb-2">'+
                     '<select class="form-control dc-loc-input " >'+
                              '<option value="1">DC 1</option>'+
                              '<option value="2">DC 2</option>'+
                    '</select>'+
                    '</div>'+
                   '<div class="form-group mx-sm-3 mb-2">'+
                        '<input class="form-control no-of-rack-input" type="number" value="1">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker dc-start-date"  placeholder="start date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker dc-end-date"  placeholder="end date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<button class="btn btn-danger rental-id" value="-1" onclick="removeDataCenter(this)"> remove </button>'+
                    '</div>';


      div.innerHTML = input;

      var parent = document.getElementsByClassName('dc-form');
      $('.dc-form').append(div);

      var n = $('.dc-form-group').length;
      console.log(n);

      if(n>1){

        $('.remove').removeAttr('disabled');
      }

        dcBind();
    }


    function dcBind(){
    console.log("bind");

        $('.datepicker').datepicker({
            dateFormat: 'yy-mm-dd'
        });

    }

     function removeDataCenter(element){
      var  parent = $(element).parent();
       var root = $(parent).parent();

      console.log(root);
      var dc = $(element).val();
      console.log(dc);
      var n = $('.dc-form-group').length;


          removeDCRequest(dc, n, root);



    }


     function removeDCRequest(dc, n, parent){

       var form_group = $(parent).parent();


       var rental = {
           'rental_id': dc
       };

       var json = JSON.stringify(rental);

       console.log("dc="+dc);

       if(dc){
         $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/customerlocation/datacenter",
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
