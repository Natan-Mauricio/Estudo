class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def area(self):
        return self.altura * self.largura
    
    def perimetro(self):
        return 2*self.altura + 2*self.largura

ret = Retangulo(10, 10)
print(f'Área do retângulo: {ret.area()}')
print(f'Perímetro do retângulo: {ret.perimetro()}')