# Restaurante (Pedidos)
# Campos utilizados no CRUD:
# • - Número do pedido
# • - Cliente
# • - Prato
# • - Quantidade
# • - Valor total
import sqlite3

### Função Menu
while True:
  print("\n===== SISTEMA CONN =====")
  print("1 - Cadastrar cliente\n")
  print("2 - Listar pedidos\n")
  print("3 - Buscar pedido\n")
  print("4 - Atualizar pedido\n")
  print("5 - Remover pedido\n")
  print("0 - Sair\n")

  options = input("Escolha uma opção: ")

  if options == "1":
    creat_cliente()
  elif options == "2":
    list_pedidos()
  elif options == "3":
    search_pedido()
  elif options == "4":
    update_pedido()
  elif options == "5":
    delete_pedido()
  elif options == "0":
    print("Saindo...")
    break
  else:
    print("Opção inválida! Tente novamente.")


## Função criar usuário

def creat_cliente():
  print("\n=== CADASTRAR PEDIDO ===")
  cardapio = 0
  codigo = input("Digite o código do pedido: ").strip()
  cliente = input("Digite o nome do cliente: ").strip()
  prato = input("Digite o prato: ").strip()
  quantidade = input("Digite a quantidade: ").strip()
  valor_total = input("Digite o valor total: ").strip()

  pedido = {
      "codigo": codigo,
      "cliente": cliente,
      "prato": prato,
      "quantidade": quantidade,
      "valor_total": valor_total
  }
  cardapio.append(pedido)
  print("✔ Pedido cadastrado com sucesso!")

## List pedidos

def list_pedidos():
    item = []
    item.append(creat_cliente(), list_pedidos(),
    search_pedido(), update_pedido(),delete_pedido())
    return item


## Buscar pedidos
def search_pedido():
    print("\n=== BUSCAR PEDIDO ===")
    numero = input("Número do pedido: ")
    if numero == "":
        print("Erro: digite um número!")
        return
    numero = int(numero)
    for p in pedido:
        if p["numero"] == numero:
            print("\nPedido encontrado!")
            print("Número:", p["numero"])
            print("Cliente:", p["cliente"])
            print("Prato:", p["prato"])
            print("Quantidade:", p["quantidade"])
            print("Valor total: R$", p["valor_total"])
            return
    print("Pedido não encontrado!")
search_pedido()

## Update pedidos
def update_pedido():
  print("\n=== ATUALIZAR PEDIDO ===")
  cardapio = 0
  codigo = input("Digite o código do pedido para atualizar:" )
  for pedido in cardapio:
    if pedido['codigo'] == codigo:
      print("1. Prato")
      print("2. Quantidade")
      print("3. Valor total")
      opcao = input("Escolha uma opção para atualizar: ")
      if opcao == "1":
        novo_prato = input("Digite o novo prato: ").strip()
        pedido['prato'] = novo_prato
        print("✔ Prato atualizado com sucesso!")
        return
      elif opcao == "2":
        nova_quantidade = input("Digite a nova quantidade: ").strip()
        pedido['quantidade'] = nova_quantidade
        print("✔ Quantidade atualizada com sucesso!")
        return
      elif opcao == "3":
        novo_valor_total = input("Digite o novo valor total: ").strip()
        pedido['valor_total'] = novo_valor_total
        print("✔ Valor total atualizado com sucesso!")
        return

## Delete pedido

def delete_pedido():
    print("\n=== REMOVER PEDIDO ===")
    codigo = input("Digite o código do pedido para remover: ").strip()
    cardapio = 0
    for pedido in cardapio:
        if pedido['codigo'] == codigo:
            cardapio.remove(pedido)
            print("Pedido removido com sucesso!")
            return
    print("Código não encontrado.")

## Banco de dados

def database():
  conn = sqlite3.connect('crud/collab_notebooks/database/database.db')
  cursor = conn.cursor()
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS pedidos (
          codigo INTEGER PRIMARY KEY AUTOINCREMENT,
          cliente TEXT,
          prato TEXT,
          quantidade INTEGER,
          valor_total REAL
      )
  ''')
  conn.commit()
  conn.close()

database()