package com.example.secondapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

// Another way to user onclick, implements View.OnClickListener
public class RegisterUserActivity extends AppCompatActivity implements View.OnClickListener{

    TextView lblDashBoardUser;
    TextView txtData;
    Button btnBackToMain, btnCancel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register_user);

        // Objects from layout selected
        lblDashBoardUser = findViewById(R.id.lbl_Dashboard_User);
        txtData = findViewById(R.id.txt_Data);
        btnBackToMain = findViewById(R.id.btn_SendToMain);
        btnCancel = findViewById(R.id.btn_Cancel);

        // In order to use implements View.OnClickListener
        btnBackToMain.setOnClickListener(this);
        btnCancel.setOnClickListener(this);

        // Taking data from Main to RegisterUser with intents
        String name = getIntent().getStringExtra("idUser");  //Intent created in MainActivy puts data taked here
        lblDashBoardUser.setText("Welcome to Dashboard " + name);

    }


    @Override
    public void onClick(View view) {

        // Read data
        String data= txtData.getText().toString().trim();;
        if( data==null){
            Toast.makeText(RegisterUserActivity.this, "Data cant be null" ,Toast.LENGTH_SHORT).show();
        }else{

            // Intent to passing DATA from DashboardUser to Main
            Intent intent = new Intent();

            //  ACCESS TO DIFFERENTE CLICKABLE OBJECTS
            if (view.getId() == R.id.btn_SendToMain){

                // Set Response
                intent.putExtra("data", data);
                intent.putExtra("status", "Sended by user" );
                setResult(RESULT_OK, intent);
                RegisterUserActivity.this.finish();  //Remove activiey form memory

            }else if (view.getId() == R.id.btn_Cancel){

                intent.putExtra("status", "Cancel by user" );
                setResult(RESULT_CANCELED);
                RegisterUserActivity.this.finish(); // always finish

            }else if (view.getId() == R.id.lbl_Dashboard_User){

                intent.putExtra("status", "Invalid action by user" );
                setResult(RESULT_CANCELED);
                RegisterUserActivity.this.finish();

            }

        }


    }
}