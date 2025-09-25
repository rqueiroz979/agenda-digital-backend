# Agenda Digital - Backend (Final Package)

This is the final backend package prepared to run on **Render** and use **Supabase (Postgres)** as database.

## Quick overview
- Flask application using Application Factory pattern.
- SQLAlchemy models for users and clients.
- JWT-based authentication (PyJWT).
- Flask-Migrate (Alembic) for database migrations.
- Seed script to create an admin user.

## Deploy (Render)
1. Push this repository to GitHub.
2. Create a new Web Service on Render linking this repo.
3. Add the following Environment Variables on Render:
   - DATABASE_URL (Supabase connection string)
   - SECRET_KEY
   - JWT_EXP_HOURS (optional, default 8)
4. Build Command:
   ```
   pip install -r requirements.txt && flask db upgrade
   ```
5. Start Command:
   ```
   gunicorn main:app
   ```
6. After deploy finishes, open **Shell** on Render and run:
   ```
   python seed.py
   ```
   This will create an admin user:
   - email: admin@empresa.com
   - senha: 123456

## API Endpoints (base path /api)
- `POST /api/usuarios/` - create user
- `POST /api/usuarios/login` - login -> returns JWT
- `GET /api/clientes/` - list clients (requires Authorization: Bearer <token>)
- `POST /api/clientes/` - create client (requires token)
- `GET /api/clientes/<id>` - get client
- `PUT /api/clientes/<id>` - update client
- `DELETE /api/clientes/<id>` - delete client

## Notes
- Do not commit `.env` with secrets.
- For frontend (Netlify), set `VITE_API_URL` to `https://<your-render-url>/api`.
