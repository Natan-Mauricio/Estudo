/*
16. Escreva um programa para calcular a redução do tempo
de vida de um fumante. Pergunte a quantidade de cigarros fumados
por dias e quantos anos ele já fumou. Considere que um fumante
perde 10 min de vida a cada cigarro. Calcule quantos dias de vida
um fumante perderá e exiba o total em dias.

Algoritmo:
1. Exibir uma janela de input solicitando a quantidade de cigarros fumados por dia.
2. Ler e armazenar a quantidade de cigarros fumados por dia como um número inteiro.
3. Exibir uma janela de input solicitando o número de anos que a pessoa fuma.
4. Ler e armazenar o número de anos fumando como um número inteiro.
5. Calcular a quantidade total de dias perdidos de vida, considerando que cada cigarro fumado diminui
a vida em 10 minutos.
6. Exibir uma janela de mensagem com o total de dias perdidos de vida.
 */
import javax.swing.JOptionPane;

public class Desafio1 {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Cigarros fumados por dia: ");
        int qtd = Integer.parseInt(entrada);

        entrada = JOptionPane.showInputDialog("Anos de fumante: ");
        int anos = Integer.parseInt(entrada);

        int total = (anos * 365 * qtd * 10) / 1440;
        JOptionPane.showMessageDialog(null, "Você perdeu " + total +" dias de vida");
    }
}
