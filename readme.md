<div align="center">

💰 Finance Dashboard Backend

Enterprise-Grade Financial Data Management & RBAC System

A robust backend architecture engineered for high-security financial tracking, featuring advanced Role-Based Access Control (RBAC) and real-time data aggregation.

Explore Docs • Report Bug • Request Feature

</div>

💎 Key Highlights

🔒 Advanced RBAC

Granular security guards enforcing permissions for ADMIN, ANALYST, and VIEWER.

📈 Real-time Analytics

High-performance server-side calculation of Net Balance and Category totals.

🛠️ Full CRUD Lifecycle

Secure management of entries with strict ownership validation.

☁️ Cloud Native

Built for PostgreSQL (Neon.tech) with SSL-secured connection pooling.

🛡️ Data Integrity

Pydantic-powered "Fail-Fast" validation for zero database corruption.

🏗️ System Architecture

The project implements a Clean Modular Pattern to ensure separation of concerns and enterprise-level maintainability.

finance_backend/
├── 📂 src/
│   ├── 📜 main.py        # API Routes & Security Guards
│   ├── 📜 models.py      # SQLAlchemy Database Blueprints
│   ├── 📜 schemas.py     # Pydantic Data Validation Models
│   └── 📜 database.py    # Session Management & Engine Config
├── 📜 .env               # Environment Secrets (DO NOT COMMIT)
└── 📜 requirements.txt   # Global Dependencies


🛡️ Role & Permission Matrix

The system enforces strict Horizontal Authorization to prevent unauthorized data exposure.

Action

Admin

Analyst

Viewer

View Personal Dashboard

✅

✅

✅

Access Global Insights

✅

❌

❌

Record Creation

✅

✅ (Own)

❌

Record Modification

✅

❌

❌

User Status Management

✅

❌

❌

🚀 Deployment & Installation

1️⃣ Clone & Initialize

git clone [https://github.com/your-username/finance-backend.git](https://github.com/your-username/finance-backend.git)
cd finance-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


2️⃣ Dependency Injection

pip install -r requirements.txt


3️⃣ Environment Configuration

Create a .env file in the root folder:

DATABASE_URL=postgresql://user:password@host:port/dbname?sslmode=require


4️⃣ Launch the Engine

uvicorn src.main:app --reload


[!TIP]
Navigate to http://localhost:8000/docs to access the Interactive Swagger UI.

🧪 Testing the Security Simulator

This backend uses a custom x-user-id header to simulate authenticated sessions without the overhead of complex OAuth flows during development.

Identity: Pass a valid User ID in the x-user-id header.

Validation: The require_role guard fetches the user from the DB and checks their role and is_active status.

Enforcement: If the user lacks permission for the specific endpoint, a 403 Forbidden response is triggered.

💡 Engineering Excellence

DRY Logic: Reusable dependencies for role verification across all routes.

Aggregated Summaries: Using SQL SUM() and GROUP BY to offload heavy calculations from Python to the Database layer.

Fail-Fast Architecture: Leveraging Pydantic to block malformed requests before they touch the business logic.

<div align="center">

Developed with ❤️ by Purab Singla

Full Stack Developer | Backend Architect

</div>
