import java.util.Scanner;

public class Regua {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int[] vetor = OperacoesVetores.gerarVetor();
        int inicio = 0, fim = 0;

        while (true) {
            System.out.print("Digite o índice de início do vetor (0 a 8): ");
            inicio = scan.nextInt();
            System.out.print("Digite o índice de fim do vetor (1 a 9): ");
            fim = scan.nextInt();
            if (inicio < fim && inicio >= 0 && inicio <= 8 && fim <= 9) {break;}
            System.out.println("\nErro! Tente novamente...\n");
        }

        System.out.print("\nVetor Original: [");
        OperacoesVetores.exibirVetor(vetor);

        System.out.print("Vetor Recortado: [");
        for (int i = inicio; i <= fim; i++) {
            System.out.printf("%d", vetor[i]);
            if(i != fim) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
