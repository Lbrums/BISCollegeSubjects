package ifc.edu.br.ifcbank;


import ifc.edu.br.ifcbank.service.FilaPrioritaria;
import ifc.edu.br.ifcbank.util.ValidadorEntrada;

public class Main {
    public static void main(String[] args) {
        FilaPrioritaria fila = new FilaPrioritaria();
        int opcao;

        do {
            System.out.println("\n=== IFCBank – Sistema de Gerenciamento de Fila com prioridade ===");
            System.out.println("1. Adicionar cliente prioritário");
            System.out.println("2. Atender próximo cliente prioritário");
            System.out.println("3. Exibir informações do cliente da frente");
            System.out.println("4. Exibir toda a fila");
            System.out.println("5. Verificar se fila está vazia");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = ValidadorEntrada.lerInteiro();

            switch (opcao) {
                case 1 -> {
                    System.out.print("Nome completo: ");
                    String nome = ValidadorEntrada.lerLinha();
                    System.out.print("Idade: ");
                    int idade = ValidadorEntrada.lerInteiro();
                    fila.inserirOrdenado(nome, idade);
                }
                case 2 -> fila.atender();
                case 3 -> fila.exibirFrente();
                case 4 -> fila.exibirFila();
                case 5 -> System.out.println(fila.estaVazia() ? "Fila vazia." : "Fila possui clientes.");
                case 0 -> System.out.println("Encerrando o programa.");
                default -> System.out.println("Opção inválida.");
            }

        } while (opcao != 0);
    }
}
