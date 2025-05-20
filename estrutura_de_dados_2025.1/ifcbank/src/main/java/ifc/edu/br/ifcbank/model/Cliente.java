package ifc.edu.br.ifcbank.model;

public class Cliente {
    private final String nome;
    private final int idade;
    private Cliente proximo;

    public Cliente(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        this.proximo = null;
    }

    public String getNome() { return nome; }
    public int getIdade() { return idade; }
    public Cliente getProximo() { return proximo; }
    public void setProximo(Cliente proximo) { this.proximo = proximo; }
}
