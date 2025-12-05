## DJLPT: uma proposta de CRUD básica

Bem-vindo ao **Sistema Codename DJLPT**, esse projeto busca facilitar a logística de pedidos para restaurantes, nesse cenário e simulado um restaurante que fornece pratos feito(PF) ou massas.

---

## Missão 
Diminuir frustração constante no resgistro de pedidos que geram atrasos no mesmo.  

---

## Funcionamento do Sistema (CRUD)

- **Cadastrar pedidos**: Nome do cliente, prato/massas, quantidade e valor total.    
- **Listar pedidos**: Visualiza todos os pedidos feitos.  
- **Buscar pedidos**: Identifica pedidos pelo número identificador.
- **Atualizar pedidos**: Altera informações de pratos, quantidade ou valor.
- **Verificar rendimento**: Mostra o lucro bruto dos pedidos cadastrados.  
- **Excluir pedidos**: Remover pedidos da mémoria.  

Tabela principal: `pedidos (cliente, prato, quantidade, valor_total)`

---

## Cenário de Uso
Imagine o cliente **Ronaldo Fernandes** chegando em um Restaurante chamado CONN:
1. Ele pede uma prato de filé com fritas.  
2. O atendente registra no sistema:  
   - Cliente: Ronaldo Fernandes  
   - Prato: Filé com fritas  
   - Quantidade: 1  
   - Valor Total: R$ 45,00  
3. O pedido é salvo na memória e aparece na lista de pedidos ativos.  
4. Após o preparo, o cliente recebe seu pedido e o atendente remove do sistema, é assim concluído.  

---
