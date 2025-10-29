from datetime import datetime, timedelta
from typing import List

# EXCEÇÕES PERSONALIZADAS
class LocadoraRoupasError(Exception):
    pass

class LimiteRoupasExcedidoError(LocadoraRoupasError):
    pass

class RoupaIndisponivelError(LocadoraRoupasError):
    pass

class RoupaNaoEncontradaError(LocadoraRoupasError):
    pass

# CLASSE ROUPA
class Roupa:
    def __init__(self, descricao: str, categoria: str, tamanho: str, codigo: str, valor_diaria: float):
        self.descricao = descricao
        self.categoria = categoria
        self.tamanho = tamanho
        self.codigo = codigo
        self.valor_diaria = valor_diaria
        self.disponivel = True
        self.data_locacao = None
        self.cliente_atual = None
    
    def locar(self, cliente: 'Cliente'):
        if not self.disponivel:
            raise RoupaIndisponivelError(f"Roupa '{self.descricao}' não está disponível")
        self.disponivel = False
        self.data_locacao = datetime.now()
        self.cliente_atual = cliente
    
    def devolver(self):
        if self.disponivel:
            raise LocadoraRoupasError(f"Roupa '{self.descricao}' já está disponível")
        
        self.disponivel = True
        valor_total = self.calcular_valor_locacao()
        multa = self.calcular_multa()
        
        self.data_locacao = None
        self.cliente_atual = None
        
        return valor_total, multa
    
    def calcular_valor_locacao(self) -> float:
        if self.data_locacao:
            dias_locacao = (datetime.now() - self.data_locacao).days
            return dias_locacao * self.valor_diaria
        return 0.0
    
    def calcular_multa(self) -> float:
        if self.data_locacao:
            dias_locacao = (datetime.now() - self.data_locacao).days
            if dias_locacao > 3:
                dias_atraso = dias_locacao - 3
                return dias_atraso * (self.valor_diaria * 0.5)
        return 0.0
    
    def __str__(self):
        status = "Disponível" if self.disponivel else f"Locada para {self.cliente_atual.nome}"
        return f"{self.descricao} ({self.categoria}) - Tamanho: {self.tamanho} - R$ {self.valor_diaria:.2f}/dia [{status}]"

# CLASSE CLIENTE
class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.roupas_locadas = []
    
    def locar_roupa(self, roupa: Roupa):
        if len(self.roupas_locadas) >= 5:
            raise LimiteRoupasExcedidoError(f"Cliente {self.nome} excedeu o limite de 5 roupas simultâneas")
        
        roupa.locar(self)
        self.roupas_locadas.append(roupa)
        return f"Roupa '{roupa.descricao}' locada com sucesso"
    
    def devolver_roupa(self, roupa: Roupa):
        if roupa not in self.roupas_locadas:
            raise LocadoraRoupasError(f"Roupa '{roupa.descricao}' não foi locada por este cliente")
        
        valor_locacao, multa = roupa.devolver()
        self.roupas_locadas.remove(roupa)
        
        resultado = f"Roupa devolvida. Valor locação: R$ {valor_locacao:.2f}"
        if multa > 0:
            resultado += f" | Multa por atraso: R$ {multa:.2f}"
        
        return resultado
    
    def __str__(self):
        roupas_descricoes = [roupa.descricao for roupa in self.roupas_locadas]
        return f"Cliente: {self.nome} (CPF: {self.cpf}) - Roupas: {len(self.roupas_locadas)} - {roupas_descricoes}"

# CLASSE LOCADORA (SISTEMA PRINCIPAL)
class LocadoraRoupas:
    def __init__(self):
        self.roupas = []
        self.clientes = []
    
    def cadastrar_roupa(self, descricao: str, categoria: str, tamanho: str, codigo: str, valor_diaria: float):
        roupa = Roupa(descricao, categoria, tamanho, codigo, valor_diaria)
        self.roupas.append(roupa)
        return roupa
    
    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str):
        cliente = Cliente(nome, cpf, telefone)
        self.clientes.append(cliente)
        return cliente
    
    def buscar_roupa_por_codigo(self, codigo: str):
        for roupa in self.roupas:
            if roupa.codigo == codigo:
                return roupa
        raise RoupaNaoEncontradaError(f"Roupa com código '{codigo}' não encontrada")
    
    def buscar_cliente_por_cpf(self, cpf: str):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def listar_roupas_disponiveis(self):
        return [roupa for roupa in self.roupas if roupa.disponivel]