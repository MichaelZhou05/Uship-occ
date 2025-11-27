# README

# Ushipp Operations Command Center (OCC)

> A distributed, cloud-native logistics engine for optimizing long-haul university moving operations.
> 

## 📋 Project Overview

**Ushipp OCC** is a headless operations platform built for University Shipping (Ushipp). It serves as the "Nerve Center" for the business, sitting downstream from the marketing website (Wix) to handle the execution phase of logistics.

The system replaces manual spreadsheet routing with an algorithmic approach, handling order ingestion, vehicle routing optimization (VRP), driver dispatch, and real-time "Last Mile" customer visibility.

### Key Capabilities

- **Headless Ingestion:** Automated webhook bridge that sanitizes and geocodes orders from the legacy Wix platform.
- **Algorithmic Routing:** Uses **Google OR-Tools** to solve the Vehicle Routing Problem (VRP) with capacity and time-window constraints for multi-state "North/South" runs.
- **Real-Time Visibility:** High-fidelity "Pizza Tracker" experience for customers, powered by **Redis Pub/Sub** and WebSocket streams.
- **Hybrid Mobile App:** A **Capacitor**based driver application that handles background GPS tracking, offline-first manifest management, and "Proof of Delivery" photo uploads.

## 🏗 Technical Architecture

This project utilizes a **Hybrid Cloud Architecture** to maximize developer velocity and infrastructure robustness.

| **Component** | **Technology** | **Hosting** | **Role** |
| --- | --- | --- | --- |
| **Frontend** | Next.js + Tailwind | **Vercel** | Admin Dashboard & Customer Tracker. |
| **Backend** | Python FastAPI | **AWS ECS (Fargate)** | Core Logic, Webhooks, & Routing Algorithm. |
| **Database** | PostgreSQL + PostGIS | **AWS RDS** | Geospatial Data & Persistence. |
| **Caching** | Redis | **AWS ElastiCache** | Live GPS State & Session Management. |
| **Mobile** | React + Capacitor | **App Store** | Driver Companion App (iOS/Android). |

### Monorepo Structure

We use a unified repository to manage the distributed services.

```
/ushipp-occ
├── /apps
│   ├── /web           # Next.js (Admin Console & Customer Tracker)
│   ├── /api           # Python FastAPI (Backend Logic)
│   └── /driver        # Next.js + Capacitor (Mobile Wrapper)
├── /packages
│   ├── /db-types      # Shared Types (TypeScript Interfaces)
│   └── /config        # Shared Constants
└── .github            # CI/CD Pipelines (AWS CodePipeline / Vercel)

```

## 🚀 Getting Started (Local Development)

Follow these steps to get the entire distributed system running on your local machine.

### Prerequisites

- Node.js (LTS) & npm
- Python 3.10+
- Docker (Optional, but recommended)
- Supabase Account (for local Dev DB)

### 1. Clone & Setup

```
git clone [https://github.com/yourusername/ushipp-occ.git](https://github.com/yourusername/ushipp-occ.git)
cd ushipp-occ
npm install  # Installs shared JS dependencies

```

### 2. Database Setup

1. Create a project on [Supabase](https://supabase.com/).
2. Run the schema script located in `/infrastructure/database_schema.sql` in the Supabase SQL Editor.
3. Get your **Connection String (URI)**.

### 3. Backend Setup (Python)

```
cd apps/api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Add your DATABASE_URL here
uvicorn main:app --reload

```

> API will be live at http://localhost:8000. Documentation at /docs.
> 

### 4. Frontend Setup (Next.js)

```
cd apps/web
cp .env.example .env.local  # Add NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev

```

> Dashboard will be live at http://localhost:3000.
> 

## 🔄 Deployment Strategy

### Frontend (Vercel)

Connect the repository to Vercel. Set the **Root Directory** to `apps/web`. Vercel will automatically deploy changes pushed to the `main` branch.

### Backend (AWS)

The project includes a `Dockerfile` in `apps/api`.

1. **Build:** `docker build -t ushipp-api ./apps/api`
2. **Deploy:** Push image to **AWS ECR**.
3. **Run:** Update **AWS ECS Service** to pull the new image.

## 🛡 License

This project is proprietary software developed for University Shipping.