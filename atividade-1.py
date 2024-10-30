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
        (triangulo1.lado2 / triangulo2.lado2 == triangulo1.lado3 / triangulo2.lado3 and triangulo1.angulo2 == triangulo2.angulo2) or
        (triangulo1.lado1 / triangulo2.lado1 == triangulo1.lado3 / triangulo2.lado3 and triangulo1.angulo3 == triangulo2.angulo3)
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

# Função principal para verificar semelhança
def verifica_semelhanca(triangulo1, triangulo2):
    if verifica_lll(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério LLL."
    elif verifica_aa(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério AA."
    elif verifica_lal(triangulo1, triangulo2):
        return "Os triângulos são semelhantes pelo critério LAL."
    else:
        return "Os triângulos não são semelhantes."

# Exemplos de teste específicos para cada critério

# Exemplo para LLL: Triângulos com lados proporcionais
triangulo1 = Triangulo(3, 4, 5)
triangulo2 = Triangulo(6, 8, 10)
print(verifica_semelhanca(triangulo1, triangulo2))

# Exemplo para LAL: Triângulos com dois lados proporcionais e o ângulo entre eles congruente
triangulo3 = Triangulo(2, 4, 5, 60, 60, 60)
triangulo4 = Triangulo(3, 6, 7, 60, 60, 60)
print(verifica_semelhanca(triangulo3, triangulo4)) 

# Exemplo para AA: Triângulos com dois ângulos congruentes
triangulo5 = Triangulo(3, 5, 7, 45, 60, 75)
triangulo6 = Triangulo(5, 7, 9, 45, 60, 75)
print(verifica_semelhanca(triangulo5, triangulo6))
