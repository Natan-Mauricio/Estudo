/*
83. Crie uma lógica que preencha um vetor de 20 posições
com números aleatórios (entre 0 e 99) gerados pelo computador.
Logo em seguida, mostre os números gerados e depois coloque o
vetor em ordem crescente, mostrando no final os valores ordenados.

Algoritmo:
1. Criar um objeto 'Random' para gerar números aleatórios.
2. Criar um vetor de tamanho 20 para armazenar 20 números aleatórios.
3. Preencher o vetor com números aleatórios entre 0 e 99 usando um loop 'for'.
4. Exibir o vetor original, imprimindo seus valores na tela, separados por " | ".
5. Chamar o metodo 'ordenar(vetor)' para ordenar o vetor em ordem crescente:
   - O metodo de ordenação utiliza o algoritmo de ordenação por troca (Bubble Sort).
   - Iterar sobre o vetor e, a cada comparação de dois elementos, trocar seus valores se o elemento da posição
   anterior for maior que o da posição seguinte.
6. Após a ordenação, imprimir o vetor ordenado da mesma forma que o vetor original, separado por " | ".
 */
import java.util.Random;

public class Desafio9 {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] vetor = new int[20];

        for (int i = 0; i < 20; i++) {
            vetor[i] = rand.nextInt(100);
        }

        System.out.print("Vetor Original:| ");
        for (int i = 0; i < 20; i++) {
            System.out.print(vetor[i] + " | ");
        }

        vetor = ordenar(vetor);
        System.out.println();

        System.out.print("Vetor Ordenado:| ");
        for (int i = 0; i < 20; i++) {
            System.out.print(vetor[i] + " | ");
        }
    }

    public static int[] ordenar(int[] v) {
        for (int i = 0; i < 20; i++) {
            for (int j = i + 1; j < 20; j++) {
                if (v[i] > v[j]) {
                    int x = v[i];
                    v[i] = v[j];
                    v[j] = x;
                }
            }
        }
        return v;
    }
}