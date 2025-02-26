package com.mycompany.mavenproject1;
import java.util.Scanner;

public class Mavenproject1 {
    
    public static int fibonacci(int n){
        if (n<=1){
            return n;
        }
        return fibonacci(n-1) + fibonacci(n-2);
    }
    
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        boolean quit = false;
        int option;
        int temp;
        int i = 0;
        
        while(!quit) {
            System.out.println("==== MENU ====");
            System.out.println("0. Quit");
            System.out.println("1. Tabuadas");
            System.out.println("2. Numeros elevados a 2 até o numero designado.");
            System.out.println("3. Sequencia de fibonnaci até o termo designado.");
            System.out.println("4. Fatorial.");
            System.out.println("5. Numero é primo?");
            System.out.print("\nEnter the desired option: ");
            option = keyboard.nextInt();
            System.out.println();
            
            switch(option) {
                case 0 -> quit = true;
                case 1 -> { 
                    System.out.println("Você deseja a tabuada de qual numero? ");
                    temp = keyboard.nextInt();
                    while(i<11) {
                            System.out.println(temp + "*" + i + "=" + temp * i);
                            i = i + 1;
                        }
                }
                case 2 -> {
                    System.out.print("Parar antes do numero: ");
                    temp = keyboard.nextInt();
                    i = 2;
                    while(i < temp){
                        System.out.println(i);
                        i = i * 2;
                    }
                }
                case 3 -> {
                    System.out.print("Parar antes do numero: ");
                    temp = keyboard.nextInt();
                    System.out.println("Sequencia de fibonacci até" + temp + " elementos: ");
                    for (i = 0; i < temp; i++) {
                        System.out.println(fibonacci(i)+"");
                    }
                }
                case 4 -> {
                    System.out.print("Fatorial do numero: ");
                    temp = keyboard.nextInt();
                    int result = 1;
                    for (i = 0; i < temp; i++){
                        result = result * (i +1);
                    }
                    System.out.println("Resultado: " + result);
                }
                case 5 -> {
                    System.out.print("Digite o numero para checar: ");
                    temp = keyboard.nextInt();
                    if (temp <= 1) {
                        System.out.println(temp + " Não é primo.");
                    } else {
                        boolean isPrimo = true;
                        for (i = 2; i <= Math.sqrt(temp); i++) {
                            if (temp % i == 0) {
                                System.out.println(temp + " Não é primo.");
                                isPrimo = false;
                                break;
                            }
                        }
                        if (isPrimo) {
                            System.out.println(temp + " É primo.");
                        }
                    }
}
                default -> System.out.println("Invalid Option");
            }
        }
    }
}
