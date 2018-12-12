$(document).ready(function(){
  $('#goRight').on('click', function(){
    $('#slideBox').animate({
      'marginLeft' : '0'
    });
    $('.topLayer').animate({
      'marginLeft' : '100%'
    });
  });
  $('#goLeft').on('click', function(){
    if (verifyName() && verifyNumber() && verifyPassword()) {
      $('#slideBox').animate({
        'marginLeft' : '50%'
      });
      $('.topLayer').animate({
        'marginLeft': '0'
      });
    }
  });
});

function verifyName() {
  name = $('#name').val();

  if (name == "") {
    alert("Name must be filled");
    return false;
  }

  return true;
}

function verifyNumber() {
  num = $.trim($('#number').val()).replace(/\s+/g, '');

  var phoneno = /^\d{10}$/;
  var longphoneno = /^\+254?([0-9]{9})$/;

  if (num == "" || !$.isNumeric(num)) {
    alert("Number must be filled and be a number");
    return false;
  }

  if(num.match(phoneno) || num.match(longphoneno)) {
    $('#vermessage').html("A one time password was sent to " + num + "<br> Please confirm the code");
    return true;
  } else {
    alert("Please input a valid number");
  }

  return false;
}

function verifyPassword() {
  password = $('#password').val();
  cpassword = $('#password-confirm').val();

  if (password == "" || cpassword == "") {
    alert("Password and Password confirmation must be filled");
    return false;
  }

  if (password != cpassword){
    alert("Passwords have to match");
    return false;
  }

  return true;
}