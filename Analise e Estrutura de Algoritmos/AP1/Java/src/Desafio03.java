/*
30. Refaça o algoritmo 25, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
• EQUILÁTERO: todos os lados iguais
• ISÓSCELES: dois lados iguais
• ESCALENO: todos os lados diferentes

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
8. Se os segmentos formarem um triângulo, chamar a função 'tipo()' para determinar o tipo de triângulo:
   - Se os três segmentos forem iguais, retornar "equilátero".
   - Se dois segmentos forem iguais, retornar "isósceles".
   - Caso contrário, retornar "escaleno".
9. Exibir uma mensagem informando o tipo do triângulo formado (equilátero, isósceles ou escaleno).
10. Se os segmentos não formarem um triângulo, exibir a mensagem "Os segmentos não formam um triângulo!".
 */
import javax.swing.JOptionPane;

public class Desafio03 {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Segmento 1: ");
        int seg1 = Integer.parseInt(entrada);
        entrada = JOptionPane.showInputDialog("Segmento 2: ");
        int seg2 = Integer.parseInt(entrada);
        entrada = JOptionPane.showInputDialog("Segmento 3: ");
        int seg3 = Integer.parseInt(entrada);

        if (seg1 < seg2 + seg3 && seg2 < seg1 + seg3 && seg3 < seg1 + seg2) {
            String nome = tipo(seg1, seg2, seg3);
            JOptionPane.showMessageDialog(null, "Os segmentos formam um triângulo "+ nome +"!");
        }
        else {
            JOptionPane.showMessageDialog(null, "Os segmentos não formam um triângulo!");
        }
    }

    public static String tipo(int s1, int s2, int s3) {
        if (s1 == s2 && s2 == s3) {
            return "equilátero";
        }
        else if (s1 == s2 || s2 == s3 || s1 == s3) {
            return "isósceles";
        }
        else {
            return "escaleno";
        }
    }
}
