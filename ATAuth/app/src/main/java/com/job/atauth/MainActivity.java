package com.job.atauth;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.africastalking.AfricasTalking;
import com.africastalking.utils.Logger;

import java.io.IOException;

/**
 * Created by Job on Wednesday : 12/12/2018.
 */
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //connectToServer();
        startActivity(new Intent(this,PhoneAuthActivity.class));
    }


    /*
    implementation of connectToServer()
     */
    private void connectToServer() {

        //Initialize te sdk, and connect to our server. Do this in a try catch block
        try {

            /*
            Put a notice in our log that we are attempting to initialize
             */
            Log.e("NOTICE", "Attempting to initialize server");
            //AfricasTalking.initialize(BuildConfig.RPC_HOST, BuildConfig.RPC_PORT, true);
            String host = "192.168.8.101";
             int port = 8080;
            AfricasTalking.initialize(host, port, true);

            //Use AT's Logger to get any message
            AfricasTalking.setLogger(new Logger() {
                @Override
                public void log(String message, Object... args) {

                    /*
                    Log this too
                     */
                    Log.e("FROM AT LOGGER", message + " " + args.toString());
                }
            });

            /*
            Final log to tell us if successful
             */
            Log.e("SERVER SUCCESS", "Managed to connect to server");
        } catch (IOException e) {

            /*
            Log our failure to connect
             */
            Log.e("SERVER ERROR", "Failed to connect to server");
        }
    }
}
