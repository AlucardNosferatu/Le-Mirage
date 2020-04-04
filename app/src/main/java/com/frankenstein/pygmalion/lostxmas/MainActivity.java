package com.frankenstein.pygmalion.lostxmas;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button head = findViewById(R.id.Button_Head);
        Button chest = findViewById(R.id.Button_Chest);
        Button waist = findViewById(R.id.Button_Waist);
        Button right_leg = findViewById(R.id.Button_Right_Leg);
        Button left_leg_1 = findViewById(R.id.Button_Left_Leg_1);
        Button left_leg_2 = findViewById(R.id.Button_Left_Leg_2);
        final TextView reply = findViewById(R.id.Text_Reply);
        head.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.head_reply));
            }
        });
        chest.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.chest_reply));
            }
        });
        waist.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.waist_reply));
            }
        });
        right_leg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.right_leg_reply));
            }
        });
        left_leg_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.left_leg_1_reply));
            }
        });
        left_leg_2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reply.setText(getString(R.string.left_leg_2_reply));
            }
        });

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
