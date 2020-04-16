package com.example.a225try5;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TimePicker;
import android.widget.Toast;

import java.util.Calendar;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{
    //variables here boi ;)
    private int notificationId = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.setBtn).setOnClickListener(this);
        findViewById(R.id.cancelBtn).setOnClickListener(this);
    }

    @Override
    public void onClick(View view){

        //Intent also in this part on this onclick
        EditText editText = findViewById(R.id.editText);
        TimePicker timePicker = findViewById(R.id.timePicker);

        Intent intent = new Intent(MainActivity.this, AlarmReceiever.class);
        intent.putExtra("notificationId",notificationId);
        intent.putExtra("ToDo",editText.getText().toString());

        PendingIntent alarmIntent = PendingIntent.getBroadcast(MainActivity.this,0, intent,PendingIntent.FLAG_CANCEL_CURRENT);
        AlarmManager alarm = (AlarmManager) getSystemService(ALARM_SERVICE);

        switch (view.getId()){
            case R.id.setBtn:
                int hr = timePicker.getCurrentHour();
                int min = timePicker.getCurrentMinute();
                Calendar  calendar = Calendar.getInstance();
                calendar.set(Calendar.HOUR_OF_DAY,hr);
                calendar.set(Calendar.MINUTE,min);
                calendar.set(Calendar.SECOND,0);
                long  aST = calendar.getTimeInMillis();

                alarm.set(AlarmManager.RTC_WAKEUP,aST, alarmIntent);
                Toast.makeText(this,"All set !",Toast.LENGTH_SHORT).show();
                break;

            case R.id.cancelBtn:
                alarm.cancel(alarmIntent);
                Toast.makeText(this, "Canceled !", Toast.LENGTH_SHORT).show();
                break;

        }



    }
}
