import java.util.Scanner;

public class LinearFibonacci {
    public static int fibonacci(int k) {
        if (k <= 1) return k;

        int anterior = 0;
        int atual = 1;

        for (int i = 2; i <= k; i++) {
            int proximo = anterior + atual;
            anterior = atual;
            atual = proximo;
        }

        return atual;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite o k-ésimo termo de Fibonacci a ser retornado: ");
        int k = scan.nextInt();
        int resultado = fibonacci(k);

        System.out.print("O " + k + "º elemento da sequência de Fibonacci é: " + resultado);
    }
}
