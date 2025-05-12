import java.util.Random;

public class OperacoesVetores {
    public static int[] gerarVetor() {
        Random random = new Random();
        int[] vetor = new int[10];

        for (int i = 0; i < 10; i++) {
            vetor[i] = random.nextInt(100);
        }

        return vetor;
    }

    public static void exibirVetor(int [] vetor) {
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf("%d", vetor[i]);
            if(i < vetor.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
