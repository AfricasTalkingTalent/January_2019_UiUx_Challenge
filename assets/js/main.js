var main = function () {
    let initValidator = () => {
        //masked input for phone number
        $('#phone_number').mask('999999999');
        $('.signup_form').validate({
            rules:{
                'phone_number': {
                    minlength: 9,
                    remote: {
                        url: baseURL+"main/check_phone_exists",
                        type: "POST",
                        data: { 
                            phone_number : () => { return "+254"+$('input[name="phone_number"]').val();}
                        },
                        dataType: 'json'                        
                    }
                },
                'pass-conf':{
                    equalTo: '#pass'
                }
            },
            messages:{
                'phone_number': {
                    minlength: "Enter a valid phone number",
                    remote: "Phone number already exists"
                },
                'pass-conf': {
                    equalTo: "Passwords do not match"
                }
            }
        });

        $('.signup_form').submit(event => {
            let _this = event.target;
            event.preventDefault();
            let action = _this.action;
            let send_data = $(_this).serializeArray();
            
            ajaxComm(action,send_data,'json')
            .done(data => {
                if(data.type == "success"){
                    $('[href="#verification_content"]').trigger('click');
                }else{
                    notify(data.icon,data.type,data.msg);
                }
                $(_this).trigger('reset');
            });
            
        });
    }

    let initTokenValidation = () => {
        $('#auth_token_form').submit(event => {
            event.preventDefault();
            let _this = event.target;
            let action = _this.action;
            let sendData = $(_this).serializeArray();

            ajaxComm(action,sendData,"json")
            .done(data => {
                if(data){
                    //true
                    notify("fa fa-info","info","Account has been succefully verified. <br> Welcome to Jenga");
                    $(_this).trigger('reset');
                }else{
                    //false
                    notify("fa fa-warning","warning","Code is invalid.");
                }
            });

        });
    }

    return {
        init : () => {
            initDefaultValidator();
            initValidator();
            initTokenValidation();
        }
    }
}();

$(document).ready(main.init());