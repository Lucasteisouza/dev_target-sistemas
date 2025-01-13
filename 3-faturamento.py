import json

def calcular_faturamento(faturamentos):
    """Calcula o menor, maior e o número de dias acima da média do faturamento."""
    # Filtrar apenas os dias com faturamento
    faturamentos_validos = [f for f in faturamentos if f > 0]
    
    if not faturamentos_validos:
        return None, None, 0  # Se não houver faturamento, retornar valores nulos

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)
    dias_acima_media = sum(1 for faturamento in faturamentos_validos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

if __name__ == "__main__":
    # Carregar dados de faturamento do arquivo JSON
    with open('dados.json', 'r') as file:
        dados = json.load(file)

    # Extrair os valores de faturamento
    faturamentos_diarios = [dia['valor'] for dia in dados]

    menor, maior, dias_acima_media = calcular_faturamento(faturamentos_diarios)
    
    if menor is not None and maior is not None:
        print(f"O menor valor de faturamento: {menor}")
        print(f"O maior valor de faturamento: {maior}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    else:
        print("Não há dados de faturamento válidos para calcular.")