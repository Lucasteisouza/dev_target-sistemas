def gera_fibonacci(n):
    """Gera a sequência de Fibonacci até o número n e retorna a sequência."""
    fibonacci = [0, 1]
    while True:
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo > n:
            break
        fibonacci.append(proximo)
    return fibonacci

def verifica_numero_fibonacci(numero):
    """Verifica se um número pertence à sequência de Fibonacci."""
    fibonacci = gera_fibonacci(numero)
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

if __name__ == "__main__":
    numero_informado = 21  # Você pode alterar este número
    resultado = verifica_numero_fibonacci(numero_informado)
    print(resultado)