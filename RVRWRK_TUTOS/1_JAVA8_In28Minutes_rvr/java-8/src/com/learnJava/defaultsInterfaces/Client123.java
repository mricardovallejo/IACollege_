package com.learnJava.defaults;

public class Client123 implements Interface1,Interface2,Interface3 {


    public void methodA(){

        System.out.println("Inside Method A" + Client123.class);
    }
//Metodo que toma es del mas hijo que encuentre hacia arriba
    // 1 -> class the implements the interface, metod A en clase123 es el q prima
    // 2 -> the sub interface that extends the interface.


    public static void main(String[] args) {

        Client123 client123 = new Client123();
        client123.methodA(); //resolve to the child implementation
        client123.methodB();
        client123.methodC();
    }
}
