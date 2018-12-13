package com.job.atauth;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.support.design.widget.Snackbar;
import android.support.design.widget.TextInputLayout;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.africastalking.AfricasTalking;
import com.africastalking.models.sms.Recipient;
import com.africastalking.services.SmsService;
import com.africastalking.utils.Logger;

import java.io.IOException;
import java.net.ConnectException;
import java.util.List;
import java.util.Random;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;
import cn.pedant.SweetAlert.SweetAlertDialog;


public class PhoneAuthActivity extends AppCompatActivity {

    private static final String TAG = "phone";
    public static final int RC_SIGN_IN = 1001;
    private static final int PERMISSION_REQUEST_CODE = 1;

    private static final String KEY_VERIFY_IN_PROGRESS = "key_verify_in_progress";

    private static final int STATE_INITIALIZED = 1;
    private static final int STATE_CODE_SENT = 2;
    private static final int STATE_VERIFY_FAILED = 3;
    private static final int STATE_VERIFY_SUCCESS = 4;
    private static final int STATE_SIGNIN_FAILED = 5;
    private static final int STATE_SIGNIN_SUCCESS = 6;

    @BindView(R.id.ph_number)
    TextInputLayout phNumber;
    @BindView(R.id.ph_code)
    TextInputLayout phCode;
    @BindView(R.id.ph_continue)
    Button phContinue;
    @BindView(R.id.signup_head)
    TextView signupHead;

    private SharedPreferences.Editor sharedPreferencesEditor;
    private SharedPreferences mSharedPreferences;
    private String mPhoneNum;

