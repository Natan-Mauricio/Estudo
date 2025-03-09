/*
70. Faça um programa que mostre os 10 primeiros elementos
da Sequência de Fibonacci: 1 1 2 3 5 8 13 21...

Algoritmo:
1. Inicializar as variáveis 'a' como 1, 'b' como 0, e 'c' como uma variável auxiliar para calcular a sequência.
2. Exibir a mensagem "Sequência de Fibonacci (10 Primeiros Termos):" para o usuário.
3. Usar um loop para gerar os primeiros 10 termos da sequência de Fibonacci:
   - O loop começa com 'i = 1' até 'i = 10' (10 iterações).
   - A cada iteração, imprimir o valor de 'a' (o termo atual da sequência).
   - Armazenar o valor de 'b' na variável 'c' temporariamente.
   - Atribuir o valor de 'a' para 'b'.
   - Somar o valor de 'c' com o de 'a' para calcular o próximo termo da sequência.
4. Continuar o processo até que os 10 primeiros termos da sequência de Fibonacci sejam exibidos.
 */
public class Desafio8 {
    public static void main(String[] args) {
        int a = 1;
        int b = 0;
        int c;

        System.out.print("Sequência de Fibonacci (10 Primeiros Termos):| ");
        for (int i = 1; i <= 10; i++) {
            System.out.print(a + " | ");
            c = b;
            b = a;
            a += c;
        }
    }
}