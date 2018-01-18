$(document).ready(function(){

        $('#edit_projector_button').click(function(){

          $('.projector-toggle').removeAttr('hidden');
          $(this).attr('hidden', 'true');
          $('.projector-input').removeAttr('disabled');
        });

        $('#cancel_edit_projector_button').click(function(){
            $('.projector-toggle').attr('hidden', 'true');
            $('#edit_projector_button').removeAttr('hidden');
            $('.projector-input').attr('disabled', 'true');
        });


        $('#update_projector_button').click(function(){
            var projectorsToAdd = [];

             var isValid = validate(".projector-required");
                console.log(isValid);

                if(!isValid){
                    return;
                }

           $('.projector-form-group').each(function(index, value){

                console.log(this);

                var projectorTag = $(this).find('.projector-tag-input').val();
                var startDate = formatDate($(this).find('.projector-start-date').val());
                var endDate = formatDate($(this).find('.projector-end-date').val());
                console.log(projectorTag);
                console.log(startDate);
                console.log(endDate);

                var projectorItem = {
                    'projector': projectorTag,
                    'startDate': startDate,
                    'endDate': endDate
                }


                projectorsToAdd.push(projectorItem);
           });

           var update = {
                    "projectors": projectorsToAdd,
                    "location": locationID
                };

            console.log(update);

            var json = JSON.stringify(update)


            $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/update/inventory/customerlocation/projector",
                    data: json,
                    contentType: "application/json",
                    success: handleResponse
                 });

                function handleResponse(data){
                    $('#update-message').text("Projector ownership successfully updated");
                    $( "#dialog-updated" ).dialog( "open" );
                    console.log(data);
                }





      });


});


function addProjector(){


      var div = document.createElement('div');
      div.className = "row form-inline projector-form-group"
      var input =   '<div class="form-group mb-2">'+
                      '<input type="text"  class="form-control projector-tag-input projector-required" placeholder="Projector Tag No">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker projector-start-date projector-required"  placeholder="start date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<input type="text" class="form-control datepicker projector-end-date projector-required"  placeholder="end date">'+
                    '</div>'+
                    '<div class="form-group mx-sm-3 mb-2">'+
                      '<button class="btn btn-danger" onclick="removeProjector(this)"> remove </button>'+
                    '</div>';


      div.innerHTML = input;

      var parent = document.getElementsByClassName('computer-form');
      $('.projector-form').append(div);

      var n = $('.projector-form-group').length;
      console.log(n);

      if(n>1){

        $('.remove').removeAttr('disabled');
      }

        projectorBind();
 }

 function projectorBind(){

        $('.projector-tag-input').autocomplete({
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


function removeProjector(element){
  var  parent = $(element).parent();
   var root = $(parent).parent();

  console.log(root);
  var projector = $(root).find('.projector-tag-input').val();
  console.log(projector);
  var n = $('.projector-form-group').length;


      removeProjectorRequest(projector, n, root);



}


 function removeProjectorRequest(tag, n, parent){

       var form_group = $(parent).parent();
        console.log(n);


       var data = {
           'projector': tag
       };

       var json = JSON.stringify(data);

       if(tag){
         $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api/delete/inventory/customerlocation/projector",
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




