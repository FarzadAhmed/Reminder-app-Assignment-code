package com.example.a225try5;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class AlarmReceiever extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {

        int ntId = intent.getIntExtra("notificationId",0);
        String msg = intent.getStringExtra("ToDo");

        Intent mIntent = new Intent(context,MainActivity.class);
        PendingIntent cIntent = PendingIntent.getActivity(context,0,mIntent,0);

        NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);


        Notification.Builder builder = new Notification.Builder(context);
        builder.setSmallIcon(android.R.drawable.ic_dialog_info)
                .setContentTitle("Your Friendly Reminder !")
                .setContentText(msg)
                .setWhen(System.currentTimeMillis())
                .setAutoCancel(true)
                .setContentIntent(cIntent);

        notificationManager.notify(ntId, builder.build());



    }
}
