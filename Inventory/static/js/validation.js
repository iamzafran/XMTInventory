function validate(required_class){

    var isValid = true;
    $(required_class).each(function(){

        var value = $(this).val();
        console.log(value);

        if(!value){
            $(this).parent().addClass("has-danger");
            isValid = false;
            console.log("false");
        }else {
            $(this).parent().removeClass("has-danger");
        }
    });

    return isValid;
}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}