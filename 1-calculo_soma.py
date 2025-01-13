def calcular_soma(indice):
    """Calcula a soma dos números de 1 até o índice fornecido (exclusivo)."""
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += (k - 1)  # Somar o valor anterior de K
    return soma

if __name__ == "__main__":
    INDICE = 13
    resultado = calcular_soma(INDICE)
    print("O valor da variável SOMA ao final do processamento é:", resultado)