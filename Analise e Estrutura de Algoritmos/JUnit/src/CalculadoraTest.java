/*
Nome: Natan Maurício da Silva
RA: 2401712
Turma: CC 3A MANHÃ
 */

import org.junit.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculadoraTest {
    @Test
    public void somaTest() {
        assertEquals(5.0, Calculadora.soma(2.0, 3.0));
        assertEquals(0.0, Calculadora.soma(-2.0, 2.0));
        assertEquals(-5.0, Calculadora.soma(-2.0, -3.0));
    }

    @Test
    public void subtracaoTest() {
        assertEquals(1.0, Calculadora.subtracao(3.0, 2.0));
        assertEquals(-5.0, Calculadora.subtracao(-2.0, 3.0));
        assertEquals(0.0, Calculadora.subtracao(2.0, 2.0));
    }

    @Test
    public void multiplicacaoTest() {
        assertEquals(6.0, Calculadora.multiplicacao(2.0, 3.0));
        assertEquals(-6.0, Calculadora.multiplicacao(-2.0, 3.0));
        assertEquals(0.0, Calculadora.multiplicacao(0.0, 3.0));
    }

    @Test
    public void potenciacaoTest() {
        assertEquals(8.0, Calculadora.potenciacao(2.0, 3.0));
        assertEquals(1.0, Calculadora.potenciacao(5.0, 0.0));
        assertEquals(0.25, Calculadora.potenciacao(2.0, -2.0));
        assertEquals(4096.0, Calculadora.potenciacao(2.0, 12.0));
    }
}