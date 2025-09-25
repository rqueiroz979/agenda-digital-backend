# 📖 Documentação Geral – Agenda Digital

## 🗂 Histórico do Projeto

1. **Primeiros arquivos enviados**
   - Projeto inicialmente veio misturado (backend + frontend).
   - Reorganizado em dois repositórios:
     - `agenda-digital-backend/`
     - `agenda-digital-frontend/`

2. **Backend (Flask + PostgreSQL no Supabase)**
   - Estrutura organizada em `src/` com:
     - `main.py` → ponto de entrada da aplicação
     - `src/__init__.py` → configuração do Flask e SQLAlchemy
     - `src/extensions.py` → inicialização do banco e migrações
     - `src/models/` → modelos (Cliente, Usuário, etc.)
     - `src/routes/` → rotas da API (usuários, clientes, saúde do sistema)
   - Ajustes realizados:
     - Corrigidas importações quebradas (`extensions`, `models`).
     - Configuração de `gunicorn main:app` para o Render.
     - `requirements.txt` revisado (apenas pacotes necessários).
   - Deploy:
     - Criado no **Render**.
     - Configurado `DATABASE_URL` com Supabase (Pooler IPv4).
     - Endpoint `/health` testado → retornando `{"status":"ok"}` ✅.

3. **Banco de Dados (Supabase)**
   - Projeto criado no Supabase (região São Paulo).
   - Usado **Transaction Pooler** para compatibilidade IPv4.
   - `DATABASE_URL` configurado no Render.
   - Senhas revisadas para evitar caracteres que quebrem a string de conexão.

4. **Frontend (React no Netlify)**
   - Código separado no repositório `agenda-digital-frontend`.
   - Deploy inicial no **Netlify** (pendente ajuste de integração com backend).
   - Estrutura organizada com páginas, componentes e chamadas API.

---

## ⚙️ Status Atual

- **Backend**:
  ✅ Deploy no Render funcionando
  ✅ Conexão com Supabase configurada
  ❌ Endpoints de cadastro/login ainda com erros (`500` no `POST /api/usuarios/`, `404` no `/api/login/`).

- **Frontend**:
  ✅ Repositório no GitHub separado
  ✅ Deploy inicial no Netlify
  ❌ Integração com backend pendente

- **Banco de Dados (Supabase)**:
  ✅ Conexão criada e configurada
  ❌ Migrations ainda não aplicadas (`flask db migrate`, `flask db upgrade`).

---

## 🔜 Próximos Passos

1. **Backend**
   - Aplicar migrations para criar tabelas no Supabase.
   - Revisar e corrigir rotas `/api/usuarios/` e `/api/login/`.

2. **Frontend**
   - Configurar variáveis no Netlify:
     ```env
     REACT_APP_API_URL=https://agenda-digital-backend.onrender.com
     ```
   - Testar integração de páginas com a API.

3. **Documentação**
   - Manter este documento atualizado no repositório.
   - Atualizar READMEs do backend e frontend para explicar execução e deploy.

---

📌 Documento criado em **25/09/2025** e deve ser atualizado conforme evolução do projeto.
