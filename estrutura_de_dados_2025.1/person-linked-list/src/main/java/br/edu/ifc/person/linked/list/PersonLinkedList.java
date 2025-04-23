/*
 * Autor:  Luciano Brum Silva
 * Curso:  Sistemas de Informação – IFC Campus Camboriú
 * Data:   23 abr 2025
 * Descrição: Implementa lista encadeada de pessoas com inserção, busca e exibição.
 */

package br.edu.ifc.person.linked.list;

import java.util.Optional;

class NodePerson {

    /* ---------- Campos ---------- */
    final String ssn;
    final String name;
    final double earnings;
    NodePerson next;

    /* ---------- Construtor ---------- */
    NodePerson(String ssn, String name, double earnings) {
        this.ssn      = ssn;
        this.name     = name;
        this.earnings = earnings;
    }
}

public class PersonLinkedList {

    /* ---------- Ponteiros da lista ---------- */
    private NodePerson head;
    private NodePerson tail;

    /* ---------- Inserção no início ---------- */
    public void addFirst(String ssn, String name, double earnings) {
        NodePerson node = new NodePerson(ssn, name, earnings);
        node.next = head;
        head = node;
        if (tail == null) tail = node;
    }

    /* ---------- Inserção no final ---------- */
    public void addLast(String ssn, String name, double earnings) {
        NodePerson node = new NodePerson(ssn, name, earnings);
        if (head == null) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
    }

    /* ---------- Busca por nome (case‑insensitive) ---------- */
    public Optional<NodePerson> findByName(String target) {
        for (NodePerson p = head; p != null; p = p.next)
            if (p.name.equalsIgnoreCase(target))
                return Optional.of(p);
        return Optional.empty();
    }

    /* ---------- Exibe toda a lista ---------- */
    public void print() {
        for (NodePerson p = head; p != null; p = p.next)
            System.out.printf("%-6s %-10s R$ %.2f%n",
                              p.ssn, p.name, p.earnings);
    }

    /* ---------- Demonstração rápida ---------- */
    public static void main(String[] args) {

        PersonLinkedList list = new PersonLinkedList();

        /* Inserções */
        for (int i = 0; i < 3; i++)
            list.addFirst("CPF" + i, "Inicio" + i, i * 1000);

        for (int i = 3; i < 6; i++)
            list.addLast("CPF" + i, "Final" + i, i * 1000);

        /* Impressão */
        System.out.println("=== Conteúdo da lista ===");
        list.print();

        /* Busca */
        String key = "Final4";
        list.findByName(key).ifPresentOrElse(
            p -> System.out.printf("%nEncontrado: %s  %s  R$ %.2f%n",
                                   p.ssn, p.name, p.earnings),
            () -> System.out.printf("%nNome \"%s\" não encontrado.%n", key)
        );
    }
}
