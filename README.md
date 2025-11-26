Ushipp Operations Command Center (OCC) - Technical Architecture (Hybrid Cloud)

1. High-Level Stack and Deployment Summary

This project utilizes a Hybrid Architecture, leveraging Vercel for best-in-class frontend performance and AWS for robust backend computation and persistence.

Component

Technology

Hosting Platform

Why this choice?

Frontend/Admin

Next.js + React

Vercel

Optimized CI/CD for Next.js, Edge caching, and zero-config SSR.

Mobile App

React + Capacitor

App Store

Native wrapper around the Vercel web build.

Backend/API

Python FastAPI

AWS ECS (Fargate)

Supports long-running processes (Routing Algo) and scalable containerization.

Persistence

PostgreSQL + PostGIS

AWS RDS

Enterprise-grade managed SQL database with geospatial support.

Realtime

Redis

AWS ElastiCache

Sub-millisecond latency for GPS tracking.

Storage

Images

AWS S3

Durable object storage for proof-of-delivery photos.

2. Service Architecture & Connectivity

A. The "Frontend Layer" (Vercel)

Domain: track.ushipp.com

Deployment: Connects directly to the GitHub repo (/apps/web). Pushing code triggers a Vercel build.

Interaction: The Next.js app makes HTTP requests to api.ushipp.com (AWS) to fetch data. It does not talk to the database directly.

B. The "Backend Layer" (AWS)

Domain: api.ushipp.com

Ingress: An AWS Application Load Balancer (ALB) sits in front of the cluster to handle SSL termination and routing.

Compute: ECS Fargate runs the Dockerized Python API. It handles the "heavy lifting" (OR-Tools optimization) that would time out on Vercel.

Security: The ECS tasks run inside a private VPC. They allow traffic only from the ALB.

C. The "Data Layer" (AWS)

Database (RDS): Configured in a private subnet. Accepts connections only from the ECS Security Group.

Cache (ElastiCache): Stores the live state of drivers. Accessible only by the Backend.

3. The Deployment Pipeline (Best of Both Worlds)

We separate the deployment pipelines based on the hosting provider.

Pipeline A: Frontend (Automated via Vercel)

Trigger: Developer pushes code to /apps/web on GitHub.

Action: Vercel detects the change.

Build: Vercel runs npm build and deploys to the Edge Network.

Result: Updates are live in < 1 minute.

Pipeline B: Backend (AWS CodePipeline)

Trigger: Developer pushes code to /apps/api on GitHub.

Action: AWS CodePipeline detects the change.

Build: AWS CodeBuild creates the Docker container.

Deploy: AWS ECS performs a rolling update of the Fargate tasks.

Result: Updates are live in ~5-10 minutes (ensures zero downtime stability).

4. Cost & Efficiency Analysis

Efficiency: High. Vercel servers (Edge) communicate with AWS servers (Region). If both are in us-east-1 (Virginia), latency is negligible (< 10ms).

Cost:

Vercel: Free Tier (Generous for hobby/student projects).

AWS: You pay only for the "Muscle" (Compute/DB).

Savings: You save money by NOT paying for an AWS Load Balancer for the frontend (Vercel handles routing for free).

This architecture provides the "Resume Value" of using AWS for infrastructure while keeping the "Developer Velocity" of Vercel for the UI.
