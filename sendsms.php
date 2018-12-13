<!DOCTYPE html>
<html>
<head>
	<title>SignUp Process</title>
	 <script src="dist/sweetalert.min.js"></script>
    <link rel="stylesheet" type="text/css" href="dist/sweetalert.css">
</head>
<body>
	
<?php
//connect to the db
require "DBConnect.php";
global $db;

//connect to africa's talking api
require 'vendor/autoload.php';
use AfricasTalking\SDK\AfricasTalking;

//getting the token
$code = '';
for ($i=0; $i < 6; $i++) { 
	$code .= mt_rand(0,9);
}
$key = 'wejsgbvnb78sgvxc8FYY68JSD6xvxv';
$token = crypt($code, $key);

//signup the user to the db
if(isset($_POST['signup'])){

    $uname = $_POST['username'];
    $phne = $_POST['phne'];
    $password = $_POST['pass'];
    $hash = md5($password);

    $sql="INSERT INTO `user`(`userName`, `phoneNumber`, `verificationToken`, `password`) VALUES ('$uname', '$phne', '$token', '$hash')";
    $result = mysqli_query($db,$sql);
    
}

if ($result) {
	// using the credentials
$username   = "sandbox";
$apiKey     = "14455b63259905b9422d216c57f4766c2437547c5b605c1a24aca60dacaa7fe4";

// getting the SDK
$AT         = new AfricasTalking($username, $apiKey);

// using the sms service
$sms        = $AT->sms();

// Set the numbers you want to send to in international format
$recipient = $phne;

// Set your message
$message    = "Your verification code is:" .$code;

try {
    // Thats it, hit send and we'll take care of the rest
    $result = $sms->send([
        'to'      => $recipient,
        'message' => $message
    ]);

   // print_r($result);
} catch (Exception $e) {
    echo "Error: ".$e->getMessage();
}

if ($result) {

        session_start();
        $_SESSION['yes'] = $uname;

	//show verification sent message
	 ?>
        <script>
            swal({
                title: "Signup Success",
                text: "Verification code sent to your sms",
                type: "success",
                timer: 2500,
                showConfirmButton: false
            });
            setTimeout(function () {
                location.href = "index.php"
            }, 1000);
        </script>
    <?php
}

}

?>
	
</body>
</html>
