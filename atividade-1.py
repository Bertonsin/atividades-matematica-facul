class Triangulo:
    def __init__(self, lado1, lado2, lado3, angulo1=None, angulo2=None, angulo3=None):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3

def verifica_lal(triangulo1, triangulo2):
    # Verifica se dois lados são proporcionais e o ângulo entre eles é congruente
    return (
        (triangulo1.lado1 / triangulo2.lado1 == triangulo1.lado2 / triangulo2.lado2 and triangulo1.angulo1 == triangulo2.angulo1) or
        (triangulo1.lado1 / triangulo2.lado3 == triangulo1.lado3 / triangulo2.lado2 and triangulo1.angulo2 == triangulo2.angulo2)
    )

def verifica_aa(triangulo1, triangulo2):
    # Verifica se dois ângulos são congruentes
    angulos1 = {triangulo1.angulo1, triangulo1.angulo2, triangulo1.angulo3}
    angulos2 = {triangulo2.angulo1, triangulo2.angulo2, triangulo2.angulo3}
    return len(angulos1.intersection(angulos2)) >= 2

def verifica_lll(triangulo1, triangulo2):
    # Verifica se todos os lados são proporcionais
    return (
        triangulo1.lado1 / triangulo2.lado1 == triangulo1.lado2 / triangulo2.lado2 == triangulo1.lado3 / triangulo2.lado3
    )

# Verifica a semelhança entre crianças
def verifica_seme_lhanca(triangulo1, triangulo2):
    if verifica_lal(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério LAL."
    elif verifica_aa(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério AA."
    elif verifica_lll(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério LLL."
    else:
        return "Os triângulos não são semelhantes."

triangulo1 = Triangulo(2, 3, 4, 30, 60, 90)
triangulo2 = Triangulo(4, 6, 8, 30, 60, 90)

print(verifica_seme_lhanca(triangulo1, triangulo2))  # Deve retornar LLL

triangulo3 = Triangulo(2, 5, 6, 30, 45, 105)
triangulo4 = Triangulo(4, 10, 12, 30, 45, 105)

print(verifica_seme_lhanca(triangulo3, triangulo4))  # Deve retornar LAL

triangulo5 = Triangulo(3, 5, 7, 45, 60, 75)
triangulo6 = Triangulo(6, 10, 14, 45, 60, 75)

print(verifica_seme_lhanca(triangulo5, triangulo6))  # Deve retornar LLL

triangulo7 = Triangulo(2, 4, 5, 60, 60, 60)
triangulo8 = Triangulo(3, 6, 7, 60, 60, 60)

print(verifica_seme_lhanca(triangulo7, triangulo8))  # Deve retornar AA
