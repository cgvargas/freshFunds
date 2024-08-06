# FreshFunds

**FreshFunds** é um sistema de gerenciamento de inventário e vendas que permite a administração eficiente de produtos, fornecedores, transações e usuários. O projeto se baseia em uma arquitetura de Backend com Python e um banco de dados MySQL.

## Índice

- [Ambiente de Desenvolvimento](#ambiente-de-desenvolvimento)
- [Fases do Projeto](#fases-do-projeto)
    - [Fase 1: Configuração do Banco de Dados](#fase-1-configuração-do-banco-de-dados)
    - [Fase 2: Desenvolvimento do Backend](#fase-2-desenvolvimento-do-backend)
    - [Fase 3: Desenvolvimento da Interface de Usuário](#fase-3-desenvolvimento-da-interface-de-usuário)
- [Implantação](#implantação)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Ambiente de Desenvolvimento

- **Desenvolvimento Local**
  - **Plataforma**: Windows
  - **Ferramentas**: IDE local (ex: PyCharm, Visual Studio Code), MySQL Workbench

## Fases do Projeto

### Fase 1: Configuração do Banco de Dados

#### Etapas:
1. **Desenhar o Esquema do Banco de Dados**:
   - Definir tabelas, campos e relacionamentos.
   - Exemplos de tabelas: Produtos, Fornecedores, Transações, Usuários.

2. **Criar Tabelas**:
   - Usar MySQL para criar tabelas com base no esquema.
   - Inserir dados de exemplo para testes.

#### UML:

```plaintext
+----------------+         +----------------+
|    Produtos    |         | Fornecedores   |
+----------------+         +----------------+
| ProductID (PK) |         | SupplierID (PK)|
| Nome           |         | Nome           |
| Preço          |         | Contato        |
+----------------+         +----------------+

+--------------------+         +--------------+
|   Transações       |         |    Usuários  |
+--------------------+         +--------------+
| TransactionID (PK) |         | UserID (PK)  |
| ProductID (FK)     |         | Username     |
| Quantidade         |         | Senha        |
| Data               |         | Função       |
+--------------------+         +--------------+
```
### Fase 2: Desenvolvimento do Backend

**Etapas:**
Configurar Ambiente:

Instalar Python e bibliotecas necessárias (ex: conector MySQL).
Camada de Acesso aos Dados (DAO):

Criar classes Python para interagir com o banco de dados.
Implementar operações CRUD para cada entidade.
Camada de Lógica de Negócios:

Definir regras de negócios e operações (ex: compras, gerenciamento de inventário).
### UML:
```plaintext
+-----------------+         +------------------+
|   ProductDAO    |         | SupplierDAO      |
+-----------------+         +------------------+
| +addProduct()   |         | +addSupplier()   |
| +getProduct()   |         | +getSupplier()   |
| +updateProduct()|         | +updateSupplier()|
| +deleteProduct()|         | +deleteSupplier()|
+-----------------+         +------------------+

+---------------------+         +--------------+
| TransactionDAO      |         |   UserDAO    |
+---------------------+         +--------------+
| +addTransaction()   |         | +addUser()   |
| +getTransaction()   |         | +getUser()   |
| +updateTransaction()|         | +updateUser()|
| +deleteTransaction()|         | +deleteUser()|
+---------------------+         +--------------+
```

### Fase 3: Desenvolvimento da Interface de Usuário

**Etapas:**
Escolher Framework de GUI:

Usar PySimpleGUI para simplicidade.
Desenhar Interface:

Criar wireframes para cada tela (ex: Login, Dashboard, Gerenciamento de Inventário).
Implementar GUI:

Desenvolver a interface usando PySimpleGUI.
Conectar GUI com operações de backend.
### UML:

```plaintext
+---------------+          +----------------+          +-----------------+
|  Login GUI    |  ->      |  Dashboard GUI |  ->      | Inventory GUI   |
+---------------+          +----------------+          +-----------------+
| +login()      |          | +viewSummary() |          | +viewProducts() |
+---------------+          +----------------+          +-----------------+
```

# Implantação:

### Implantação Local
Testar a aplicação exaustivamente em uma máquina local.
Garantir que todas as funcionalidades estejam funcionando corretamente e que o sistema esteja estável.

### Implantação na Nuvem (Etapa Futura Opcional)
Escolher uma plataforma de nuvem (AWS, GCP, Azure).
Configurar uma máquina virtual e um serviço de banco de dados.

### Implantar a aplicação usando Docker ou outras ferramentas relevantes.

Configurar DNS e configurações de segurança.
- Tecnologias Utilizadas
- Linguagens: Python
- Banco de Dados: MySQL
- Framework de GUI: PySimpleGUI
- IDE: PyCharm, Visual Studio Code

**Contribuição:**
Sinta-se à vontade para contribuir com o projeto! Se você desejar colaborar, por favor, crie um pull request ou abra uma issue para discutir suas ideias.

**Licença:**
Este projeto está licenciado sob a `MIT License`.
