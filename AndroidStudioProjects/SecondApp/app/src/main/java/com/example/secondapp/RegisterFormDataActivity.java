package com.example.secondapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class RegisterFormDataActivity extends AppCompatActivity {

    TextView lblRegister;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register_form_data);

        lblRegister = findViewById(R.id.lbl_Register);

        String idUser = getIntent().getStringExtra("idUser");  //Intent created in MainActivy puts data taked here
        lblRegister.setText("Welcome to Dashboard " + idUser);

        Log.d("Msg: ", "Event On Create");

    }

    @Override
    protected void onPause() {
        super.onPause();

        Log.d("Msg: ", "Event On Pause");

    }

    @Override
    protected void onStop() {
        super.onStop();

        Log.d("Msg: ", "Event On Stop");
    }

    @Override
    protected void onRestart() {
        super.onRestart();

        Log.d("Msg: ", "Event On Restart");
    }

}
