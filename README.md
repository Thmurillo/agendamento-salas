# Agendamento de Salas

Este sistema, desenvolvido em Python utilizando FastAPI e PostgreSQL, permite o agendamento de salas em um ambiente institucional.

## Requisitos

- Python 3.12 instalado
- PostgreSQL instalado e em execução localmente (porta padrão: 5432)
- Git instalado

## Passo a Passo para Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Thmurillo/agendamento-salas.git
   ```

   *ou baixe a pasta `projeto_api`.*

2. **Acesse a pasta do projeto:**

   ```bash
   cd caminho/para/projeto_api
   ```

3. **Crie o ambiente virtual (dentro da pasta `projeto_api`):**

   ```bash
   python3 -m venv venv
   ```

4. **Ative o ambiente virtual:**

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

5. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Configurando o Banco de Dados

6. **Crie o banco de dados:**

   - **Opção 1 - Via terminal:**

     Abra o terminal e execute:

     ```bash
     psql -U postgres -h localhost -p 5432 -c "CREATE DATABASE agendamento_salas;"
     ```

     *(Substitua `postgres` pelo seu usuário do PostgreSQL, se for diferente.)*

   - **Opção 2 - Via SQL Shell (psql):**

     Abra o programa SQL Shell (psql).

     Pressione Enter para todas as opções até chegar no prompt.

     Digite:

     ```sql
     CREATE DATABASE agendamento_salas;
     ```

7. **Crie as tabelas do banco de dados:**

   Com o banco criado, execute o script que está na pasta `projeto_api`:

   ```bash
   psql -U postgres -d agendamento_salas -f schema.sql
   ```

   *(Substitua `postgres` se seu usuário for diferente.)*
   
   Ou execute o scrip do arquivo schema.sql diretamente no PostgreSQL

## Variável de Ambiente

8. **Crie um arquivo chamado `.env` dentro da pasta `projeto_api`:**

   Utilize um editor de texto para criar o arquivo com o nome exato `.env` (sem nome antes do ponto) e adicione o seguinte conteúdo:

   ```ini
   DATABASE_URL=postgresql+asyncpg://postgres@localhost:5432/agendamento_salas
   ```

   *(Substitua `postgres` após `//` pelo seu usuário do PostgreSQL, se for diferente.)*

   Se seu PostgreSQL tiver senha ou usuário diferente:

   ```ini
   DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/agendamento_salas
   ```

## Executando o Servidor FastAPI

9. **Inicie o servidor FastAPI:**

   Com o ambiente virtual ativado e dentro da pasta `projeto_api`, execute:

   ```bash
   uvicorn main:app --reload
   ```

   O servidor iniciará em:

   ```
   http://127.0.0.1:8000
   ```

10. **Acesse a documentação interativa da API:**

    Abra no navegador:

    ```
    http://127.0.0.1:8000/docs
    ```

    O sistema estará em execução local e você pode testar todos os endpoints pela documentação gerada automaticamente pelo Swagger UI.

11. **Para uso no Postman:**

    Consulte o arquivo `.pdf` intitulado "Manual de uso API agendamento salas" para obter instruções detalhadas.

Qualquer problema, consulte este README novamente ou entre em contato pelo email [thmurillo@hotmail.com].

Desenvolvido por Thales Murillo.

Bons testes! ✨
