public class IterativeReverseArray {
    public static void main(String[] args) {
        int [] vetor = OperacoesVetores.gerarVetor();
        int [] vetorReverso = new int[vetor.length];

        for (int i = 0; i < vetor.length; i++) {
            vetorReverso[i] = vetor[vetor.length - 1 - i];
        }

        System.out.print("\nVetor Original: [");
        OperacoesVetores.exibirVetor(vetor);

        System.out.print("Vetor Reverso: [");
        OperacoesVetores.exibirVetor(vetorReverso);
    }
}
