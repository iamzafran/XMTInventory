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
           $('.computer-tag-no').each(function(index, value){
                console.log("index :" + index + ", value:"+value);
                console.log($(value).val());
                serversToAdd.push($(value).val());

           });

           var new_inventory = {
                "department": departmentID,
                "servers": serversToAdd
           };

           var json = JSON.stringify(new_inventory);


           $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/update/inventory/department",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
                console.log(data);
            }

           console.log(json);

      });


    });

    function add(){


      var div = document.createElement('div');
      div.className = "row form-row"
      console.log(div);
      var input = '<input type="text" class="form-control input col-8 computer-tag-no">'+
        '<button class="btn btn-danger button input remove" onclick="remove(this)">Remove</button>';

      div.innerHTML = input;

      var parent = document.getElementsByClassName('form-group');
      $('.form-group').append(div);

      var n = $('.form-row').length;
      console.log(n);

      if(n>1){

        $('.remove').removeAttr('disabled');
      }

        bind();
    }


    function remove(element){
      var  parent = $(element).parent();
      var n = $('.form-row').length;
      console.log(n);
        var server = $(element).prev().val();
         console.log(server);

        deleteServer(server, n, parent, element)


    }





    function bind(){

        $('.input').autocomplete({
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

    }


    function deleteServer(tag, n, parent, element){
        var server = {
            'hostname': tag
        }

        var json = JSON.stringify(server)

         $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/delete/inventory/department",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
              if(n===1){
                $(element).prev().val("");

              }else{
                $(parent).remove();

              }
                console.log(data);
            }

    }





