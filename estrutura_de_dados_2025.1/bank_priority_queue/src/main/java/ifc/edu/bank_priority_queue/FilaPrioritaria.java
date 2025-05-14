package ifc.edu.bank_priority_queue;

/**
 * Estrutura de dados para gerenciar uma fila de atendimento prioritário.
 */
public class FilaPrioritaria {
    private Cliente inicio;

    public boolean estaVazia() {
        return inicio == null;
    }

    public void inserirCliente(String nome, int idade) {
        if (idade < 60) {
            System.out.println("Cliente não é prioritário (idade < 60). Não será adicionado à fila.");
            return;
        }

        Cliente novoCliente = new Cliente(nome, idade);

        if (inicio == null || idade > inicio.idade) {
            novoCliente.proximo = inicio;
            inicio = novoCliente;
        } else {
            Cliente atual = inicio;
            while (atual.proximo != null && atual.proximo.idade >= idade) {
                atual = atual.proximo;
            }
            novoCliente.proximo = atual.proximo;
            atual.proximo = novoCliente;
        }

        System.out.println("Cliente adicionado com sucesso!");
    }

    public void atenderCliente() {
        if (estaVazia()) {
            System.out.println("Fila vazia. Nenhum cliente para atender.");
            return;
        }

        Cliente atendido = inicio;
        inicio = inicio.proximo;

        System.out.printf("Atendendo cliente: %s (Idade: %d)%n", atendido.nome, atendido.idade);
    }

    public void exibirClienteFrente() {
        if (estaVazia()) {
            System.out.println("Fila vazia.");
            return;
        }

        System.out.printf("Cliente da frente: %s (Idade: %d)%n", inicio.nome, inicio.idade);
    }

    public void exibirTodosClientes() {
        if (estaVazia()) {
            System.out.println("Fila vazia.");
            return;
        }

        System.out.println("=== Fila de Atendimento Prioritário ===");
        Cliente atual = inicio;

        while (atual != null) {
            System.out.printf("Nome: %s | Idade: %d%n", atual.nome, atual.idade);
            atual = atual.proximo;
        }
    }
}
