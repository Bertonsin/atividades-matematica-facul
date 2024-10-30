
# Realiza o cálculo a razão entre os segmentos divididos pela bissetriz interna usando ângulos adjacentes
def razao_bissetriz_interna(ab, ac):
    return ab / ac

# Testes
ab, ac = 8, 6  # Lados do triângulo em relação ao vértice A
razao_interna = razao_bissetriz_interna(ab, ac)
print(f"A razão entre BD e DC pela bissetriz interna é: {razao_interna:.2f}")