    private boolean mVerificationInProgress = false;
    private String mVerificationId;
    private String wantPermission = Manifest.permission.READ_PHONE_STATE;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_phone_auth);
        ButterKnife.bind(this);

        connectToServer();

        if (savedInstanceState != null) {
            onRestoreInstanceState(savedInstanceState);
        }

        sharedPreferencesEditor = getPreferences(MODE_PRIVATE).edit();
        mSharedPreferences = getPreferences(MODE_PRIVATE);


        //auth set phone
        if (!checkPermission(wantPermission)) {
            requestPermission(wantPermission);
        } else {
            if (getPhone() != null) {
                phNumber.getEditText().setText(getPhone());
            }
        }

        //TODO: REMOVE: TESTING PURPOSES ONLY
        if (BuildConfig.DEBUG) {

            // The test phone number and code should be whitelisted in the console.
            String phoneNumber = "+254711223344";
            String smsCode = "123456";

        }
    }

    private boolean isValidMobile(String phone) {
        if (phone.isEmpty()) {
            return false;
        }
        return Patterns.PHONE.matcher(phone).matches();
    }

    @OnClick(R.id.logo)
    public void onLogoClicked() {
    }

    private void tweakUIInit() {

        //ui editing
        phNumber.setVisibility(View.VISIBLE);

        phCode.setVisibility(View.GONE);

        signupHead.setText(R.string.enter_phonenumber);
        phContinue.setText(R.string.continue_txt);

    }

    private void tweakUICodeIncoming() {

        //ui editing: number entered
        phNumber.setVisibility(View.GONE);

        phCode.setVisibility(View.VISIBLE);

        signupHead.setText(R.string.enter_sms_code);
        phContinue.setText(R.string.verify_text);

    }

    private void tweakUISmsFailed() {

        //ui editing
        phNumber.setVisibility(View.VISIBLE);

        phCode.setVisibility(View.GONE);

        signupHead.setText(R.string.enter_phonenumber);
        phContinue.setText(R.string.continue_txt);

    }

    @OnClick(R.id.ph_continue)
    public void onPhContinueClicked() {

        String CN = getString(R.string.continue_txt);
        String VR = getString(R.string.verify_text);

      /*  final SweetAlertDialog pDialog = new SweetAlertDialog(this, SweetAlertDialog.PROGRESS_TYPE);
        pDialog.getProgressHelper().setBarColor(Color.parseColor("#FF4081"));
        pDialog.setTitleText("SMS sent" + "to " + mPhoneNum);
        pDialog.setContentText("Enter code to continue");
        pDialog.setCancelable(true);
        pDialog.setCanceledOnTouchOutside(true);
        pDialog.show();*/


        if (phContinue.getText().equals(CN)) {
            if (validatePhone()) {

                tweakUICodeIncoming();
                sharedPreferencesEditor.putString("PHONE",mPhoneNum);
                showSnackbar("SMS sent" + " to : " + mPhoneNum);
                startPhoneNumberVerification(mPhoneNum);
            }
        }

        if (phContinue.getText().equals(VR)) {
            if (validateCode()) {

                String code = mSharedPreferences.getString("TOKEN","");

                Toast.makeText(this, "Successfull", Toast.LENGTH_SHORT).show();
                sendUserToMainActivity();
            }
        }
    }

    private boolean validatePhone() {
        boolean valid = true;

        String phone = phNumber.getEditText().getText().toString();

        if (phone.isEmpty()) {
            phNumber.setError("enter a valid phone number");
            valid = false;
        } else {
            phNumber.setError(null);
            Log.d(TAG, "validatePhone: " + phone);
            //mPhoneNum = "+254" + phone;
            mPhoneNum = phone;
        }

        return valid;
    }

    private boolean validateCode() {
        boolean valid = true;

        String code = phCode.getEditText().getText().toString();

        //TODO: verify sent code too

        if (code.isEmpty()) {
            phCode.setError("invalid code");
            valid = false;
        } else {
            phCode.setError(null);
        }

        return valid;
    }


    private void sendUserToMainActivity() {
        Intent main = new Intent(this, MainActivity.class);
        main.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(main);
        finish();
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putBoolean(KEY_VERIFY_IN_PROGRESS, mVerificationInProgress);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
        mVerificationInProgress = savedInstanceState.getBoolean(KEY_VERIFY_IN_PROGRESS);
        if (mVerificationInProgress) {
            tweakUICodeIncoming();
        }
    }

    private void startPhoneNumberVerification(String phoneNumber) {

        String message = generateAuthToken();
        phCode.getEditText().setText(message);
        sharedPreferencesEditor.putString("TOKEN",message);
        sendMessage(phoneNumber, message);
        asyncTimerSimulator();
    }


    private void updateUI(int uiState, final SweetAlertDialog pDialog) {
        switch (uiState) {
            case STATE_INITIALIZED:
                // Initialized state, show only the phone number field and start button

                tweakUIInit();
                break;
            case STATE_CODE_SENT:
                // Code sent state, show the verification field, the

                //tweakUICodeIncoming();
                showSnackbar(getString(R.string.status_code_sent));

                break;
            case STATE_VERIFY_FAILED:
                // Verification has failed, show all options

                tweakUISmsFailed();
                showSnackbar("Number verification failed", "Retry", new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        onPhContinueClicked();
                    }
                });
                break;
            case STATE_VERIFY_SUCCESS:
                // Verification has succeeded, proceed to firebase sign in
                //disableViews(mStartButton, mVerifyButton, mResendButton, mPhoneNumberField, mVerificationField);
                //mDetailText.setText(R.string.status_verification_succeeded);
                tweakUICodeIncoming();

                break;
            case STATE_SIGNIN_FAILED:
                // No-op, handled by sign-in check

                if (pDialog != null) {
                    pDialog.changeAlertType(SweetAlertDialog.ERROR_TYPE);
                    pDialog.setTitle(getString(R.string.status_verification_failed));
                    pDialog.setConfirmClickListener(new SweetAlertDialog.OnSweetClickListener() {
                        @Override
                        public void onClick(SweetAlertDialog sweetAlertDialog) {
                            sweetAlertDialog.dismiss();
                        }
                    });
                }

                tweakUISmsFailed();
                showSnackbar("Number verification failed", "Retry", new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        onPhContinueClicked();
                    }
                });

                break;
            case STATE_SIGNIN_SUCCESS:
                tweakUICodeIncoming();
                // Np-op, handled by sign-in check
                if (pDialog != null) {
                    pDialog.changeAlertType(SweetAlertDialog.SUCCESS_TYPE);
                    pDialog.dismissWithAnimation();

                }
                sendUserToMainActivity();
                break;
        }
    }

    @Override
    protected void onStart() {
        super.onStart();

    }

    private void requestPermission(String permission) {
        if (ActivityCompat.shouldShowRequestPermissionRationale(this, permission)) {
            Toast.makeText(this, "Phone state permission allows us to get phone number. Please allow it for additional functionality.", Toast.LENGTH_LONG).show();
        }
        ActivityCompat.requestPermissions(this, new String[]{permission}, PERMISSION_REQUEST_CODE);
    }

    private String getPhone() {
        TelephonyManager phoneMgr = (TelephonyManager) this.getSystemService(Context.TELEPHONY_SERVICE);
        if (ActivityCompat.checkSelfPermission(this, wantPermission) != PackageManager.PERMISSION_GRANTED) {
            return "";
        }
        return phoneMgr.getLine1Number();
    }

    private boolean checkPermission(String permission) {
        if (Build.VERSION.SDK_INT >= 23) {
            int result = ContextCompat.checkSelfPermission(this, permission);
            if (result == PackageManager.PERMISSION_GRANTED) {
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    }

    private void showSnackbar(final String mainTextStringId) {
        Snackbar.make(
                this.findViewById(android.R.id.content),
                mainTextStringId,
                Snackbar.LENGTH_LONG)
                .show();
    }

    private void showSnackbar(final String mainTextStringId, final String actionStringId,
                              View.OnClickListener listener) {
        Snackbar.make(
                findViewById(android.R.id.content),
                mainTextStringId,
                Snackbar.LENGTH_INDEFINITE)
                .setAction(actionStringId, listener).show();
    }

    /*
 Implementation of our sendMessage method
  */
    private void sendMessage(final String number, final String message) {

        /*
        get our sms service and use it to send the message
         */
        @SuppressLint("StaticFieldLeak") AsyncTask<Void, String, Void> smsTask = new AsyncTask<Void, String, Void>() {
            @Override
            protected Void doInBackground(Void... voids) {

                /*
                put it in try catch block
                 */
                try {

                    //Log this
                    Log.e("SMS INFO", "Attempting to send SMS");

                    //get the sms service
                    SmsService smsService = AfricasTalking.getSmsService();

                    //Send the sms, get the response
                    List<Recipient> recipients = smsService.send(message, new String[]{number});

                    /*
                    Log the response
                     */
                    Log.e("SMS RESPONSE", recipients.get(0).messageId + " " + recipients.get(0).status);

                    if (recipients.get(0).status.equals("Success")) {

                    }

                } catch (ConnectException e) {

                    Log.e("Connection FAILURE", e.toString());
                } catch (IOException e) {

                    Log.e("SMS FAILURE", e.toString());
                }

                return null;
            }
        };

        smsTask.execute();
    }

    // a four auth code
    private String generateAuthToken() {
        Random random = new Random();
        StringBuilder authBuilder = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            int code = random.nextInt(4);
            authBuilder.append(code);
        }

        return authBuilder.toString();
    }

    private void connectToServer() {

        //Initialize te sdk, and connect to our server. Do this in a try catch block
        try {

            /*
            Put a notice in our log that we are attempting to initialize
             */
            Log.e("NOTICE", "Attempting to initialize server");
            //AfricasTalking.initialize(BuildConfig.RPC_HOST, BuildConfig.RPC_PORT, true);
            String host = "192.168.8.100";
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

    /*
    * Simulating SMS response time
    * RESEND SMS logic on failure
    * */
    private void asyncTimerSimulator(){

        final SweetAlertDialog pDialog = new SweetAlertDialog(this, SweetAlertDialog.PROGRESS_TYPE);
        pDialog.getProgressHelper().setBarColor(Color.parseColor("#FF5521"));
        pDialog.setCancelable(false);
        pDialog.show();

        new CountDownTimer(10000, 1000) {

            public void onTick(long millisUntilFinished) {
                String timer = (Util.toMinutes(millisUntilFinished) +" : " + Util.toSec(millisUntilFinished));
                pDialog.setTitleText("Waiting SMS confirmation");
                pDialog.setContentText(""+timer);

            }

            public void onFinish() {
                //done
                pDialog.changeAlertType(SweetAlertDialog.SUCCESS_TYPE);
                pDialog.setConfirmClickListener(new SweetAlertDialog.OnSweetClickListener() {
                    @Override
                    public void onClick(SweetAlertDialog stDialog) {
                        stDialog.dismissWithAnimation();
                        String code = mSharedPreferences.getString("TOKEN","");
                        phCode.getEditText().setText(code);
                    }
                });
            }
        }.start();
    }
}
