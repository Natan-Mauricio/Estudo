import java.util.Scanner;

public class BinaryFib {
    public static String binaryFib(int k) {
        return Integer.toBinaryString(LinearFibonacci.fibonacci(k));
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite o k-ésimo termo de Fibonacci a ser retornado em binário: ");
        int k = scan.nextInt();
        String resultado = binaryFib(k);

        System.out.print("O " + k + "º elemento da sequência de Fibonacci é: " + resultado);
    }
}