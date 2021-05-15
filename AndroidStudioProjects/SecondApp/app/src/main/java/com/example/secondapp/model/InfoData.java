package com.example.secondapp.model;

import java.util.function.LongToIntFunction;

public class InfoData {

    protected String userName;
    protected Long cc;
    protected Long form_Number;

    public Long getCc() {
        return cc;
    }

    public void setCc(Long cc) {
        this.cc = cc;
    }

    public Long getForm_Number() {
        return form_Number;
    }

    public void setForm_Number(Long form_Number) {
        this.form_Number = form_Number;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }
}
