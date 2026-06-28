from ui import tela_cadastro

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

def validar_nome(nome: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações do Nome:
    if nome == "":
        return [False, "Nome não pode estar vazio."]
    elif nome.isalpha():
        return [False, "Nome Não Pode Conter Números ou Caracteres especiais!"]
    elif len(nome) < 3:
        return [False, "Nome Muito Curto!"]
    return True


def validar_cpf_cnpj(cpf_cnpj: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações do cpf
    if not cpf_cnpj:
        return [False, "Campo CPF/CNPJ é Obrigatório!"]
    if not cpf_cnpj.isdigit():
        return [False, "Digite Somente Numeros!"]
    # Verificacao de sintaxe de cnpj e cpf:
    if len(cpf_cnpj) == 14:
        if not verificar_cnpj(cnpj=cpf_cnpj):
            return [False, "CNPJ inválido!"]
    elif len(cpf_cnpj) == 11:
        if not verificar_cpf(cpf=cpf_cnpj):
            return [False, "CPF inválido!"]
    else:
        return [False, "O Campo deve ter 11 ou 14 dígitos (CPF ou CNPJ)"]
    return True

def validar_nascimento(nascimento: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações da Rua:
    if not nascimento:
        return [False, "Campo Data de Nascimento é Obrigatório!"]
    elif not len(nascimento) == 8:
        return [False, "Digite a Data de Nascimento na forma: DDMMYYYY!"]
    return True

def validar_rua(rua: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações da Rua:
    if not rua:
        return [False, "Campo Rua é Obrigatório!"]
    elif len(rua) < 3:
        return [False, "Rua Muito Curta!"]
    return True


def validar_numero(numero: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações do Numero:
    if not numero:
        return [False, "Campo Numero é Obrigatório!"]
    elif not numero.isdigit():
        return [False, "Campo Numero deve ser número!"]
    return True

def validar_complemento(complemento: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações da Rua:
    if not complemento:
        return [False, "Campo Complemento é Obrigatório!"]
    elif len(complemento) < 3:
        return [False, "Complemento Muito Curta!"]
    return True

def validar_cep(cep: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificação de CEP:
    if not cep:
        return [False, "Campo CEP é Obrigatório!"]
    elif len(cep) != 8:
        return [False, "Campo CEP deve ter 8 dígitos!"]
    return True


def validar_bairro(bairro: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificações de Bairro:
    if not bairro:
        return [False, "Campo Bairro é Obrigatório!"]
    elif not bairro.isalpha():
        return [False, "Bairro Não Pode ter números!"]
    return True


def validar_cidade(cidade: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificacao Cidade:
    if not cidade:
        return [False, "Campo Cidade é Obrigatório!"]
    return True

#função validadora de uf
def validar_uf(uf: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificação UF:
    if not uf:
        return [False, "Campo UF é Obrigatório!"]
    elif len(uf) != 2:
        return [False, "UF pode ter somente 2 letras!"]
    return True

# Funçao validadora de contato
def validar_contato(contato: str):
    '''Função que retorna tupla [resultado,mensagem_erro] para o dado em questão'''
    # Verificação Contato:
    if not contato:
        return [False, "Campo Contato é Obrigatório!"]
    elif len(contato) != 11:
        return [False, "Campo Contato deve ter 11 dígitos!"]
    return True
