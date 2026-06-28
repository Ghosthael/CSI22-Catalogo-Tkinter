from db import prestadores

# Função de busca de dados e entrega de lista de tuplas
def buscar_prestadores_nome(nome=""):
   '''Busca um prestador com base no nome dele. Retorna Lista com os campos ou uma lista vazia caso não encontrado! '''
   # Atribui classe prestador:
   prestador = prestadores.Prestador()

   # Resultado:
   resultado = prestador.select_prestador(dado=nome)

   # Entrega lista de dados:
   if resultado[0]:
      # Retorna a lista:
      return resultado[2]
   else:
      return []
