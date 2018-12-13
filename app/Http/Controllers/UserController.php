<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use AfricasTalking\SDK\AfricasTalking;

class UserController extends Controller
{
    public function message(Request $request) {
      $username = 'sandbox';
      $apikey = '7dbf3790d6a2e46cd3156b0f54fc1b2620b70dc78ab294a52fca8e4391969697';

      $AT = new AfricasTalking($username, $apikey);

      $sms = $AT->sms();

      $recipient = $request->phone_no;

      $message = 1234;

      try {
          $result = $sms->send([
              'to'      => $recipient,
              'message' => $message
          ]);
          return [$result, "message" => $message];
      } catch (Exception $e) {
          return "Error: ".$e->getMessage();
      }
    }
      
}
