package com.mycompany.mavenproject1;
import java.util.Scanner;

class Mavenproject1 {

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        boolean quit = false;
        int option;
        int temp;
        float temperature;
        int number;
        int number0;
        int number1;
        int number2;
        while(!quit) {
            System.out.println("==== MENU ====");
            System.out.println("0. Quit");
            System.out.println("1. Convert Celsius to Fahrenheit");
            System.out.println("2. Convert Fahrenheit to Celsius");
            System.out.println("3. Check if a number is odd or even");
            System.out.println("4. Put 3 numbers in ascending order");
            System.out.print("\nEnter the desired option: ");
            option = keyboard.nextInt();
            System.out.println();
       
            switch(option) {
                case 0:
                    quit = true;
                    break;
                case 1: 
                    System.out.println("Insert Celsius Temperature: ");
                    temperature = keyboard.nextFloat();
                    temperature = (temperature * 9 + 160)/5;
                    System.out.println("In Fahrenheit: " + String.format("%.2f", temperature));
                    break;
                case 2:
                    System.out.println("Insert Fahrenheit Temperature: ");
                    temperature = keyboard.nextFloat();
                    temperature = (temperature -32)* 5/9;
                    System.out.println("In Celcius: " + String.format("%.2f", temperature));
                    break;
                case 3:
                    System.out.println("Insert the number: ");
                    number = keyboard.nextInt();
                    if (number % 2 == 0) {
                        System.out.println(number + " Is Even");
                    } else {
                        System.out.println(number + " Is Odd");
                    }
                    break;
                case 4:
                    System.out.println("Insert three numbers, one by one: "); /// Not able to use arrays.
                    number0 = keyboard.nextInt();
                    number1 = keyboard.nextInt();
                    number2 = keyboard.nextInt();
                
                    if(number0 > number1){
                      temp = number1;
                      number1 = number0;
                      number0 = temp;                          
                    }
                    if(number1 > number2){
                        temp = number1;
                        number1 = number2;
                        number2 = temp;
                    }
                    if(number0 > number1){
                      temp = number1;
                      number1 = number0;
                      number0 = temp;                          
                    }
                    System.out.println(number0 + "<" + number1 + "<" + number2);
                    break;
                default:
                    System.out.println("Invalid Option");
            }           
        }
    }
}