<?php

    require 'vendor/autoload.php';
    use AfricasTalking\SDK\AfricasTalking;

    session_start();

    // get post variables
    extract($_POST);


    // generate an 8-character long confirmation code
    $characters = str_split("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv");
    
    $confirmation_code = "";

    for ($i=0; $i < 8 ; $i++) { 
       $confirmation_code .= $characters[rand(0, count($characters) - 1)];
    }

    // put the generated confirmation code in a session variable for reference
    $_SESSION['confirmation_code'] = $confirmation_code;

    // the sms API
    $username = 'sandbox'; 
    $apiKey   = '3e539b9e0b405fb4bacaebeba83a3319ff995bfea8db27e4bd5b117d7fe33d1c'; 

    $AT       = new AfricasTalking($username, $apiKey);
   
    $sms        = $AT->sms();

    // $phone extacted from $_POST
    try {

        // replace first '0' in phone number with '254'
        $phone = preg_replace('/^0/', '254', $phone, 1);

        $result = $sms->send([
            'to'      => $phone,
            'message' => $confirmation_code
        ]);
        
        if ($result['status'] == "success") {
           // Message sent successsfully
           // Reload to confrmation page
           header("location:confirm.html");
        }else{
            echo "something went wrong";
        }

    } catch (Exception $e) {
        echo "Error: ".$e->getMessage();
    }
?>