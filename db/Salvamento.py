from db import prestadores

def Salvamento_Prestador(nome="", 
                         cpf_cnpj="", 
                         data_nascimento="", 
                         rua="", 
                         numero="", 
                         complemento="", 
                         bairro="", 
                         cidade="", 
                         uf="", 
                         cep="", 
                         contato=""):
    
    # Guarda os dados no objeto prestador:
    cadastro = prestadores.Prestador(nome=nome,
                          cpf_cnpj=cpf_cnpj,
                          rua=rua,
                          numero=numero,
                          complemento=complemento,
                          bairro= bairro,
                          cidade=cidade,
                          uf=uf,
                          cep=cep,
                          contato=contato)
    
    # Salvamento no banco de dados:
    try:
        # Tenta usar o método de 
        cadastro.insert_prestador()
    except Exception as e:
        return [False,f"Ocorrou um erro {e} no salvamento dos dados!"]
    else:
        return[True, "Prestador Salvo com Sucesso!"]
