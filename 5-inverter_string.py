def inverter_string(s):
    """Inverte os caracteres de uma string."""
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida  # Adiciona o caractere no início
    return string_invertida

if __name__ == "__main__":
    # String a ser invertida
    string_original = "String de exemplo"
    
    string_invertida = inverter_string(string_original)
    print("String original:", string_original)
    print("String invertida:", string_invertida)