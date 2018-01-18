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

        $('.datepicker').datepicker({
            dateFormat: 'yy-mm-dd'
        });
        bindSystem();

        $('#save_system').click(function(){

            var system_or_app = $('#system_or_app').val();
            var name = $('#system_name').val();
            var developer_name = $('#developer_name').val();
            var contact_no = $('#contact_number').val();
            var start_date = $('#start_date').val();
            var end_date = $('#end_date').val();
            var db = $('#database_name').val();

            var new_system = {
                'name': name,
                'location_id': locationID,
                'developer_name': developer_name,
                'developer_contact': contact_no,
                'startDate': start_date,
                'endDate': end_date,
                'db': db
            }

             var json = JSON.stringify(new_system);

            console.log(json);

            if(system_or_app==1){
                addSystem(json);
            }else if(system_or_app==2){
                addSoftware(json);
            }



        });





});


function check(element){
    var system_or_app = $(element).val();

    if(system_or_app==1){
        console.log("system");

        $('#system_name').attr("placeholder","System Name");
        $('#system_name').removeClass("software-autocomplete");
        $('#system_name').addClass("system-autocomplete");
        bindSystem();
    }else if(system_or_app==2){
        console.log("app");

        $('#system_name').attr("placeholder","App Name");
        $('#system_name').removeClass("system-autocomplete");
        $('#system_name').addClass("software-autocomplete");
        bindSoftware();

    }
}

function bindSystem(){

    $('.system-autocomplete').autocomplete({
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
                            $('system-autocomplete').val(ui.item.label);
                            return false;
                        }
                    });
                 },
                 appendTo: ".system-form",
                 delay : 500,
                 minLength : 2
    });
}

function bindSoftware(){
$('.software-autocomplete').autocomplete({
                 source : function(request, response){
                    $.ajax({
                        url: 'http://127.0.0.1:8000/api/software/autocomplete',
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
                            $('.software-autocomplete').val(ui.item.label);
                            return false;
                        }
                    });
                 },
                  appendTo: ".system-form",
                 delay : 500,
                 minLength : 2
});

}

function addSystem(json){


      var isValid = validate(".system-required");
        console.log(isValid);

        if(!isValid){
            return;
        }

     $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/system",
                    data: json,
                    contentType: "application/json",
                    success: handleAddSystem
        });

        function handleAddSystem(data){
        console.log(data);
          $('#add-message').text("System succesfully added");
                 $( "#dialog-added" ).dialog( "open" );


    }
}


function addSoftware(json){

   var isValid = validate(".system-required");
        console.log(isValid);

        if(!isValid){
            return;
        }
         $.ajax({
                        type: "POST",
                        url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/software",
                        data: json,
                        contentType: "application/json",
                        success: handleAddSoftware
            });

            function handleAddSoftware(data){
        console.log(data);
          $('#add-message').text("Software succesfully added");
                 $( "#dialog-added" ).dialog( "open" );


    }
}

 function handleResponse(data){

        console.log(data);


    }


function updateSoftware(element, developer_id){

    var root = $(element).parent().parent();
    var softwareID = $(element).val();
    var developer_name = $(root).find('.developer-name').val();
    var developer_contact = $(root).find('.developer-contact').val();
    var start_date = formatDate($(root).find('.start-date').val());
    var end_date = formatDate($(root).find('.end-date').val());
    var db = $(root).find('.database-name').val();

    var update = {
        'software_id': softwareID,
        'location_id': locationID,
         'developer_id': developer_id,
        'developer_name': developer_name,
        'developer_contact': developer_contact,
        'startDate': start_date,
        'endDate': end_date,
        'db': db
    }

    console.log(update);

    var json = JSON.stringify(update)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/software/developer",
                    data: json,
                    contentType: "application/json",
                    success: handleUpdateSoftware
                 });
     function handleUpdateSoftware(data){

        console.log(data);
        $('#update-message').text("Software license updated");
        $( "#dialog-updated" ).dialog( "open" );
    }



}

  function handleResponse(data){

        console.log(data);
}



function updateSystem(element, developer_id){

    var root = $(element).parent().parent();
    var systemID = $(element).val();
    var developer_name = $(root).find('.developer-name').val();
    var developer_contact =$(root).find('.developer-contact').val();
    var start_date = formatDate($(root).find('.start-date').val());
    var end_date =  formatDate($(root).find('.end-date').val());
    var db = $(root).find('.database-name').val();

    var update = {
        'system_id': systemID,
        'location_id': locationID,
         'developer_id': developer_id,
        'developer_name': developer_name,
        'developer_contact': developer_contact,
        'startDate': start_date,
        'endDate': end_date,
        'db': db
    }

    console.log(update);

    var json = JSON.stringify(update)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/system/developer",
                    data: json,
                    contentType: "application/json",
                    success: handleUpdateSystem
                 });

      function handleUpdateSystem(data){

        console.log(data);
         $('#update-message').text("System license updated");
        $( "#dialog-updated" ).dialog( "open" );
    }




}


function removeSystem(element, developer_id){
    var root = $(element).parent().parent();

    var systemID = $(element).val();

    var remove = {
        "location_id": locationID,
        "developer_id": developer_id,
        "system_id": systemID
    }

    var json = JSON.stringify(remove)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/customerlocation/system/",
                    data: json,
                    contentType: "application/json",
                    success: function(data){
                        handleResponse(data);
                        var parent = $(root).parent();
                        $(parent).remove();
                    }
                 });


}


function removeSoftware(element, developer_id){
    var root = $(element).parent().parent();


    var softwareID = $(element).val();

    var remove = {
        "location_id": locationID,
        "developer_id": developer_id,
        "software_id": softwareID
        }


    var json = JSON.stringify(remove)
                 $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/customerlocation/software/",
                    data: json,
                    contentType: "application/json",
                    success: function(data){
                        handleResponse(data);
                        var parent = $(root).parent();
                        $(parent).remove();
                    }
             });

}


  function handleResponse(data){
        console.log(data);
}