package com.example.secondapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.util.Log;
import android.view.View;

import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText txtIdUser;
    Button btnGoToRegisterFormData, btnGoToRegisterUser,  btnCallFriend, btnUbicate;
    TextView lblResponse;
    ImageView imgSend, imgGoWeb, imgGeoLoc, imgInitUser, imgGoCamera;

    final int GO_TO_REGISTER_FORM_DATA = 0;
    final int TAKE_PICTURE = 1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Log.d("Msg: ", "Event On Create");

        txtIdUser = findViewById(R.id.txt_IdUser);
        lblResponse = findViewById(R.id.lbl_Status);

        imgInitUser = findViewById(R.id.img_InitUser);
        imgGoCamera =  findViewById(R.id.img_GoCamera);
        imgGeoLoc = findViewById(R.id.img_GeoLoc);
        imgGoWeb =  findViewById(R.id.img_GoWeb);
        imgSend =  findViewById(R.id.img_Send);

        btnGoToRegisterFormData = findViewById(R.id.btn_ResetAll);
        btnGoToRegisterUser = findViewById(R.id.btn_CallUser);

        // Simple start another activity
        btnGoToRegisterFormData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){

                // Read Name
                String idUser = txtIdUser.getText().toString().trim();

               if( txtIdUser.getText()==null){
                   Toast.makeText(MainActivity.this, "Input your ID." ,Toast.LENGTH_SHORT).show();
               }else{

                   // Put Text
                   lblResponse.setText(getString(R.string.register_user_correct) +":" + idUser);
                   lblResponse.setVisibility(View.VISIBLE);

                   // Intent passing data form Main to Dashboard - Simple startActivity
                   Intent intent = new Intent(MainActivity.this, RegisterFormDataActivity.class);
                   intent.putExtra("idUser", idUser);  // Passing info during action
                   startActivity(intent);
               }

            }
        });

        // Start another activity flagged for Result
        imgInitUser.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                    // Read data
                    String idUser = txtIdUser.getText().toString().trim();
                    // Intent from Dashboard to Main --> use startActivityForResult to call
                    Intent intent = new Intent(MainActivity.this, RegisterUserActivity.class);
                    intent.putExtra("idUser", idUser);  // Passing info during action
                    startActivityForResult(intent, GO_TO_REGISTER_FORM_DATA); //Its a flag for event of intent
                }

        });


        btnGoToRegisterUser.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:5142130644"));
                startActivity(intent);

            }
        });

        imgGoCamera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, RegisterFormDataActivity.class);
                startActivityForResult(intent, TAKE_PICTURE);

            }
        });

        imgGeoLoc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("geo:0,0?q=7105 Rue de Lanivet, Brossard"));
                startActivity(intent);

            }
        });

        imgGoWeb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.discovery.com"));
                startActivity(intent);

            }
        });

        imgSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                imgSend.setImageResource(R.drawable.calling); // to change dinamacally
                Intent intent = new Intent(Intent.ACTION_DIAL);
                startActivity(intent);

            }
        });

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        //When intent flagged in another activity its finished, it will be here.
        //request code: to identitfy intent_action
        //result code: to run depends of results status
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == GO_TO_REGISTER_FORM_DATA){

            if (resultCode == RESULT_OK){

                lblResponse.setText(data.getStringExtra("status") + "_" + data.getStringExtra("data"));

            }

            if (resultCode == RESULT_CANCELED){
                lblResponse.setText("Action Cancelled by user");
            }

        } else if (requestCode == TAKE_PICTURE){

            if (resultCode == RESULT_OK){

                lblResponse.setText(data.getStringExtra("status"));

            }

            if (resultCode == RESULT_CANCELED){
                lblResponse.setText("DataForm not received");
            }

        }


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