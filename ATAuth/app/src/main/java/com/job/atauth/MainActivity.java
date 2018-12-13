package com.job.atauth;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;

import com.africastalking.AfricasTalking;
import com.africastalking.utils.Logger;

import java.io.IOException;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

/**
 * Created by Job on Wednesday : 12/12/2018.
 */
public class MainActivity extends AppCompatActivity {

    @BindView(R.id.ph_username)
    TextInputLayout phUsername;
    @BindView(R.id.ph_password) TextInputLayout phPassword;
    @BindView(R.id.textView)
    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ButterKnife.bind(this);

    }

    @OnClick(R.id.ph_continue) void onPhContinueClick() {
        if (validateCode()){
            sendToHomeActivity();
        }
    }

    private void sendToHomeActivity() {
        Intent main = new Intent(this, HomeActivity.class);
        main.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(main);
        finish();
    }

    private boolean validateCode() {
        boolean valid = true;

        String username = phUsername.getEditText().getText().toString();
        String pss = phPassword.getEditText().getText().toString();

        if (username.isEmpty()) {
            phUsername.setError("invalid username");
            valid = false;
        } else {
            phUsername.setError(null);
        }

        if (pss.isEmpty()) {
            phPassword.setError("invalid password");
            valid = false;
        } else {
            phPassword.setError(null);
        }

        return valid;
    }

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
