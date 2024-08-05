## Sobre o desafio

Proposto pelo meu mentor, [Jonh Sousa](https://www.linkedin.com/in/jonhsousa/), para ajudar no desenvolvimento de habilidades técnicas com bancos NoSQL e FastAPI. Além disso, visa aprimorar minha capacidade de organização em projetos, focando primeiro no essencial e depois no que é possível desenvolver.

## Sobre o projeto

O projeto consiste em uma aplicação backend que utiliza APIs para criar e gerenciar objetivos pensados na metodologia S.M.A.R.T. no banco de dados MongoDB.
### O que é S.M.A.R.T.?
- A metodologia S.M.A.R.T. é uma técnica de definição de objetivos que garante clareza e alcançabilidade. Ela promove a criação de metas bem estruturadas, focadas em resultados específicos e mensuráveis, que são realistas e relevantes, com prazos definidos. Isso facilita o planejamento e a execução eficazes, melhorando a produtividade e garantindo o cumprimento dos objetivos.
- S: Específicos (claramente definidos)
- M: Mensuráveis (quantificáveis para avaliar o progresso)
- A: Alcançáveis (realistas e possíveis de alcançar)
- R: Relevantes (importantes e alinhados com outros objetivos)
- T: Temporais (com um prazo definido para conclusão)

## Passo a passo para rodar o projeto
### 1. Instalar Dependências
- Baixe e instale o MongoDB e o NoSQLBooster no seu computador a partir de seus sites oficiais.

### 2. Clonar o Repositório
- Clone o código em uma pasta local:
    ```
    git clone https://github.com/kauesv/SMARTify.git
    ```

### 3. Criar Ambiente Virtual
- Crie um ambiente virtual (Windows):
    ```
    py -m venv venv
    ```

### 4. Ativar Ambiente Virtual
- Ative o ambiente virtual (Windows):
    ```
    venv\Scripts\Activate
    ```

### 5. Instalar Dependências do Projeto
- Instale usando o arquivo requirements:
    ```
    pip install -r requirements.txt 
    ```

### 6. Iniciar o Servidor
- Suba o servidor com Uvicorn:
    ```
    uvicorn main:app --reload
    ```

### 7. Configurar MongoDB
- Configure o MongoDB:
    - Acesse o NoSQLBooster.
    - Vá até a pasta documentacoes/mongodb, copie os scripts de criação das coleções de usuários e smart, e execute-os no NoSQLBooster.

### 8. Teste das APIs
- Use o arquivo de documentação da API:
    - Encontre o arquivo na pasta documentacoes/api.
    - Importe-o no Postman para testar as rotas da API.
- Ou use o docs do próprio FastAPI:
    - localhost:8000/docs/

## Contato

Para mais informações ou para discutir qualquer um dos repositórios, sinta-se à vontade para entrar em contato:

- **Email:** [kauesousavieira534@gmail.com](mailto:kauesousavieira534@gmail.com)
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/kaue-sousa-vieira/)

---
Obrigado por visitar meu repositório!
