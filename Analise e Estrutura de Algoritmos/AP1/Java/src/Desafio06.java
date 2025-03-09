/*
55. Vamos melhorar o jogo que fizemos no exercício
32. A partir de agora, o computador vai sortear um número entre
1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.

Algoritmo:
1. Criar um objeto 'Random' para gerar um número aleatório entre 1 e 10 (inclusive).
2. Inicializar uma variável 'i' para contar o número de tentativas feitas pelo usuário (limite de 4 tentativas).
3. Iniciar um loop de tentativas (até 4 tentativas).
4. Dentro do loop, exibir uma janela de input solicitando que o usuário adivinhe um número entre 1 e 10.
5. Validar a entrada do usuário para garantir que seja um número inteiro dentro do intervalo de 1 a 10.
6. Se a entrada for inválida, exibir uma mensagem de erro e pedir a entrada novamente.
7. Comparar o número inserido pelo usuário com o número sorteado:
   - Se o número inserido for igual ao sorteado, exibir a mensagem "Você Acertou!" e sair do loop de tentativas.
   - Caso contrário, exibir a mensagem "Você Errou!" com o número de tentativas restantes e incrementar a variável 'i'.
8. Se o usuário não acertar após 4 tentativas, exibir a mensagem "Suas Tentativas Acabaram!".
*/
import javax.swing.JOptionPane;
import java.util.Random;

public class Desafio06 {
    public static void main(String[] args) {
        Random rand = new Random();
        int sortear = rand.nextInt(10) + 1;
        String entrada = "";
        int escolha = 0;
        int i = 1;

        while (i <= 4) {
            while (true) {
                entrada = JOptionPane.showInputDialog("Advinhe o Número! (1 a 10): ");

                try {
                    escolha = Integer.parseInt(entrada);
                    if (escolha >= 1 && escolha <= 10) {
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
                break;
            }
            else {
                JOptionPane.showMessageDialog(null, "Você Errou! Tentativas: ("+ i +"/4)");
                i += 1;
            }
        }

        if (i == 5) {
            JOptionPane.showMessageDialog(null, "Suas Tentativas Acabaram!");
        }
    }
}
