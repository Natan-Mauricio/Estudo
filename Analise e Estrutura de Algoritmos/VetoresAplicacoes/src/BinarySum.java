import java.util.Scanner;

public class BinarySum {
    public static int [] mesmoTamanho(int [] v, int tam) {
        int [] novoVetor = new int[tam];

        for (int i = 0; i <v.length ; i++) {
            novoVetor[novoVetor.length - 1 - i] = v[v.length - 1 - i];
        }

        return novoVetor;
    }

    public static int [] somaBinaria(int [] v1, int [] v2) {
        if (v1.length != v2.length) {
            if (v1.length > v2.length) {
                v2 = mesmoTamanho(v2, v1.length);
            }
            else {
                v1 = mesmoTamanho(v1, v2.length);
            }
        }

        int [] resultado = new int[v1.length + 1];
        int sobeUm = 0;

        for (int i = v1.length - 1; i >= 0; i--) {
            int soma = v1[i] + v2[i] + sobeUm;
            resultado[i + 1] = soma % 2;
            sobeUm = soma / 2;
        }

        if (sobeUm == 1) {
            resultado[0] = 1;
            return resultado;
        }
        else {
            int [] resultado2 = new int[resultado.length - 1];
            for (int i = 0; i < resultado2.length; i++) {
                resultado2[i] = resultado[i + 1];
            }
            return resultado2;
        }
    }

    public static int [] converterString(String string) {
        int [] binario = new int[string.length()];

        for (int i = 0; i < string.length(); i++) {
            binario[i] = string.charAt(i) - '0';
        }

        return binario;
    }

    public static boolean eBinario(String string) {
        for (int i = 0; i < string.length(); i++) {
            char caractere = string.charAt(i);
            if (caractere != '0' && caractere != '1') {
                return false;
            }
        }
        return true;
    }

    public static int [] entrada(String frase) {
        Scanner scan = new Scanner(System.in);
        String entrada;
        int [] binario;

        while (true){
            System.out.print(frase);
            entrada = scan.nextLine();
            if (eBinario(entrada)) {
                binario = converterString(entrada);
                break;
            }
            System.out.println("Erro! O número não é binário...");
        }

        return binario;
    }

    public static void main(String[] args) {
        int [] binario1 = entrada("Digite um número binário: ");
        int [] binario2 = entrada("Digite outro número binário: ");
        int [] soma = somaBinaria(binario1, binario2);

        System.out.print("Soma = ");
        for (int i = 0; i < soma.length; i++) {
            System.out.print(soma[i] + " ");
        }
    }
}
