### FreshFunds - Gerenciador Financeiro para Hortifrutis

---

![FreshFunds](freshfunds_logo.png)

---

## Sobre o FreshFunds

O **FreshFunds** é uma solução de gerenciamento de inventário e vendas, projetada inicialmente para o setor de hortifruti com a visão de expandir para mercados e outros segmentos. Nosso objetivo é fornecer uma ferramenta eficiente e intuitiva para ajudar negócios a gerenciar suas finanças e operações com precisão e facilidade.

## Funcionalidades

### Gestão de Vendas e Despesas
- **Registro de Vendas**: Acompanhe todas as transações de vendas em tempo real.
- **Controle de Despesas**: Registre e categorize despesas para melhor controle financeiro.
- **Relatórios Detalhados**: Gere relatórios financeiros detalhados para análise de desempenho.

### Gestão de Estoque
- **Controle de Inventário**: Monitore seu estoque com precisão, garantindo que você nunca fique sem produtos.
- **Alertas de Baixa de Estoque**: Receba notificações quando os níveis de estoque estiverem baixos.

### Interface Intuitiva
- **Dashboard Interativo**: Visualize rapidamente o estado financeiro do seu negócio.
- **Interface Amigável**: Design simples e intuitivo para facilitar o uso diário.

### Segurança e Confiabilidade
- **Backup Automático**: Suas informações sempre seguras com backups automáticos.
- **Segurança de Dados**: Proteção robusta para garantir a privacidade e integridade dos seus dados.

## Tecnologias Utilizadas

- **Python**: Backend robusto e eficiente.
- **PySimpleGUI**: Interface gráfica intuitiva e fácil de usar.
- **MySQL**: Banco de dados relacional para armazenamento seguro e eficiente de dados.

## Índice

- [Ambiente de Desenvolvimento](#ambiente-de-desenvolvimento)
- [Fases do Projeto](#fases-do-projeto)
    - [Fase 1: Configuração do Banco de Dados](#fase-1-configuração-do-banco-de-dados)
    - [Fase 2: Desenvolvimento do Backend](#fase-2-desenvolvimento-do-backend)
    - [Fase 3: Desenvolvimento da Interface de Usuário](#fase-3-desenvolvimento-da-interface-de-usuário)
- [Implantação](#implantação)
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

#### Etapas:

1. **Configurar Ambiente**:
   - Instalar Python e bibliotecas necessárias (ex: conector MySQL).

2. **Camada de Acesso aos Dados (DAO)**:
   - Criar classes Python para interagir com o banco de dados.
   - Implementar operações CRUD para cada entidade.

3. **Camada de Lógica de Negócios**:
   - Definir regras de negócios e operações (ex: compras, gerenciamento de inventário).

#### UML:

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

#### Etapas:

1. **Escolher Framework de GUI**:
   - Usar PySimpleGUI para simplicidade.

2. **Desenhar Interface**:
   - Criar wireframes para cada tela (ex: Login, Dashboard, Gerenciamento de Inventário).

3. **Implementar GUI**:
   - Desenvolver a interface usando PySimpleGUI.
   - Conectar GUI com operações de backend.

#### UML:

```plaintext
+---------------+          +----------------+          +-----------------+
|  Login GUI    |  ->      |  Dashboard GUI |  ->      | Inventory GUI   |
+---------------+          +----------------+          +-----------------+
| +login()      |          | +viewSummary() |          | +viewProducts() |
+---------------+          +----------------+          +-----------------+
```

## Implantação

### Implantação Local
- Testar a aplicação exaustivamente em uma máquina local.
- Garantir que todas as funcionalidades estejam funcionando corretamente e que o sistema esteja estável.

### Implantação na Nuvem (Etapa Futura Opcional)
- Escolher uma plataforma de nuvem (AWS, GCP, Azure).
- Configurar uma máquina virtual e um serviço de banco de dados.
- Implantar a aplicação usando Docker ou outras ferramentas relevantes.
- Configurar DNS e configurações de segurança.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para novas funcionalidades, correções de bugs ou melhorias na documentação.

## Licença

Este projeto está licenciado sob a licença MIT. 
Veja o arquivo [LICENSE](MIT_license.txt) para mais detalhes.

---

### Nota Importante

Esta aplicação está atualmente em desenvolvimento e é destinada para fins acadêmicos. Estamos trabalhando para implementar todas as funcionalidades descritas e garantir a estabilidade do sistema. Sua contribuição e feedback são valiosos para nós!

---

Feito com dedicação por [Claudio G. Vargas](https://github.com/CGVARGAS)

![GitHub Stars](https://img.shields.io/github/stars/CGVARGAS/freshfunds?style=social) ![GitHub Forks](https://img.shields.io/github/forks/CGVARGAS/freshfunds?style=social)
