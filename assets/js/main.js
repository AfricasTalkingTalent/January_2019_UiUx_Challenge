var main = function () {
    let initValidator = () => {
        //masked input for phone number
        $('#phone_number').mask('999999999');
        $('.signup_form').validate({
            rules:{
                'phone_number': {
                    minlength: 9 
                },
                'pass-conf':{
                    equalTo: '#pass'
                }
            },
            messages:{
                'phone_number': {
                    minlength: "Enter a valid phone number"
                },
                'pass-conf': {
                    equalTo: "Passwords do not match"
                }
            },
            submitHandler: form => {
                console.log("You should work");
            }
        });
        $('.signup_form').submit(event => {
            let _this = event.target;
            event.preventDefault();
            let action = _this.action;
            let send_data = $(_this).serializeArray();
            
            $.ajax({
                url: action,
                type: "POST",
                data: send_data,
                dataType: "json",
                
            }).done(data => {
                console.log(data);
                
            });
            // ajaxComm(action,send_data,'json')
            // .done(data => {
            //     console.log(data);
            // });
            
        });
    }

    return {
        init : () => {
            initDefaultValidator();
            initValidator();
        }
    }
}();

$(document).ready(main.init());