/*
 * *********************************************************************************
 *                                                                                 *
 * Utility functions                                                               *
 *                                                                                 * 
 * *********************************************************************************
 */

/**
 * 
 * @param {String} icon An icon class to be used for the notification.
 * @param {String} type success || danger || warning || info(default)
 * @param {String} message Message to be displayed in the notification body
 * @param {Sting} url If you want the notification to be a link (Optional)
 * @param {String} align Position to be aligned on page right(default) || left
 */
var notify = function(icon,type,message,url,align){
    // Create notification
    $.notify({
        //options
        icon: icon || '',
        message: message,
        url: url || ''
    },
    {
        //settings
        element: 'body',
        type: type || 'info',
        allow_dismiss: true,
        newest_on_top: true,
        showProgressbar: false,
        placement: {
            from: 'top',
            align: align || 'right'
        },
        mouse_over: 'pause',
        offset: 20,
        spacing: 10,
        z_index: 1033,
        delay: 6000,
        template: '<div data-notify="container" class="col-xs-11 col-sm-3 p-20 alert alert-{0}" role="alert">' +
            '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
                '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
        '</div>',
        animate: {
            enter: 'animated fadeIn',
            exit: 'animated fadeOutDown'
        },
        onShow: function() {
            this.css({'width':'auto','height':'auto'});
        },
    });
};

/**
 * Ajax comunication helper for data sending and receiving with the server
 *  
 * @param {String} dataTarget URL tp where to send the request
 * @param {Object} dataSend   An object with data to send with request
 * @param {String} dataType     json || text || html || xml This is whatever the server will respond with
 * @param {String} errorMessage  Message to be displayed when ajax call fails
 * @param {Boolean} formdata True|False whether you are using formdata object
 * 
 * @return {Object} an ajax object of the ajax call
 */
var ajaxComm = function(dataTarget,dataSend,dataType){
    return $.ajax({
                url: dataTarget,
                type: "POST",
                data: dataSend,
                dataType: dataType,
            })
            .fail(error => {
                var icon = "fa fa-warning";
                notify(icon,"danger","Error in server connection");
                console.log(error);
            });
}

/**
 * Sets sweet alert defaults
 * @returns {Object} A swal object
 */
var mySwal =  () => {
    // Set default properties
    return swal.mixin({
                buttonsStyling: false,
                showCancelButton: true,
                confirmButtonClass: 'btn btn-lg btn-success m-5',
                cancelButtonClass: 'btn btn-lg btn-danger m-5',
                inputClass: 'form-control'
            });
};

/**
 * Set form validatorjquery defaults
 */
var initDefaultValidator = () => {
    console.log("Loaded validator defaults");
    
    $.validator.setDefaults({
        debug: true,
        ignore: ':hidden,.select2-search__field',
        errorClass: 'invalid-feedback animated fadeInDown',
        errorElement: 'div',
        errorPlacement: function(error, e) {
            jQuery(e).parents('.form-group').append(error);
        },
        highlight: function(e) {
            jQuery(e).closest('.form-group').removeClass('is-invalid').addClass('is-invalid');
        },
        success: function(e) {
            jQuery(e).closest('.form-group').removeClass('is-invalid');
            jQuery(e).remove();
        }
    });

    //Add method to check file size
    $.validator.addMethod("filesize", function(value, element, param) {
        var isOptional = this.optional(element),
            file;
        
        if(isOptional) {
            return isOptional;
        }
        
        if ($(element).attr("type") === "file") {
            
            if (element.files && element.files.length) {
                
                file = element.files[0];            
                return ( file.size && file.size <= param ); 
            }
        }
        return false;
    }, "File size is too large.");
}

/**
 * Set defaults for form Wizards
 * For more examples check https://github.com/VinceG/twitter-bootstrap-wizard
 */
var initWizardDefaults = function(){
    console.log("Loaded wizard defaults");
    jQuery.fn.bootstrapWizard.defaults.tabClass         = 'nav nav-tabs';
    jQuery.fn.bootstrapWizard.defaults.nextSelector     = '[data-wizard="next"]';
    jQuery.fn.bootstrapWizard.defaults.previousSelector = '[data-wizard="prev"]';
    jQuery.fn.bootstrapWizard.defaults.firstSelector    = '[data-wizard="first"]';
    jQuery.fn.bootstrapWizard.defaults.lastSelector     = '[data-wizard="last"]';
    jQuery.fn.bootstrapWizard.defaults.finishSelector   = '[data-wizard="finish"]';
    jQuery.fn.bootstrapWizard.defaults.backSelector     = '[data-wizard="back"]';
};