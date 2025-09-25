# 📅 Agenda Digital - Backend

Este é o backend do projeto **Agenda Digital**, responsável pela API de usuários, autenticação e integração com banco de dados PostgreSQL (Supabase).

Frontend disponível em: [Agenda Digital Frontend](https://github.com/rqueiroz979/agenda-digital-frontend)

---

## 🚀 Tecnologias utilizadas
- Python 3.13
- Flask 3.x
- Flask-SQLAlchemy
- Flask-Migrate (migrations)
- PostgreSQL (Supabase)
- Render (deploy backend)
- Netlify (deploy frontend)

---

## 📂 Estrutura principal
```
agenda-digital-backend/
├── src/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models/          # Modelos do banco de dados
│   ├── routes/          # Rotas da API
│   ├── config.py        # Configurações (carrega DATABASE_URL do Render)
│   └── __init__.py
├── requirements.txt     # Dependências
├── DOCUMENTACAO_GERAL.md # Documentação completa do projeto
└── README.md            # Este arquivo (resumo)
```

---

## ⚙️ Configuração de Ambiente

### 🔑 Variáveis de ambiente necessárias
No **Render**:
- `DATABASE_URL` → string de conexão do Supabase  
  Exemplo:  
  ```
  postgresql://postgres.stgphknybtgcdulqfgcb:SENHA@aws-1-sa-east-1.pooler.supabase.com:6543/postgres
  ```
- `SECRET_KEY` → chave secreta para JWT

---

## ▶️ Como rodar no Render
O Render já está configurado para:
```bash
gunicorn src.main:app
```

---

## 🛠 Endpoints principais

### Health Check
```
GET /health
Response: { "status": "ok" }
```

### Criar usuário
```
POST /api/usuarios/
{
  "nome": "Ramon",
  "email": "ramon@email.com",
  "senha": "123456"
}
```

### Login
```
POST /api/login/
{
  "email": "ramon@email.com",
  "senha": "123456"
}
```

### Listar usuários (exemplo protegido)
```
GET /api/usuarios/
Authorization: Bearer <TOKEN>
```

---

## 📖 Documentação Completa
Para detalhes do histórico, decisões técnicas e estrutura completa, veja:  
👉 [DOCUMENTACAO_GERAL.md](./DOCUMENTACAO_GERAL.md)
