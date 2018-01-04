 $(document).ready(function(){
        console.log(staffID);

        var pc =  $('#computer-detail-input').val();
        var system = $('#system-detail-input').val();
        var system = $('#system-detail-input').val();
        var email = $('#email-detail-input').val();
        $('#edit_button').click(function(){

          $('.toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.input').removeAttr('disabled');
        });

        $('#cancel_button').click(function(){
            $('.toggle').attr('hidden', 'true');
            $('#edit_button').removeAttr('hidden');
            $('.input').attr('disabled', 'true');

            $('#computer-detail-input').val(pc);
            $('#system-detail-input').val(system);
            $('#email-detail-input').val(email);
        });


        //autocomplete for computer
        $('#computer-detail-input').autocomplete({
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
                    $('#computer-detail-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        }); //end autocomplete computer


        //autocomplete for system
        $('#system-detail-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/system/autocomplete',
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
                    $('#system-detail-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        }); //end autocomplete for system

        //email autocomplete
        $('#email-detail-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/email/autocomplete',
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
                    $('#email-detail-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });


        //update staff inventory
        $('#update_button').click(function(){
           var new_computer = $('#computer-detail-input').val();
           var new_system = $('#system-detail-input').val();
           var new_email = $('#email-detail-input').val();

           var update = {
                "staff_id": staffID,
                "pcTagNo": new_computer,
                "systemName": new_system,
                "principalName": new_email
           };

           console.log(update);

           var json = JSON.stringify(update);

            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/update/inventory/staff",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
                console.log(data);
            }

        });



    });

