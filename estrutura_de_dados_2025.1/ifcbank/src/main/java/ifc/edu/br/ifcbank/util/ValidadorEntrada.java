package ifc.edu.br.ifcbank.util;

import java.util.Scanner;

public class ValidadorEntrada {
    private static final Scanner scanner = new Scanner(System.in);

    public static int lerInteiro() {
        while (true) {
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida. Digite um número inteiro.");
            }
        }
    }

    public static String lerLinha() {
        return scanner.nextLine().trim();
    }
}