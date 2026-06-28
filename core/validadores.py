
# Função de verificação de CPF
def verificar_cpf(cpf=""):
    '''Dada uma string de cpf, devolve True se válido e False se não'''
    # Garante tamanho do cpf:
    if(len(cpf) != 11):
        return False

    # Primeiro dígito
    soma_d1 = sum(int(cpf[i]) * (10 - i) for i in range(0, 9))
    resto_d1 = soma_d1 % 11
    d1 = 0 if resto_d1 < 2 else 11 - resto_d1

    if d1 != int(cpf[9]):
        return False

    # Segundo dígito
    soma_d2 = sum(int(cpf[i]) * (11 - i) for i in range(0, 10))
    resto_d2 = soma_d2 % 11
    d2 = 0 if resto_d2 < 2 else 11 - resto_d2

    if d2 != int(cpf[10]):
        return False
    
    # Caso contrário, entrega verdadeiro
    return True

def verificar_cnpj(cnpj=""):

    '''Dada uma string de cnpj, devolve True se válido e False se não'''

    if(len(cnpj)!=14):

        return False

    # Calculo da soma do primeiro algarismo:
    pesos = [5,4,3,2,9,8,7,6,5,4,3,2]
    somad1 = sum([pesos[i]*int(cnpj[i]) for i in range(0,12)])

    # Calcula digito d1 com base no resto da soma d1:
    restod1 = somad1 % 11
    if restod1 < 2:
        d1 = 0
    else:
        d1 = 11 - restod1

    # Verifica se o digito d1 corresponde:
    if not d1 == int(cnpj[12]):
        return False

    # Lógica de verificação do segundo digito:
    pesos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    somad2 = sum([pesos[i]*int(cnpj[i]) for i in range(0,13)])

    # Calcula digito d1 com base no resto da soma d1:
    restod2 = somad2 % 11
    if restod2 < 2:
        d2 = 0
    else:
        d2 = 11 - restod2

    # Verifica se o digito d1 corresponde:
    if not d2 == int(cnpj[13]):
        return False

    # Se todos iguais, então retorna true
    return True
