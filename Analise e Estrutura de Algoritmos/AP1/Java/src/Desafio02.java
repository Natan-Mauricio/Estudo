/*
25. Crie um programa que leia o tamanho de três segmentos
de reta. Analise seus comprimentos e diga se é possível formar um
triângulo com essas retas. Matematicamente, para três segmentos
formarem um triângulo, o comprimento de cada lado deve ser menor
que a soma dos outros dois.

Algoritmo:
1. Exibir uma janela de input solicitando o valor do primeiro segmento.
2. Ler e armazenar o valor do primeiro segmento como um número inteiro.
3. Exibir uma janela de input solicitando o valor do segundo segmento.
4. Ler e armazenar o valor do segundo segmento como um número inteiro.
5. Exibir uma janela de input solicitando o valor do terceiro segmento.
6. Ler e armazenar o valor do terceiro segmento como um número inteiro.
7. Verificar se os três segmentos podem formar um triângulo, aplicando a condição:
   - O primeiro segmento deve ser menor que a soma dos outros dois.
   - O segundo segmento deve ser menor que a soma dos outros dois.
   - O terceiro segmento deve ser menor que a soma dos outros dois.
8. Se os segmentos formarem um triângulo, exibir a mensagem "Os segmentos formam um triângulo!".
9. Caso contrário, exibir a mensagem "Os segmentos não formam um triângulo!".
 */
import javax.swing.JOptionPane;

public class Desafio02 {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Segmento 1: ");
        int seg1 = Integer.parseInt(entrada);
        entrada = JOptionPane.showInputDialog("Segmento 2: ");
        int seg2 = Integer.parseInt(entrada);
        entrada = JOptionPane.showInputDialog("Segmento 3: ");
        int seg3 = Integer.parseInt(entrada);

        if (seg1 < seg2 + seg3 && seg2 < seg1 + seg3 && seg3 < seg1 + seg2) {
            JOptionPane.showMessageDialog(null, "Os segmentos formam um triângulo!");
        }
        else {
            JOptionPane.showMessageDialog(null, "Os segmentos não formam um triângulo!");
        }
    }
}
