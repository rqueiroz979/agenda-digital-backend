# Agenda Digital - Backend

Este é o repositório do backend da aplicação Agenda Digital, desenvolvido com Flask.

## Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd agenda-digital-backend
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    DATABASE_URL=postgresql://user:password@host:port/database_name
    SECRET_KEY=sua_chave_secreta_para_jwt
    JWT_EXP_HOURS=8
    ALLOWED_ORIGINS=http://localhost:5173,https://seu-frontend.netlify.app
    EXTERNAL_API_TIMEOUT=8
    ```
    - `DATABASE_URL`: String de conexão com o banco de dados PostgreSQL (ex: Supabase).
    - `SECRET_KEY`: Chave secreta para a assinatura de tokens JWT.
    - `JWT_EXP_HOURS`: Tempo de expiração do token JWT em horas.
    - `ALLOWED_ORIGINS`: Origens permitidas para CORS, separadas por vírgula.

5.  **Inicialize e aplique as migrações do banco de dados:**
    Certifique-se de que o banco de dados esteja vazio ou que as tabelas `clientes` e `usuarios` não existam, caso contrário, você pode enfrentar erros de tipo de coluna.
    ```bash
    export FLASK_APP=src/__init__.py
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

## Execução da Aplicação

Para iniciar o servidor Flask:

```bash
export FLASK_APP=src/__init__.py
flask run --port 5000
```

O backend estará disponível em `http://localhost:5000`.
