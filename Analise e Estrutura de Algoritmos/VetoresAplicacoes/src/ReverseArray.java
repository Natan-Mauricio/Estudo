public class ReverseArray {
    public static int[] inverterVetor(int[] original, int i, int[] reverso) {
        if (i == original.length) {
            return reverso;
        }

        reverso[i] = original[original.length - 1 - i];
        return inverterVetor(original, i + 1, reverso);
    }

    public static void main(String[] args) {
        int[] vetor = OperacoesVetores.gerarVetor();
        int[] vetorReverso = inverterVetor(vetor, 0, new int[vetor.length]);

        System.out.print("\nVetor Original: [");
        OperacoesVetores.exibirVetor(vetor);

        System.out.print("Vetor Reverso: [");
        OperacoesVetores.exibirVetor(vetorReverso);
    }
}