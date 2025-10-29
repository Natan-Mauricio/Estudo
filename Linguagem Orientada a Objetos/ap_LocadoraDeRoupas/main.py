from src.locadora_roupas import LocadoraRoupas, RoupaIndisponivelError, LimiteRoupasExcedidoError
from datetime import datetime, timedelta

def main():
    # Criando a locadora
    locadora = LocadoraRoupas()
    
    # Cadastrando roupas
    roupas = [
        ("Vestido Longo Vermelho", "Festa", "M", "VEST001", 45.0),
        ("Terno Preto", "Formal", "G", "TERN001", 60.0),
        ("Fantasia Super-Herói", "Fantasia", "U", "FANT001", 75.0),
        ("Vestido Noiva", "Casamento", "P", "NOIV001", 120.0),
        ("Blazer Azul Marinho", "Formal", "M", "BLAZ001", 40.0),
        ("Fantasia Princesa", "Fantasia", "M", "FANT002", 65.0),
        ("Smoking", "Formal", "GG", "SMOK001", 80.0)
    ]
    
    for descricao, categoria, tamanho, codigo, diaria in roupas:
        locadora.cadastrar_roupa(descricao, categoria, tamanho, codigo, diaria)
    
    # Cadastrando clientes
    clientes = [
        ("Ana Carolina Silva", "111.222.333-44", "(11) 97777-7777"),
        ("Carlos Eduardo Lima", "555.666.777-88", "(11) 96666-6666"),
    ]
    
    for nome, cpf, telefone in clientes:
        locadora.cadastrar_cliente(nome, cpf, telefone)
    
    print("=== SISTEMA DE LOCADORA DE ROUPAS E FANTASIAS ===\n")
    
    # Demonstração das funcionalidades
    ana = locadora.buscar_cliente_por_cpf("111.222.333-44")
    carlos = locadora.buscar_cliente_por_cpf("555.666.777-88")
    
    vestido = locadora.buscar_roupa_por_codigo("VEST001")
    terno = locadora.buscar_roupa_por_codigo("TERN001")
    fantasia = locadora.buscar_roupa_por_codigo("FANT001")
    smoking = locadora.buscar_roupa_por_codigo("SMOK001")
    
    try:
        # Cliente Ana loca roupas
        print("=== LOCAÇÕES DA ANA ===")
        print(ana.locar_roupa(vestido))
        print(ana.locar_roupa(fantasia))
        print(f"\nStatus da Ana:\n{ana}")
        
        # Cliente Carlos loca roupas
        print("\n=== LOCAÇÕES DO CARLOS ===")
        print(carlos.locar_roupa(terno))
        print(carlos.locar_roupa(smoking))
        print(f"\nStatus do Carlos:\n{carlos}")
        
        # Simular passagem de tempo para cálculo de valores
        # Vestido: 2 dias de locação (dentro do prazo)
        vestido.data_locacao = datetime.now() - timedelta(days=2)
        
        # Fantasia: 5 dias de locação (2 dias de atraso)
        fantasia.data_locacao = datetime.now() - timedelta(days=5)
        
        # Terno: 4 dias de locação (1 dia de atraso)  
        terno.data_locacao = datetime.now() - timedelta(days=4)
        
        # Smoking: 1 dia de locação (dentro do prazo)
        smoking.data_locacao = datetime.now() - timedelta(days=1)
        
        print("\n=== TENTATIVA DE LOCAR ROUPA JÁ LOCADA ===")
        blazer = locadora.buscar_roupa_por_codigo("BLAZ001")
        print(carlos.locar_roupa(vestido))  #Vestido já está locado pela Ana
        
    except (RoupaIndisponivelError, LimiteRoupasExcedidoError) as e:
        print(f"Erro: {e}")
    
    # Devoluções
    print("\n=== DEVOLUÇÕES ===")
    print(ana.devolver_roupa(vestido))    # 2 dias: R$ 90.00
    print(ana.devolver_roupa(fantasia))   # 5 dias: R$ 375.00 + multa R$ 75.00
    print(carlos.devolver_roupa(terno))   # 4 dias: R$ 240.00 + multa R$ 30.00
    print(carlos.devolver_roupa(smoking)) # 1 dia: R$ 80.00
    
    print("\n=== RELATÓRIO FINAL ===")
    print("Roupas disponíveis:")
    for roupa in locadora.listar_roupas_disponiveis():
        print(f"  - {roupa}")
    
    print(f"\nTotal de clientes cadastrados: {len(locadora.clientes)}")
    print(f"Total de roupas cadastradas: {len(locadora.roupas)}")

if __name__ == "__main__":
    main()