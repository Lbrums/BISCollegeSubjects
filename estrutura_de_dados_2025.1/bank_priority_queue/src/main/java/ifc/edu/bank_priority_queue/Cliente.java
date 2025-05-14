package ifc.edu.bank_priority_queue;

/**
 * Representa um cliente da fila prioritária.
 */
public class Cliente {
    String nome;
    int idade;
    Cliente proximo;

    public Cliente(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        this.proximo = null;
    }
}
