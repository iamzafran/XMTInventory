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


    });
