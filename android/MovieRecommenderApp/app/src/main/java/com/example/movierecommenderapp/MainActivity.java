package com.example.movierecommenderapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText mname;
    Button recommend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mname=findViewById(R.id.movie);
        recommend=findViewById(R.id.recommend);
        recommend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String inp=mname.getText().toString();
                Intent intent=new Intent(MainActivity.this,Recommendations.class);
                intent.putExtra("moviename",inp);
                startActivity(intent);
            }
        });
    }
}