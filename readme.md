# ███████╗██╗███╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗
# ██╔════╝██║████╗  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝
# █████╗  ██║██╔██╗ ██║███████║██╔██╗ ██║██║     █████╗
# ██╔══╝  ██║██║╚██╗██║██╔══██║██║╚██╗██║██║     ██╔══╝
# ██║     ██║██║ ╚████║██║  ██║██║ ╚████║╚██████╗███████╗
# ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝

# ==============================================
# FINANCE DASHBOARD BACKEND
# ==============================================

# secure | scalable | analytics-driven backend
# built with fastapi + postgres + strict RBAC

# ----------------------------------------------
# CORE FEATURES
# ----------------------------------------------

# [RBAC]
# - ADMIN / ANALYST / VIEWER
# - strict permission enforcement
# - horizontal authorization

# [DATA ENGINE]
# - real-time balance calculation
# - category aggregation (SQL optimized)
# - zero redundant computation in python

# [SECURITY]
# - ownership validation
# - role guards (dependency-based)
# - fail-fast request validation

# [CLOUD READY]
# - postgres (neon)
# - ssl enforced
# - production-friendly structure

# ----------------------------------------------
# PROJECT MAP
# ----------------------------------------------

finance_backend/
├── src/
│   ├── main.py        # api entry + guards
│   ├── models.py      # db models
│   ├── schemas.py     # validation layer
│   └── database.py    # engine + sessions
├── .env               # secrets (ignored)
└── requirements.txt

# ----------------------------------------------
# PERMISSION MATRIX
# ----------------------------------------------

# action            ADMIN   ANALYST   VIEWER
# ------------------------------------------
# dashboard          ✔       ✔        ✔
# global stats       ✔       ✘        ✘
# create record      ✔       own      ✘
# modify record      ✔       ✘        ✘
# manage users       ✔       ✘        ✘

# ----------------------------------------------
# QUICK START
# ----------------------------------------------

git clone https://github.com/your-username/finance-backend.git
cd finance-backend

python -m venv venv

# activate
source venv/bin/activate        # linux/mac
venv\Scripts\activate           # windows

pip install -r requirements.txt

# ----------------------------------------------
# ENV SETUP
# ----------------------------------------------

touch .env

DATABASE_URL=postgresql://user:password@host:port/dbname?sslmode=require

# ----------------------------------------------
# RUN
# ----------------------------------------------

uvicorn src.main:app --reload

# docs
http://localhost:8000/docs

# ----------------------------------------------
# AUTH SIMULATION (DEV MODE)
# ----------------------------------------------

# send header with request:
# x-user-id: <user_id>

# flow:
# -> fetch user from db
# -> validate role + active status
# -> allow / reject (403)

# ----------------------------------------------
# INTERNAL DESIGN
# ----------------------------------------------

# DRY architecture
# reusable role dependencies

# DB-first computation
# (SUM, GROUP BY handled in postgres)

# strict validation
# (pydantic blocks invalid payloads early)

# ----------------------------------------------
# AUTHOR
# ----------------------------------------------

# purab singla
# backend engineer

# ----------------------------------------------
# LICENSE
# ----------------------------------------------

# MIT
