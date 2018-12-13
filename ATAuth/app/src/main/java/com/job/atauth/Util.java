package com.job.atauth;

/**
 * Created by Job on Thursday : 12/13/2018.
 */
public class Util {

    public static String toMinutes(long millisUntilFinished){
        long min =  (millisUntilFinished) / (1000 * 60);
        return String.valueOf(min);
    }

    public static String toSec(long millisUntilFinished){
        long remainedSecs = millisUntilFinished / 1000;
        return String.valueOf((remainedSecs % 60));
    }
}
