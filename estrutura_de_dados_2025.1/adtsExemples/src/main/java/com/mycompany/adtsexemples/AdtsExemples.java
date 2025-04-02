package com.mycompany.adtsexemples;
import java.util.ArrayList;
import java.nio.charset.StandardCharsets;
import java.io.PrintStream;

public class AdtsExemples{
    public static void main(String[] args1) {
        try {
            System.setOut(new PrintStream(System.out, true, StandardCharsets.UTF_8.name()));
        } catch (Exception e) {
            e.printStackTrace();
        }
        ArrayList<Alunos> alunos = new ArrayList<>();
        alunos.add(new Alunos("Carlos", 8.5f));
        alunos.add(new Alunos("Ana", 6.0f));
        alunos.add(new Alunos("João", 9.2f));
        alunos.add(new Alunos("Pedro", 5.5f));

        Alunos.exibirTodos(alunos);
        Alunos.emExame(alunos);
    }
}
class Alunos {
        private final String nome;
        private float media;
        public Alunos(String nome, float media) {
            this.nome = nome;
            this.media = media;
        }
        public void exibirInfo() {
            System.out.println("Nome: " + nome);
            System.out.printf("Média: %.1f\n", media);
        }
        public static void exibirTodos(ArrayList<Alunos> alunos ) {
            for (Alunos aluno : alunos){
                aluno.exibirInfo();
            }
        }
        public static void emExame (ArrayList<Alunos> alunos) {
            for (Alunos aluno : alunos){
                if(aluno.media < 7){
                    aluno.exibirInfo();
                }
            }
        }
}