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



        $('#save_button').click(function(){


            var startLeasing = $('#start-lease-input').val();
            var endLeasing = $('#end-lease-input').val();
            var warrantyPeriod = $('#warranty-period-input').val();
            var extendedWarranty = $('#extended-warranty-input').val();



            var update = {
                "id": assetID,
                "start_leasing": startLeasing,
                "end_leasing": endLeasing,
                "warranty_period": warrantyPeriod,
                "extended_warranty": extendedWarranty,

            };

            console.log(update);

            var json = JSON.stringify(update);

            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/api/update/inventory/dcasset",
                data: json,
                contentType: "application/json",
                success: handleResponse
            });

            function handleResponse(data){
                 $('#update-message').text(data+" successfully updated");
                $( "#dialog-updated" ).dialog( "open" );
            }


        });









    });
