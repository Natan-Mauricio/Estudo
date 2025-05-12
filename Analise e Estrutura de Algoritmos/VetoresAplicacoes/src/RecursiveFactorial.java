import java.util.ArrayList;
import java.util.Scanner;

public class RecursiveFactorial {
    private static ArrayList<Integer> resultados = new ArrayList<>();

    public static Integer calcularFatorial(int n) {
        //Evitar erro de recursividade infinita
        if (n < 0) {
            throw new IllegalArgumentException("O número não pode ser negativo");
        }

        if (n == 0 || n == 1) {
            resultados.add(1);
            return 1;
        }

        Integer resultado = n * calcularFatorial(n - 1);
        resultados.add(resultado);
        return resultado;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite um número inteiro para calcular o fatorial: ");
        int numero = scan.nextInt();

        calcularFatorial(numero);

        System.out.print("Resultados: 1");
        for (int i = 0; i < resultados.size(); i++) {
            System.out.print(" * " + (i + 1) + " = " + resultados.get(i));
        }
    }
}
