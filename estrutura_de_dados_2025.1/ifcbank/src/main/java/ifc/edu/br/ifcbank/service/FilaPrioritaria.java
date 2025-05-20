package ifc.edu.br.ifcbank.service;

import ifc.edu.br.ifcbank.model.Cliente;

public class FilaPrioritaria {
    private Cliente inicio;

    public FilaPrioritaria() {
        this.inicio = null;
    }

    public boolean estaVazia() {
        return inicio == null;
    }

    public void inserirOrdenado(String nome, int idade) {
        if (idade < 60) {
            System.out.println("Somente clientes com 60 anos ou mais podem entrar na fila prioritária.");
            return;
        }

        Cliente novo = new Cliente(nome, idade);

        if (inicio == null || idade > inicio.getIdade()) {
            novo.setProximo(inicio);
            inicio = novo;
        } else {
            Cliente atual = inicio;
            while (atual.getProximo() != null &&
                    atual.getProximo().getIdade() >= idade) {
                atual = atual.getProximo();
            }
            novo.setProximo(atual.getProximo());
            atual.setProximo(novo);
        }
        System.out.println("Cliente adicionado com sucesso.");
    }

    public void atender() {
        if (estaVazia()) {
            System.out.println("Fila vazia.");
            return;
        }
        Cliente atendido = inicio;
        inicio = inicio.getProximo();
        System.out.printf("Atendendo: %s, %d anos%n", atendido.getNome(), atendido.getIdade());
    }

    public void exibirFrente() {
        if (estaVazia()) {
            System.out.println("Fila vazia.");
            return;
        }
        System.out.printf("Frente da fila: %s, %d anos%n", inicio.getNome(), inicio.getIdade());
    }

    public void exibirFila() {
        if (estaVazia()) {
            System.out.println("Fila vazia.");
            return;
        }

        Cliente atual = inicio;
        System.out.println("Fila de atendimento:");
        while (atual != null) {
            System.out.printf("- %s, %d anos%n", atual.getNome(), atual.getIdade());
            atual = atual.getProximo();
        }
    }
}
