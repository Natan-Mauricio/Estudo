import pytest
from datetime import datetime, timedelta
from locadora_roupas import (
    Roupa, Cliente, LocadoraRoupas, 
    RoupaIndisponivelError, LimiteRoupasExcedidoError, RoupaNaoEncontradaError,
    LocadoraRoupasError
)

class TestLocadoraRoupas:
    def test_roupa_locacao_devolucao(self):
        # Testa o processo básico de locação e devolução de roupas
        roupa = Roupa("Vestido Longo", "Festa", "M", "VEST001", 30.0)
        cliente = Cliente("Maria", "123.456.789-00", "(11) 99999-9999")
        
        assert roupa.disponivel == True
        
        roupa.locar(cliente)
        assert roupa.disponivel == False
        assert roupa.cliente_atual == cliente
        
        valor, multa = roupa.devolver()
        assert roupa.disponivel == True
        assert roupa.cliente_atual is None
    
    def test_roupa_locacao_indisponivel(self):
        # Testa tentativa de locar roupa indisponível
        roupa = Roupa("Terno", "Formal", "G", "TERN001", 40.0)
        cliente1 = Cliente("Cliente1", "111", "99999")
        cliente2 = Cliente("Cliente2", "222", "88888")
        
        roupa.locar(cliente1)
        
        with pytest.raises(RoupaIndisponivelError):
            roupa.locar(cliente2)
    
    def test_cliente_limite_roupas(self):
        # Testa limite de roupas por cliente
        cliente = Cliente("Teste", "123", "99999")
        roupas = [
            Roupa(f"Roupa {i}", "Festa", "M", f"COD{i}", 25.0) 
            for i in range(6)
        ]
        
        # Deve conseguir locar 5 roupas
        for i in range(5):
            cliente.locar_roupa(roupas[i])
        
        # Deve falhar ao tentar locar a sexta
        with pytest.raises(LimiteRoupasExcedidoError):
            cliente.locar_roupa(roupas[5])
    
    def test_calculo_valor_locacao(self):
        # Testa cálculo do valor da locação
        roupa = Roupa("Fantasia", "Carnaval", "P", "FANT001", 50.0)
        cliente = Cliente("Teste", "123", "99999")
        
        roupa.locar(cliente)
        
        # Simula 2 dias de locação
        roupa.data_locacao = datetime.now() - timedelta(days=2)
        
        valor = roupa.calcular_valor_locacao()
        assert valor == 100.0  # 2 dias × R$ 50,00
    
    def test_calculo_multa(self):
        # Testa cálculo de multa por atraso
        roupa = Roupa("Vestido Noiva", "Casamento", "M", "NOIV001", 100.0)
        cliente = Cliente("Teste", "123", "99999")
        
        roupa.locar(cliente)
        
        # Simula atraso de 2 dias (total 5 dias)
        roupa.data_locacao = datetime.now() - timedelta(days=5)
        
        multa = roupa.calcular_multa()
        assert multa == 100.0  # 2 dias × (R$ 100,00 × 50%)
    
    def test_sistema_locadora_integracao(self):
        # Teste integrado do sistema completo
        locadora = LocadoraRoupas()
        
        # Cadastro
        roupa = locadora.cadastrar_roupa("Blazer", "Formal", "G", "BLAZ001", 35.0)
        cliente = locadora.cadastrar_cliente("João", "123", "99999")
        
        # Busca
        assert locadora.buscar_roupa_por_codigo("BLAZ001") == roupa
        assert locadora.buscar_cliente_por_cpf("123") == cliente
        
        # Locação
        cliente.locar_roupa(roupa)
        assert len(locadora.listar_roupas_disponiveis()) == 0
        
        # Devolução
        resultado = cliente.devolver_roupa(roupa)
        assert "devolvida" in resultado.lower()
        assert len(locadora.listar_roupas_disponiveis()) == 1
    
    def test_buscar_roupa_inexistente(self):
        # Testa busca por roupa que não existe
        locadora = LocadoraRoupas()
        
        with pytest.raises(RoupaNaoEncontradaError):
            locadora.buscar_roupa_por_codigo("CODIGO_INEXISTENTE")
    
    def test_devolver_roupa_nao_locada(self):
        # Testa devolução de roupa não locada pelo cliente
        roupa = Roupa("Saia", "Festa", "P", "SAIA001", 20.0)
        cliente = Cliente("Maria", "123", "99999")
        
        with pytest.raises(LocadoraRoupasError): 
            cliente.devolver_roupa(roupa)