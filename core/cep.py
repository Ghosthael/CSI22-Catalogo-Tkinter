# Arquivo de API de cep
import requests 
import re

# Fazer função retornar lista com os campos de volta da api:
def dados_cep(cep_str):
    '''Função de retornar lista de dados que a api de cep pode entregar'''

    # Tratamento minimo de dados:
    # Corte de caracteres / e -:
    cep = re.sub(r'\D','',cep_str)

    # Verificação de formatação do cep:
    if len(cep) != 8:
        return [False,"CEP deve ter 9 digitos!"]
    elif cep.isdigit() is not True:
        return [False, "CEP deve conter apenas dígitos!"]
     
    # API de consulta:
    # Caracteriza a url de chamada:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        # Faz a requisição
        resposta = requests.get(url,timeout=5)

        # Levanta exceção, se houver:
        resposta.raise_for_status()

        # Extrai dados do json encontrado
        dados = resposta.json()

    except requests.exceptions.Timeout:
        return False, "Tempo de Consulta Esgotado!"
    except requests.exceptions.ConnectionError:
        return False, "Sem Conexão!"
    
    # Se houve algum erro, mesmo sem erro de requisição:
    if dados.get("erro"):
        return False, "CEP não encontrado!"
    
    # Retorna dicionário com os dados encontrados pelo cep
    return True, {
        "rua": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "uf": dados.get("uf", ""),
        "complemento": dados.get("complemento", ""),
        "cep": dados.get("cep", ""),
    }
 