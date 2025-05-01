'''
Nome: Natan Maurício da Silva
RA: 2401712
Turma: CC 3A MANHÃ
'''
import networkx as nx
import matplotlib.pyplot as plt

def exibir_grafo(grafo):
    G = nx.Graph(grafo)
    pos = nx.spring_layout(G, k=0.5, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.gcf().canvas.manager.set_window_title("Grafo Original")
    plt.show()

def busca_largura(grafo, inicio):
    visitados = []
    fila = [inicio]
    indice = 0
    
    while indice < len(fila):
        no = fila[indice]
        indice += 1
        
        if no not in visitados:
            visitados.append(no)
            for vizinho in grafo[no]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
    
    return visitados

def busca_profundidade(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = []
    visitados.append(inicio)
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_profundidade(grafo, vizinho, visitados)
    return visitados

def exibir_busca_largura(grafo, ordem_busca_largura):
    G = nx.Graph()
    posicoes = {}
    nivel = 0
    nos_por_nivel = {}
    
    # Organiza os nós por nível
    for i, no in enumerate(ordem_busca_largura):
        if i == 0:
            nivel = 0
        else:
            for pai in ordem_busca_largura[:i]:
                if no in grafo[pai]:
                    nivel = nos_por_nivel[pai] + 1
                    break
        nos_por_nivel[no] = nivel
    
    # Calcula posições
    for no in ordem_busca_largura:
        nivel = nos_por_nivel[no]
        posicoes[no] = (nivel, -ordem_busca_largura.index(no)/2)
    
    # Adiciona arestas da árvore busca_largura
    for i in range(1, len(ordem_busca_largura)):
        no = ordem_busca_largura[i]
        for pai in ordem_busca_largura[:i]:
            if no in grafo[pai]:
                G.add_edge(pai, no)
                break
    
    plt.figure() 
    nx.draw(G, posicoes, with_labels=True, node_color='lightgreen', node_size=800)
    plt.gcf().canvas.manager.set_window_title("Árvore da Busca em Largura")
    plt.show()

def exibir_busca_profundidade(grafo, ordem_busca_profundidade):
    G = nx.Graph()
    pos = {}
    profundidade = 0
    caminho = []
    
    # Calcula o caminho e profundidades
    for i, no in enumerate(ordem_busca_profundidade):
        if i == 0:
            profundidade = 0
        else:
            for anterior in reversed(caminho):
                if no in grafo[anterior[0]]:
                    profundidade = anterior[1] + 1
                    break
        caminho.append((no, profundidade))
        pos[no] = (profundidade, -i/2)
    
    # Adiciona arestas do caminho busca_profundidade
    for i in range(1, len(ordem_busca_profundidade)):
        no = ordem_busca_profundidade[i]
        for anterior in reversed(ordem_busca_profundidade[:i]):
            if no in grafo[anterior]:
                G.add_edge(anterior, no)
                break
    
    nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=800)
    plt.gcf().canvas.manager.set_window_title("Caminho da Busca em Profundidade")
    plt.show()

def exibir(grafo, inicio):
    exibir_grafo(grafo)
    exibir_busca_largura(grafo, busca_largura(grafo, inicio))
    exibir_busca_profundidade(grafo, busca_profundidade(grafo, inicio))

#Testes:
grafo1 = {
0: [1],
1: [0, 2],
2: [1, 3, 4, 5, 6],
3: [2, 4, 5, 6],
4: [2, 3, 5, 6],
5: [2, 3, 4, 6],
6: [2, 3, 4, 5, 8],
7: [9, 10],
8: [6, 9],
9: [7, 8, 10],
10: [7, 9]
}

grafo2 = {
'A': ['B', 'F', 'D'],
'B': ['A', 'C'],
'C': ['B', 'D', 'E'],
'D': ['C', 'E', 'A'],
'E': ['D', 'F', 'C'],
'F': ['E', 'A']
}

exibir(grafo1, 0)
exibir(grafo2, 'A')