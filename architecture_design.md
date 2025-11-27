# Architecture Design

# Ushipp OCC - Technical Architecture & Stack

## 1. The Distributed System (Hybrid Cloud)

We utilize a **Hybrid Architecture** to maximize developer experience (frontend) and engineering robustness (backend).

| **Component** | **Tech Stack** | **Hosting Service** | **Role** |
| --- | --- | --- | --- |
| **Frontend** | **Next.js** + Tailwind CSS | **Vercel** | Admin Dashboard & Customer Tracker. Handles UI, SEO, and static generation. |
| **Backend** | **Python FastAPI** | **AWS ECS / Railway** | The Logic Core. Handles Webhooks, Routing Algorithm (OR-Tools), and API endpoints. |
| **Database** | **PostgreSQL** + **PostGIS** | **Supabase (AWS)** | The Source of Truth. PostGIS handles geospatial queries (radius search). |
| **Realtime** | **Redis** | **Supabase / ElastiCache** | In-memory cache for live GPS coordinate streaming. |
| **Mobile** | **Capacitor** + React | **App Store** | Native iOS/Android wrapper allowing background GPS and Camera access. |

## 2. Monorepo Code Structure

We use a single GitHub repository to manage all services.

```
/ushipp-occ
├── /apps
│   ├── /web           # Next.js App (Admin & Customer)
│   ├── /api           # Python FastAPI App (Logic & Workers)
│   └── /driver        # Next.js + Capacitor App (Mobile)
├── /packages
│   ├── /db-types      # Shared TypeScript interfaces (Order, Route)
│   └── /config        # Shared constants
└── .github            # CI/CD Workflows

```

## 3. Data Flow & Communication

1. **Frontend -> Backend:**
    - **Protocol:** HTTP/JSON.
    - *Example:* Admin clicks "Optimize" -> Next.js sends `POST /api/routes/optimize` to Python backend.
2. **Backend -> Database:**
    - **Protocol:** SQLAlchemy / SQLModel.
    - *Example:* Python saves the optimized route manifest to Postgres.
3. **Mobile -> Backend:**
    - **Protocol:** Secure API Rest.
    - *Example:* Driver App sends `POST /driver/location` every 10s.
4. **Backend -> Redis -> Frontend:**
    - **Protocol:** Pub/Sub (WebSockets).
    - *Example:* Python pushes location to Redis channel `truck_1`. Frontend subscribes and updates map marker.

## 4. Deployment Strategy

- **Vercel (Frontend):** Connects to GitHub. Automatically deploys changes detected in `/apps/web`.
- **AWS/Railway (Backend):** Connects to GitHub. Detects changes in `/apps/api`. Builds the `Dockerfile` and deploys the container.
- **Mobile:** Manual build script (`npm run build:native`) generates binaries for App Store submission.