package com.mycompany.mavenproject3;
import java.util.Scanner;

public class Mavenproject3 {
    static String name_abbreviate(String name){
        String[] parts = name.split(" ");
        StringBuilder abbreviation = new StringBuilder();
        
        abbreviation.append(parts[0]);
        
        for (int i =1; i < parts.length - 1; i++){
            abbreviation.append(" ").append(parts[i].charAt(0)).append(".");
            }
        if (parts.length > 1){
            abbreviation.append(" ").append(parts[parts.length - 1]);
        }
        
        return abbreviation.toString();
    }
    
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Por favor, insira o seu nome: ");
        String fullName = keyboard.nextLine();
        String abreviatedName = name_abbreviate(fullName);
        System.out.println("Nome abreviado: " + abreviatedName);
    }
}
