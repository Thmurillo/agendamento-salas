Agendamento de Salas

Sistema desenvolvido em Python com FastAPI e PostgreSQL para agendamento de salas em um ambiente institucional.

Requisitos

Python 3.12 instalado

PostgreSQL instalado e rodando localmente (porta padrão: 5432)

Git instalado

Passo a passo para executar o projeto

1- Clone o repositório
git clone https://github.com/Thmurillo/agendamento-salas.git ou baixe a pasta projeto_api

2. Acesse a pasta do projeto
cd endereço/projeto_api

3. Crie o ambiente virtual (dentro da pasta projeto_api)
python3 -m venv venv

4. Ative o ambiente virtual
No macOS/Linux:

source venv/bin/activate

No Windows:

venv\Scripts\activate

5. Instale as dependências
pip install -r requirements.txt

Configurando o banco de dados

6. Crie o banco de dados
Opção 1 - Via terminal:

Abra o terminal e execute:

psql -U postgres -h localhost -p 5432 -c "CREATE DATABASE agendamento_salas;"

(Substitua postgres pelo seu usuário do PostgreSQL, se for diferente)

Opção 2 - Via SQL Shell (psql):

Abra o programa SQL Shell (psql)

Pressione Enter para todas as opções até chegar no prompt

Digite:

CREATE DATABASE agendamento_salas;

7. Crie as tabelas do banco de dados
Com o banco criado, execute o script que está na pasta projeto_api:

psql -U postgres -d agendamento_salas -f schema.sql

(Substitua postgres se seu usuário for diferente)

Variável de ambiente

8. Crie um arquivo chamado .env dentro da pasta projeto_api Para criação pode-se usar um editor
Crie o arquivo com o nome exato .env (sem nome antes do ponto) e adicione o seguinte:

Altere os dados conforme sua instalação local:

DATABASE_URL=postgresql+asyncpg://postgres@localhost:5432/agendamento_salas (Substitua postgres(depois do"//") pelo seu usuário do PostgreSQL, se for diferente)

Se seu PostgreSQL tiver senha ou usuário diferente:

DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/agendamento_salas

9. Rode o servidor FastAPI
Estando com o ambiente virtual ativado e dentro da pasta projeto_api:

uvicorn main:app --reload

O servidor iniciará em:

http://127.0.0.1:8000

10. Acesse a documentação interativa da API:
Abra no navegador:

http://127.0.0.1:8000/docs

Pronto!

O sistema estará em execução local e você pode testar todos os endpoints pela documentação gerada automaticamente pelo Swagger UI.

11. Para uso em postman acesse o arquivo .pdf "Manual de uso API agendamento salas"

Qualquer problema, consulte o README novamente ou entre em contato pelo email thmurillo@hotmail.com.

Desenvolvido por Thales Murillo

Bons testes! ✨
