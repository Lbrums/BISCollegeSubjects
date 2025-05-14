package ifc.edu.bank_priority_queue;

import java.util.Scanner;

/**
 * Classe principal com interface de console para o sistema de fila prioritária.
 */
public class BankPriorityQueue {
    private static final Scanner scanner = new Scanner(System.in);
    private static final FilaPrioritaria fila = new FilaPrioritaria();

    public static void main(String[] args) {
        int opcao;

        do {
            exibirMenu();
            opcao = lerOpcaoUsuario();
            executarAcao(opcao);
        } while (opcao != 0);

        System.out.println("Sistema encerrado.");
    }

    private static void exibirMenu() {
        System.out.println("\n=== IFCBank - Sistema de Gerenciamento de Fila Prioritária ===");
        System.out.println("1. Adicionar cliente prioritário");
        System.out.println("2. Atender próximo cliente");
        System.out.println("3. Exibir cliente da frente");
        System.out.println("4. Exibir toda a fila");
        System.out.println("5. Verificar se a fila está vazia");
        System.out.println("0. Sair");
        System.out.print("Escolha uma opção: ");
    }

    private static int lerOpcaoUsuario() {
        while (!scanner.hasNextInt()) {
            System.out.print("Opção inválida. Digite novamente: ");
            scanner.next();
        }
        int opcao = scanner.nextInt();
        scanner.nextLine(); // Limpa o buffer
        return opcao;
    }

    private static void executarAcao(int opcao) {
        switch (opcao) {
            case 1 -> adicionarCliente();
            case 2 -> fila.atenderCliente();
            case 3 -> fila.exibirClienteFrente();
            case 4 -> fila.exibirTodosClientes();
            case 5 -> System.out.println(fila.estaVazia() ? "A fila está vazia." : "A fila contém clientes.");
            case 0 -> {}
            default -> System.out.println("Opção inválida.");
        }
    }

    private static void adicionarCliente() {
        System.out.print("Nome do cliente: ");
        String nome = scanner.nextLine();

        System.out.print("Idade do cliente: ");
        while (!scanner.hasNextInt()) {
            System.out.print("Idade inválida. Digite novamente: ");
            scanner.next();
        }
        int idade = scanner.nextInt();
        scanner.nextLine(); // Limpa o buffer

        fila.inserirCliente(nome, idade);
    }
}
