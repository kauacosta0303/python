def limpar_cpf(cpf):
    """Remove caracteres não numéricos do CPF e retorna uma lista de dígitos."""
    return [int(caractere) for caractere in cpf if caractere.isdigit()]

def calcular_resto(soma):
    """Calcula o resto da divisão da soma por 11 e retorna a unidade."""
    return soma % 11

def verificar_cpf(cpf):
    """Verifica se o CPF é válido."""
    # Limpa o CPF para obter apenas os dígitos
    cpf_limpo = limpar_cpf(cpf)
    
    # Pega os 9 primeiros dígitos do CPF
    primeiros_9_digitos = cpf_limpo[:9]
    
    # Passo 1: Multiplica cada um dos 9 primeiros dígitos pelo seu índice + 1
    soma_1 = sum(digito * (indice + 1) for indice, digito in enumerate(primeiros_9_digitos))
    resto_1 = calcular_resto(soma_1) % 10
    
    # Verifica o primeiro dígito verificador
    primeiro_digito_verificador = cpf_limpo[9]
    if resto_1 != primeiro_digito_verificador:
        return False
    
    # Passo 2: Multiplica os 10 primeiros dígitos (incluindo o primeiro dígito verificador)
    # pelo índice correspondente começando em 0
    primeiros_10_digitos = cpf_limpo[:10]
    soma_2 = sum(digito * indice for indice, digito in enumerate(primeiros_10_digitos))
    resto_2 = calcular_resto(soma_2) % 10
    
    # Verifica o segundo dígito verificador
    segundo_digito_verificador = cpf_limpo[10]
    if resto_2 != segundo_digito_verificador:
        return False
    
    # Se ambos os dígitos verificadores forem válidos, o CPF é válido
    return True

# Exemplo de uso
cpf = input("Qual seu CPF?")
resultado = verificar_cpf(cpf)


if resultado:
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
