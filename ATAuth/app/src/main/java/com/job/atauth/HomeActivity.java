package com.job.atauth;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.button.MaterialButton;
import android.support.v7.app.AppCompatActivity;
import android.widget.ImageView;
import android.widget.TextView;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class HomeActivity extends AppCompatActivity {

    @BindView(R.id.user_info_image) ImageView userInfoImage;
    @BindView(R.id.user_info_username) TextView userInfoUsername;
    @BindView(R.id.user_info_time) TextView userInfoPhone;
    @BindView(R.id.user_info_course) TextView userInfoCourse;
    @BindView(R.id.user_info_logout) TextView userInfoLogout;
    @BindView(R.id.button) MaterialButton button;

    private SharedPreferences mSharedPreferences;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.userinfo_layout);
        ButterKnife.bind(this);

        mSharedPreferences = getPreferences(MODE_PRIVATE);

        loadUI();
    }

    private void loadUI() {
        String phone = mSharedPreferences.getString("PHONE","");
        String user = mSharedPreferences.getString("USER","");

        userInfoUsername.setText(user);
        userInfoPhone.setText("phone: "+phone);
    }

    @OnClick(R.id.button)
    public void loggout(){
        Intent main = new Intent(this, PhoneAuthActivity.class);
        main.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(main);
        finish();
    }
}
