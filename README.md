
# Simulador de Caixa Eletrônico

Este projeto é uma simulação de um sistema de caixa eletrônico (ATM) com as funcionalidades de **depósito**, **saque** e **extrato**. O sistema permite a criação de contas e usuários, além de manter um histórico de transações realizadas.

## Funcionalidades

O sistema inclui as seguintes operações:

- **Depósito**: Realiza depósitos em contas de clientes.
- **Saque**: Permite a realização de saques, com controle de limite de saques diários e valor máximo por saque.
- **Extrato**: Gera o extrato de transações de uma conta, podendo ser completo ou filtrado por depósitos ou saques.
- **Criação de nova conta**: Cria novas contas correntes associadas a clientes.
- **Listagem de contas**: Lista todas as contas cadastradas.
- **Criação de novo usuário**: Adiciona novos clientes ao sistema.

## Estrutura do Código

### Classes Principais

- **Cliente**: Classe base para representar os clientes. Clientes podem realizar transações e ter uma ou mais contas associadas.
- **PessoaFisica**: Subclasse de `Cliente`, representa um cliente do tipo pessoa física, contendo informações como nome, CPF e data de nascimento.
- **Conta**: Representa uma conta bancária, contendo operações como saque, depósito e acesso ao histórico de transações.
- **ContaCorrente**: Subclasse de `Conta`, com limites de saque e quantidade de saques diários.
- **Transacao**: Classe abstrata para representar uma transação. Suas subclasses são:
  - **Deposito**: Realiza a operação de depósito.
  - **Saque**: Realiza a operação de saque.
- **Historico**: Armazena as transações realizadas em uma conta e permite gerar relatórios de extrato.

### Funcionalidades Extras

- **Iterador de Contas**: Classe `ContaIterador` permite iterar sobre as contas registradas.
- **Limite de Transações**: O sistema impõe um limite de 10 transações diárias por conta.
- **Log de Transações**: Decoração `@log_transacao` para registrar e imprimir no console quando transações são realizadas.

## Requisitos do Sistema

- **Python 3.8+**
- **Bibliotecas nativas**: Não há dependências externas.

## Como Executar

1. Clone este repositório para sua máquina:
   ```bash
   git clone https://github.com/seu_usuario/simulador-caixa-eletronico.git
   cd simulador-caixa-eletronico
   ```

2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

3. Siga o menu interativo para realizar as operações disponíveis.

## Menu Principal

Ao iniciar o sistema, você verá o seguinte menu interativo:

```
-------------- MENU ---------------
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
=> 
```

### Exemplos de Operações:

- **Depósito**: Escolha a opção `[d]` e insira o CPF do cliente e o valor a ser depositado.
- **Saque**: Escolha a opção `[s]`, informe o CPF e o valor a ser sacado.
- **Extrato**: Escolha `[e]` e visualize o histórico de transações (depósitos, saques ou completo).

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório
2. Crie uma branch para sua funcionalidade (`git checkout -b minha-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Envie para o repositório (`git push origin minha-funcionalidade`)
5. Crie um Pull Request
