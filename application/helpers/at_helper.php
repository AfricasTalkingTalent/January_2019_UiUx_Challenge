<?php defined('BASEPATH') or exit('No direct script access allowed'); 

/**
 * @return String Properties with key and secret of AT API
 */
function at_credentials(){
    return '9374db8271f868918b7d3e9d3eca33c2c7a6a18a0f94cb0dec672bda30b30ab7';
}

/**
 * Generates a random code to send to user
 * Depending on passed length
 */
function generate_auth_token($length){
    return random_string('alnum', $length);
}

function send_msg($to,$msg){
    // use AfricasTalking\SDK\AfricasTalking;

    // Set your app credentials
    $username   = "sandbox";
    $apikey     = at_credentials();

    // Initialize the SDK
    $AT         = new AfricasTalking\SDK\AfricasTalking($username, $apikey);

    // Get the SMS service
    $sms        = $AT->sms();

    // Set the numbers you want to send to in international format
    $recipients = $to;

    // Set your message
    $message    = $msg;

    try {
        // Thats it, hit send and we'll take care of the rest
        $result = $sms->send([
            'to'      => $recipients,
            'message' => $message
        ]);

        return $result['status'] == 'success';
    } catch (Exception $e) {
        echo "Error: ".$e->getMessage();
    }
}