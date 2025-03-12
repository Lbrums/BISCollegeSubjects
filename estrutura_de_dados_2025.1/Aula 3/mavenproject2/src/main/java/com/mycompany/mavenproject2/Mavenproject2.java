package com.mycompany.mavenproject2;
import java.util.Scanner;

public class Mavenproject2 {
    
    static int soma(int a, int b){
        int resp = 0;
        for(int i = a; i<=b; i++){
            resp = i + resp;
        }
        return resp;
    }
    
    
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Você irá receber a soma dos numeros entre o intervalo do valor 1 e valor 2.");
        System.out.println("Insira o primeiro valor: ");
        int value_a = keyboard.nextInt();
        System.out.println("Insira o segundo valor: ");
        int value_b = keyboard.nextInt();
        int result = soma(value_a, value_b);
        System.out.println(result);
    }
}
