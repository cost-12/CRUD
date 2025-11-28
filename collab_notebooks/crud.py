import sqlite3

# Função para criar o banco e tabela
def database():
    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            prato TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            valor_total REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para cadastrar pedido
def creat_pedido():
    print("\n=== CADASTRAR PEDIDO ===")
    cliente = input("Digite o nome do cliente: ").strip()
    prato = input("Digite o prato: ").strip()
    quantidade = int(input("Digite a quantidade: ").strip())
    valor_total = float(input("Digite o valor total: ").strip())

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (cliente, prato, quantidade, valor_total)
        VALUES (?, ?, ?, ?)
    ''', (cliente, prato, quantidade, valor_total))
    conn.commit()
    conn.close()
    print("Pedido cadastrado com sucesso!!!")

# Função para listar pedidos
def list_pedidos():
    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()

    for linhas in pedidos:
      print(linhas)

    conn.close()

# Função para buscar pedido
def search_pedido():
    print("\n=== BUSCAR PEDIDO ===")
    codigo = input("Digite o código do pedido: ").strip()

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos WHERE codigo = ?", (codigo,))
    pedido = cursor.fetchone()
    conn.close()

    if pedido:
        print(f"\nPedido encontrado!\nCódigo: {pedido[0]} | Cliente: {pedido[1]} | Prato: {pedido[2]} | Quantidade: {pedido[3]} | Valor total: R$ {pedido[4]:.2f}")
    else:
        print("Pedido não encontrado.")

# Função para atualizar pedido
def update_pedido():
    print("\n=== ATUALIZAR PEDIDO ===")
    codigo = input("Digite o código do pedido para atualizar: ").strip()

    print("1. Prato\n2. Quantidade\n3. Valor total")
    opcao = input("Escolha uma opção para atualizar: ")

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()

    if opcao == "1":
        novo_prato = input("Digite o novo prato: ").strip()
        cursor.execute("UPDATE pedidos SET prato = ? WHERE codigo = ?", (novo_prato, codigo))
    elif opcao == "2":
        nova_quantidade = int(input("Digite a nova quantidade: ").strip())
        cursor.execute("UPDATE pedidos SET quantidade = ? WHERE codigo = ?", (nova_quantidade, codigo))
    elif opcao == "3":
        novo_valor = float(input("Digite o novo valor total: ").strip())
        cursor.execute("UPDATE pedidos SET valor_total = ? WHERE codigo = ?", (novo_valor, codigo))
    else:
        print("Opção inválida!")
        conn.close()
        return

    conn.commit()
    conn.close()
    print("Pedido atualizado com sucesso!!!")

# Função para remover pedido
def delete_pedido():
    print("\n=== REMOVER PEDIDO ===")
    codigo = input("Digite o código do pedido para remover: ").strip()

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()
    print("Pedido removido com sucesso!!!")

# Função Menu
def menu():
    database()  # garante que a tabela existe
    while True:
        print("\n===== SISTEMA CONN =====")
        print("1 - Cadastrar pedido")
        print("2 - Listar pedidos")
        print("3 - Buscar pedido")
        print("4 - Atualizar pedido")
        print("5 - Remover pedido")
        print("0 - Sair")

        options = input("Escolha uma opção: ")

        if options == "1":
            creat_pedido()
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

menu()
