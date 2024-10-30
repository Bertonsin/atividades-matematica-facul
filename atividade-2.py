class Triangulo:
    def __init__(self, lado_ab, lado_ac, lado_bc):
        self.lado_ab = lado_ab
        self.lado_ac = lado_ac
        self.lado_bc = lado_bc

    def calcula_razao_bissetriz_interna(self):
        # Calcula a razão das partes formadas pela bissetriz interna no lado oposto
        razao = self.lado_ab / self.lado_ac
        return razao

# Exemplo de uso
lado_ab = float(input("Digite o comprimento do lado AB: "))
lado_ac = float(input("Digite o comprimento do lado AC: "))
lado_bc = float(input("Digite o comprimento do lado BC: "))

triangulo = Triangulo(lado_ab, lado_ac, lado_bc)
print("A razão das partes formadas pela bissetriz interna é:", triangulo.calcula_razao_bissetriz_interna())

class TrianguloExterno:
    def __init__(self, lado_ab, lado_ac, lado_bc):
        self.lado_ab = lado_ab
        self.lado_ac = lado_ac
        self.lado_bc = lado_bc

    def calcula_razao_bissetriz_externa(self):
        # Calcula a razão das partes formadas pela bissetriz externa no lado oposto
        razao = self.lado_ab / self.lado_ac
        return razao

# Exemplo de uso
lado_ab = float(input("Digite o comprimento do lado AB: "))
lado_ac = float(input("Digite o comprimento do lado AC: "))
lado_bc = float(input("Digite o comprimento do lado BC: "))

triangulo_externo = TrianguloExterno(lado_ab, lado_ac, lado_bc)
print("A razão das partes formadas pela bissetriz externa é:", triangulo_externo.calcula_razao_bissetriz_externa())
