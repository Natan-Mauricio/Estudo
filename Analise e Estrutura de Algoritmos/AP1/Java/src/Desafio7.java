/*
69. Desenvolva um programa que leia o primeiro termo e a
razão de uma PA (Progressão Aritmética), mostrando na tela os 10
primeiros elementos da PA e a soma entre todos os valores da
sequência.

Algoritmo:
1. Inicializar as variáveis 'termo', 'razao', 'limite' e 'total' como 0.
2. Iniciar um loop para solicitar ao usuário os valores do primeiro termo e da razão da progressão aritmética (PA).
3. Exibir uma janela de input solicitando o valor do primeiro termo e da razão.
4. Validar a entrada do usuário para garantir que ambos os valores sejam inteiros. Caso a entrada seja inválida,
exibir uma mensagem de erro e solicitar novamente.
5. Após as entradas válidas, exibir uma mensagem com a razão da PA e o primeiro termo.
6. Usar um loop para gerar os primeiros 10 termos da progressão aritmética, somando a razão ao valor anterior a
cada iteração:
   - Inicializar a variável 'i' com o primeiro termo.
   - Adicionar a razão ao valor de 'i' a cada iteração.
   - Imprimir cada termo da PA.
   - Contabilizar a soma dos termos no total.
7. Após gerar os 10 primeiros termos, exibir a soma dos termos calculada.
 */
import javax.swing.JOptionPane;

public class Desafio7 {
    public static void main(String[] args) {
        int termo = 0;
        int razao = 0;
        int limite = 0;
        int total = 0;

        while(true){
            String entrada1 = JOptionPane.showInputDialog(null,
                    "Primeiro Termo:", "Progressão Aritmética", JOptionPane.QUESTION_MESSAGE);;
            String entrada2 = JOptionPane.showInputDialog(null,
                    "Razão da PA:", "Progressão Aritmética", JOptionPane.QUESTION_MESSAGE);

            try {
                termo = Integer.parseInt(entrada1);
                razao = Integer.parseInt(entrada2);
                break;
            }
            catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Escolha Inválida! Tente Novamente...");
            }
        }
        System.out.print("Progressão Aritmética (10 Primeiros Termos)\nRazão: "+ razao +"\nPrimeiro Termo: "+ termo +"\nResultado:");

        for(int i = termo; limite < 10; i += razao) {
            System.out.print(" > "+ i);
            total += i;
            limite += 1;
        }

        System.out.println("\nSoma dos Termos: "+total);

    }
}