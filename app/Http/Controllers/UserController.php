<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use AfricasTalking\SDK\AfricasTalking;
use App\User;

class UserController extends Controller
{
    public function message(Request $request) {
      $username = 'sandbox';
      $apikey = '7dbf3790d6a2e46cd3156b0f54fc1b2620b70dc78ab294a52fca8e4391969697';

      $AT = new AfricasTalking($username, $apikey);

      $sms = $AT->sms();

      $recipient = $request->phone_no;
      $randomNo = mt_rand(pow(10, 3), pow(10, 4)-1);
      $message = $randomNo;

      try {
        $result = $sms->send([
          'to'      => $recipient,
          'message' => $message
        ]);
        return ["response" => $result, "message" => $message];
      } catch (Exception $e) {
        return "Error: ".$e->getMessage();
      }
    }

    public function register(Request $request) {
      $user =  User::create([
        'first_name' => $request->first_name,
        'last_name' => $request->last_name,
        'country_code' => $request->country_code,
        'phone_no' => $request->phone_no,
        'password' => Hash::make($request->password),
      ]);
      return 'success';
    }
      
}
