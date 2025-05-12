import java.util.Scanner;

public class LinearSum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite o tamanho dos vetores: ");
        int tam = scan.nextInt();

        int[] vetor1 = new int[tam];
        int[] vetor2 = new int[tam];

        System.out.println("\nDigite os valores do vetor 1:");
        for (int i = 0; i < tam; i++) {
            System.out.print("[" + i + "]: ");
            vetor1[i] = scan.nextInt();
        }

        System.out.println("\nDigite os valores do vetor 2:");
        for (int i = 0; i < tam; i++) {
            System.out.print("[" + i + "]: ");
            vetor2[i] = scan.nextInt();
        }

        System.out.print("\nSoma Linear: [");
        for (int i = 0; i < tam; i++) {
            System.out.print(vetor1[i]);
            if (i < tam - 1) {
                System.out.print(", ");
            }
        }

        System.out.print("] + [");
        for (int i = 0; i < tam; i++) {
            System.out.print(vetor2[i]);
            if (i < tam - 1) {
                System.out.print(", ");
            }
        }

        System.out.print("] = [");
        for (int i = 0; i < tam; i++) {
            System.out.print(vetor1[i] + vetor2[i]);
            if (i < tam - 1) {
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }
}
