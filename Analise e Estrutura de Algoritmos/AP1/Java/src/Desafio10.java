/*
94. Desenvolva um aplicativo que tenha um procedimento
chamado Fibonacci() que recebe um único valor inteiro como
parâmetro, indicando quantos termos da sequência serão mostrados
na tela. O seu procedimento deve receber esse valor e mostrar a
quantidade de elementos solicitados.

Algoritmo:
1. Solicitar ao usuário o número de termos que ele deseja na sequência de Fibonacci. O valor é armazenado
na variável 'termos'.
2. Chamar o metodo 'fibonacci(termos)' para gerar e exibir a sequência de Fibonacci com a quantidade de termos
fornecida pelo usuário.
3. Dentro do metodo 'fibonacci':
   - Inicializar as variáveis 'a' e 'b' para os primeiros dois termos da sequência (1 e 0, respectivamente).
   - Criar uma variável 'exibir' para armazenar os termos da sequência que serão exibidos.
   - Utilizar um loop 'for' para calcular e armazenar os termos da sequência de Fibonacci:
     - Se o índice atual for o último termo (igual a 'qtd'), adicionar o termo final seguido de " >> FIM".
     - Caso contrário, adicionar o termo atual seguido de " >> ".
     - Atualizar as variáveis 'a' e 'b' para gerar o próximo termo da sequência.
4. Exibir os termos gerados da sequência de Fibonacci, com a mensagem formatada para mostrar
o número de termos e a sequência calculada.
 */
import javax.swing.JOptionPane;

public class Desafio10 {
    public static void main(String[] args) {
        int termos = Integer.parseInt(JOptionPane.showInputDialog(null,
                "Quantidade de Termos: ", "Fibonacci", JOptionPane.QUESTION_MESSAGE));
        fibonacci(termos);
    }

    public static void fibonacci(int qtd) {
        int a = 1;
        int b = 0;
        int c;
        String exibir = "";

        for (int i = 1; i <= qtd; i++) {
            if (i == qtd) {
                exibir += a + " >> FIM";
            }
            else {
                exibir += a + " >> ";
                c = b;
                b = a;
                a += c;
            }
        }

        JOptionPane.showMessageDialog(null, exibir,
                "Fibonacci ("+ qtd +" Primeiros Termos)", JOptionPane.INFORMATION_MESSAGE);
    }
}