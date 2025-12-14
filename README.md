# Desafio – API + Dashboard com Docker

Este projeto utiliza **Docker** e **Docker Compose** para subir um ambiente completo com:

* PostgreSQL
* PgAdmin
* API (FastAPI)
* Dashboard (Streamlit)

---

## 📌 Pré-requisitos

Antes de iniciar, certifique-se de que sua máquina possui:

* **Docker** instalado
* **Docker Compose** instalado

Verifique com:

```bash
docker --version
docker compose version
```

---

## 🐍 Ambiente virtual (ETL / carga inicial)

Para executar scripts de carga ou manipulação de dados (CSV → PostgreSQL), é necessário criar um ambiente virtual Python.

### 1️⃣ Criar o ambiente virtual

Na raiz do projeto:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# .venv\\Scripts\\activate  # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install sqlalchemy pandas psycopg2-binary
```

> 📌 O script de carga já estará disponível no diretorio script_db.

---

## 🔐 Arquivos `.env`

É necessário criar **arquivo `.env`:

* Raiz do projeto
---

---

## 📁 `.env` – **Raiz do projeto**

Crie o arquivo `.env` na raiz com as variáveis abaixo:

```env
POSTGRES_USER=<seu_usuario>
POSTGRES_PASSWORD=<sua_senha>
POSTGRES_DB=<seu_banco>
TIME_ZONE=America/Sao_Paulo

PGADMIN_EMAIL=<email_login>
PGADMIN_PASSWORD=<login>
PGADMIN_PORT=<porta_no_host>

POSTGRES_PORT=<porta_no_host>

URL_DB=postgresql+psycopg2://<seu_usuario>:<sua_senha>@postgres:5432/<seu_banco>
API_PORT=<porta_host_api>
DASH_PORT=<porta_dash_api>
```

---

## 🐳 Subindo o ambiente com Docker Compose
Clone o repositorio https://github.com/Dyego-Barros/desafio-pin-people.git
```bash
git clone https://github.com/Dyego-Barros/desafio-pin-people.git

```
Na raiz do projeto, apos criar seu arquivo .env com os valores  execute:

```bash
docker compose up -d
```

Isso irá subir:

* PostgreSQL
* PgAdmin
* API
* Dashboard

---

## 🌐 Acessos

Após os containers estarem em execução:

### 🔹 API

```text
http://localhost:<sua_porta>
```

### 🔹 Dashboard (Streamlit)

```text
http://localhost:<sua_porta>
```

### 🔹 PgAdmin

```text
http://localhost:<sua_porta>
```

---

## 🛑 Parar os containers

Para parar o ambiente:

```bash
docker compose down
```

---

## ✅ Observações finais

* A comunicação entre os serviços ocorre via **network Docker (`desafio`)**
* O hostname do banco dentro dos containers é **`postgres`**
* O uso de `.env` evita hardcode de credenciais

---

🚀 Ambiente pronto para desenvolvimento e testes.
