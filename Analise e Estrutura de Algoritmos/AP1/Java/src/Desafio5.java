/*
32. Crie um jogo onde o computador vai sortear um número
entre 1 e 5 o jogador vai tentar descobrir qual foi o valor
sorteado.

Algoritmo:
1. Criar um objeto 'Random' para gerar um número aleatório entre 1 e 5 (inclusive).
2. Iniciar um loop para solicitar ao usuário que adivinhe o número sorteado, garantindo que a entrada
esteja no intervalo de 1 a 5.
3. Solicitar ao usuário que insira um número entre 1 e 5.
4. Tentar converter a entrada do usuário para um número inteiro e verificar se está dentro do intervalo
permitido (1 a 5). Se a entrada for inválida ou fora do intervalo, exibir uma mensagem de erro e
pedir a entrada novamente.
5. Comparar o número inserido pelo usuário com o número sorteado pelo computador:
   - Se os números coincidirem, exibir a mensagem "Você Acertou!".
   - Caso contrário, exibir a mensagem "Você Errou!" e mostrar o número sorteado.
 */
import javax.swing.JOptionPane;
import java.util.Random;

public class Desafio5 {
    public static void main(String[] args) {
        Random rand = new Random();
        int sortear = rand.nextInt(5) + 1;
        String entrada = "";
        int escolha = 0;

        while (true) {
            entrada = JOptionPane.showInputDialog("Advinhe o Número! (1 a 5): ");

            try {
                escolha = Integer.parseInt(entrada);
                if (escolha >= 1 && escolha <= 5) {
                    break;
                }
                else {
                    throw new Exception();
                }
            }
            catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Escolha Inválida! Tente Novamente...");
            }
        }

        if (escolha == sortear) {
            JOptionPane.showMessageDialog(null, "Você Acertou!");
        }
        else {
            JOptionPane.showMessageDialog(null, "Você Errou!\nNúmero Sorteado: "+ sortear);
        }
    }
}