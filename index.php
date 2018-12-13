<!DOCTYPE html>
<html>
<head>
  <title>User Registration</title>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
  <div class="container">
<form method="POST">
  <h1><u>User Registration Form</u></h1>
  <div class="form-group">
    <label for="firstName">Username:</label>
    <input type="text" class="form-control" id="userName">
  </div>
  <div class="form-group">
    <label for="lastName">Phone Number:</label>
    <input type="text" class="form-control" name="phoneNo" placeholder="Use format +254XXXXXXXXX" required>
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <button type="submit" name="submit"class="btn btn-default"><a href="#myModal" data-toggle="modal" data-target="#myModal">Register</a></button>
</form>
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title" id="myModalLabel">Phone Number Verification</h4>
            </div>
            <div class="modal-body">
              Kindly confirm that you have received verification token via the phone number to complete registration.
              <br>
              Enter Verification code
              <input type="text" name="code">
              <button type="submit" name="codeResend">Resend Code</button>
              <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary">Complete Sign Up</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </body>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="js/script.js"></script>
</body>
</html>
<?php
require 'vendor/autoload.php';
use AfricasTalking\SDK\AfricasTalking;


if(isset($_POST['submit'])){

//function sendMessage(){



// Set your app credentials
$username   = "sandbox";
$apikey     = "26752227ddd2a565cc3242ce57948f4a568c6d108cb7dab5647d0e44725af9f2";

// Initialize the SDK
$AT         = new AfricasTalking($username, $apikey);

// Get the SMS service
$sms        = $AT->sms();

// Set the numbers you want to send to in international format
$recipient = $_POST['phoneNo'];

//function to generate random verification token to be sent to recipient
function generateRandomString($length = 8) {
    return substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);
}

// Set your message
$message    = "Welcome to Stephen Odipo Inc. Kindly use this verification code ". generateRandomString(). " to complete sign up";

try {
    // Thats it, hit send and we'll take care of the rest
    $result = $sms->send([
        'to'      => $recipient,
        'message' => $message
    ]);

    print_r($result);
} catch (Exception $e) {
    echo "Error: ".$e->getMessage();
}
}
?>
