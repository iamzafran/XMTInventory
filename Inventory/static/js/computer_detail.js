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

        $('#edit_ownership_button').click(function(){
          $('.ownership-toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.ownership-input').removeAttr('disabled');
        });

        $('#cancel_ownership_edit_button').click(function(){
            $('.ownership-toggle').attr('hidden', 'true');
            $('#edit_ownership_button').removeAttr('hidden');
            $('.ownership-input').attr('disabled', 'true');
        });

         $('#monitor-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/monitor/autocomplete',
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
                    $('#monitor-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });

        $('#projector-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/projector/autocomplete',
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
                    $('#monitor-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });

        $('#save_button').click(function(){

            var pcName = $('#pc-name-input').val();
            var os = $('#operating-system-input').val();
            var remarks = $('#remarks-input').val();
            var projector = $('#projector-input').val();
            var monitor = $('#monitor-input').val();

            var update = {
                "id": computerID,
                "pcName": pcName,
                "os": os,
                "remarks": remarks,
                "projector": projector,
                "monitor": monitor
            };

            console.log(update);

            var json = JSON.stringify(update);

            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/update/inventory/computer",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
                console.log(data);
            }


        });

        $('#ownership-type-input').change(function(){
          var type = $('#ownership-type-input').val();
          console.log("fired");


          if(type=="staff"){
            console.log("staff");
            $('.staff').removeAttr('hidden');
            $('.project').attr('hidden', 'true');
            $('.tenant').attr('hidden', 'true');


          }else if (type=="project"){
            $('.project').removeAttr('hidden');
            $('.tenant').attr('hidden', 'true');
            $('.staff').attr('hidden', 'true');

          }else if(type=="tenant"){
            console.log("tenant");
            $('.tenant').removeAttr('hidden');
            $('.project').attr('hidden', 'true');
            $('.staff').attr('hidden', 'true');
          }
        });


        //staff autocomplete
        $('#staff-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/staff/autocomplete',
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
                    $('#staff-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });


        //tenant autocomplete
        $('#tenant-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/tenant/autocomplete',
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
                    $('#tenant-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });

         //tenant autocomplete
        $('#project-input').autocomplete({
         source : function(request, response){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/project/autocomplete',
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
                    $('#tenant-input').val(ui.item.label);
                    return false;
                }
            });
         },
         delay : 500,
         minLength : 2
        });

        $('#update_ownership_button').click(function(){
            var type = $('#ownership-type-input').val();
            var staff_name = $('#staff-input').val();
            var project_name = $('#project-input').val();
            var tenant_name = $('#tenant-input').val();

            var update = {
                'type': type,
                'computer_id': computerID,
                'staff_name': staff_name,
                'project_name': project_name,
                'tenant_name': tenant_name
            };

            var json = JSON.stringify(update);
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/update/ownership/computer",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
                console.log(data);
            }


        });





    });
