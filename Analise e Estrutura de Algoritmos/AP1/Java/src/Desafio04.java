/*
31. Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

Algoritmo:
1. Criar um objeto 'Random' para gerar a escolha aleatória do computador (entre 1 e 3).
2. Exibir uma janela de input com as opções de "Pedra", "Papel" e "Tesoura" para o jogador escolher.
3. Validar se a entrada do jogador é válida (1, 2 ou 3), repetindo a solicitação até que uma escolha
válida seja fornecida.
4. Converter a entrada do jogador para um número inteiro.
5. Comparar a escolha do jogador com a escolha do computador para determinar o resultado:
   - Se as escolhas forem iguais, o jogo empata.
   - Se o jogador ganhar (Pedra > Tesoura, Papel > Pedra, Tesoura > Papel), exibir "Ganhou!".
   - Caso contrário, exibir "Perdeu!".
6. Exibir uma janela com as escolhas do jogador e do computador, além do resultado do
jogo (Ganhou, Perdeu ou Empatou).
7. Criar uma função 'nome()' que converte o número da escolha para o nome
correspondente ("Pedra", "Papel" ou "Tesoura").
 */
import java.util.Random;
import javax.swing.JOptionPane;

public class Desafio04 {
    public static void main(String[] args) {
        Random rand = new Random();
        int pc = rand.nextInt(3) + 1;
        String entrada = "";
        String result = "";

        while (true) {
            entrada = JOptionPane.showInputDialog("JoKenPo\n\n1. Pedra\n2. Papel\n3. Tesoura\n\nEscolha: ");

            if (entrada.equals("1") || entrada.equals("2") || entrada.equals("3")) {
                break;
            }

            JOptionPane.showMessageDialog(null, "Opção Inválida! Tente Novamente...");
        }

        int jogador = Integer.parseInt(entrada);

        if (jogador == pc) {
            result = "Empatou!";
        } else {
            if ((jogador == 1 && pc == 3) || (jogador == 2 && pc == 1) || (jogador == 3 && pc == 2)) {
                result = "Ganhou!";
            } else {
                result = "Perdeu!";
            }
        }

        JOptionPane.showMessageDialog(null, "Sua Escolha: " + nome(jogador) + "\nComputador: " + nome(pc) + "\nVocê " + result);
    }

    public static String nome(int escolha) {
        switch (escolha) {
            case 1:
                return "Pedra";
            case 2:
                return "Papel";
            case 3:
                return "Tesoura";
            default:
                return "Escolha Invalida!";
        }
    }
}
