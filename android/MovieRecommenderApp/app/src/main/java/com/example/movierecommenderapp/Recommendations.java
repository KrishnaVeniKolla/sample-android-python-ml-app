package com.example.movierecommenderapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.method.ScrollingMovementMethod;
import android.widget.TextView;

public class Recommendations extends AppCompatActivity {
    TextView title,results;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommendations);
        title=findViewById(R.id.mname);
        results=findViewById(R.id.recmovies);
        String movie=getIntent().getStringExtra("moviename");
        title.setText("Recommendations for "+movie+" are");
        results.setMovementMethod(new ScrollingMovementMethod());

    }
}