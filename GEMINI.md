# GEMINI.md

## 🚀 Project Overview

This project is the **Ushipp Operations Command Center (OCC)**, a headless logistics engine for the University Shipping company. It's designed to automate and optimize long-haul university moving operations, replacing manual processes with a modern, cloud-native solution.

The system handles everything from order ingestion and vehicle routing to driver dispatch and real-time customer visibility, providing an "Amazon-like" experience for students.

### Key Features:

- **Automated Order Ingestion:** A webhook bridge to ingest and process orders from the legacy Wix platform.
- **Algorithmic Routing:** Utilizes Google OR-Tools to solve the Vehicle Routing Problem (VRP) with capacity and time-window constraints.
- **Real-Time Customer Visibility:** A "pizza tracker" style experience for customers to track their shipments in real-time.
- **Hybrid Mobile App:** A cross-platform mobile app for drivers to manage their routes, track their location, and upload proof of delivery.

## 🏗️ Technical Architecture

The project follows a hybrid cloud architecture, leveraging the strengths of different platforms for different components.

| Component | Technology | Hosting | Role |
| --- | --- | --- | --- |
| **Frontend** | Next.js + Tailwind CSS | Vercel | Admin Dashboard & Customer Tracker |
| **Backend** | Python FastAPI | AWS ECS (Fargate) | Core Logic, Webhooks, & Routing |
| **Database** | PostgreSQL + PostGIS | AWS RDS | Geospatial Data & Persistence |
| **Caching** | Redis | AWS ElastiCache | Live GPS State & Session Management |
| **Mobile** | React + Capacitor | App Store | Driver Companion App (iOS/Android) |

### Monorepo Structure

The project is organized as a monorepo to manage the different services in a single repository.

```
/ushipp-occ
├── /apps
│   ├── /web           # Next.js (Admin Console & Customer Tracker)
│   ├── /api           # Python FastAPI (Backend Logic)
│   └── /driver        # Next.js + Capacitor (Mobile Wrapper)
├── /packages
│   ├── /db-types      # Shared Types (TypeScript Interfaces)
│   └── /config        # Shared Constants
└── .github            # CI/CD Pipelines
```

## 🚀 Getting Started (Local Development)

### Prerequisites

- Node.js (LTS) & npm
- Python 3.10+
- Docker (Optional)
- Supabase Account (for local Dev DB)

### 1. Clone & Setup

```bash
git clone <repository-url>
cd ushipp-occ
npm install
```

### 2. Database Setup

1. Create a project on [Supabase](https://supabase.com/).
2. Run the schema script located in `/infrastructure/database_schema.sql` in the Supabase SQL Editor.
3. Get your **Connection String (URI)**.

### 3. Backend Setup (Python)

```bash
cd apps/api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Add your DATABASE_URL here
uvicorn main:app --reload
```

> API will be live at http://localhost:8000.

### 4. Frontend Setup (Next.js)

```bash
cd apps/web
cp .env.example .env.local  # Add NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev
```

> Dashboard will be live at http://localhost:3000.
