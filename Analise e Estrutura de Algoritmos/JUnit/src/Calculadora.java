/*
Nome: Natan Maurício da Silva
RA: 2401712
Turma: CC 3A MANHÃ
 */

public class Calculadora {
    public static Double soma(double a, double b) {
        return a + b;
    }

    public static Double subtracao(double a, double b) {
        return a - b;
    }

    public static Double multiplicacao(double a, double b) {
        return a * b;
    }

    public static Double potenciacao(double a, double b) {
        if (a == 0 && b <= 0) {
            throw new ArithmeticException("Indeterminação matemática: 0^0 ou 0^-b");
        }

        if (b < 0) {
            return 1 / potenciacao(a, -b);
        }

        double resultado = 1;
        for (int i = 0; i < b; i++) {
            resultado *= a;
        }
        return resultado;
    }
}