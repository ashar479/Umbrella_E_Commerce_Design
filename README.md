# 🛒 Umbrella E‑Commerce System Design

This document outlines the **high‑level architecture, components, and design decisions** for building a scalable e‑commerce platform for **Umbrella Digital**.

---

## 📌 Problem Statement
Design an **end‑to‑end e‑commerce system** that supports:

- Product browsing & search
- Shopping cart & checkout
- Secure payments
- Order tracking
- Scalability for millions of users
- High availability and low latency during peak loads (e.g., sales events)

---

## 🏗️ High-Level Architecture
  ┌──────────────┐
  │   Client UI  │  (Web, Mobile, API)
  └──────┬───────┘
         │
  ┌──────▼────────┐
  │ API Gateway   │  (Rate limiting, Routing, Auth)
  └──────┬────────┘


---

## 🗄️ Data Storage Design

| Component       | Database                   | Notes |
|-----------------|----------------------------|-------|
| Product Catalog | **NoSQL** (MongoDB/DynamoDB)| Fast reads, flexible schema for varying product attributes |
| User Accounts   | **Relational** (PostgreSQL/MySQL) | Strong consistency for user data |
| Orders          | **Relational** (PostgreSQL) | ACID transactions for payment & order integrity |
| Cart            | **In‑Memory** (Redis)      | Low-latency updates & session storage |
| Search Index    | **Elasticsearch**          | Full-text search, filters, relevance scoring |

---

## 🔄 Workflow — Order Placement

1. **User adds items** to cart → Cart Service (Redis)
2. **Checkout request** goes through API Gateway
3. **Order Service** validates stock & reserves items
4. **Payment Service** processes via secure external provider (e.g., Stripe, Adyen)
5. On success:
   - Order stored in relational DB
   - Event emitted to Kafka for:
     - Inventory update
     - Shipping request
     - Email/SMS confirmation

---

## 📈 Scalability & Performance Strategies

- **API Gateway** → Rate limiting, request routing, authentication
- **Microservices** → Independent scaling for product, cart, order services
- **CDN** → Deliver static assets & product images globally
- **Caching** → Redis for cart/session; CDN edge caching for static content
- **Async Processing** → Kafka for non-blocking downstream workflows
- **Horizontal Scaling** → Stateless services + container orchestration (Kubernetes/ECS)

---

## 🔐 Security & Compliance

- **TLS Everywhere** – HTTPS for all client‑server communication
- **JWT-based Authentication** – Secure session management
- **PCI-DSS Compliance** – Delegate payment handling to certified providers
- **Input Validation & WAF** – Mitigate XSS, SQL injection, and other injection attacks
- **Role-Based Access Control (RBAC)** – Protect admin endpoints

---

## 📊 Capacity Planning (Sample Targets)

| Metric          | Target        |
|-----------------|--------------|
| Peak Users      | 5M concurrent |
| Avg Latency     | < 200ms       |
| Availability    | 99.99%        |
| Payment Success | 99%+          |

---

## 🔧 Tech Stack Recommendations

| Layer        | Technology Options |
|--------------|--------------------|
| Frontend     | React, Next.js, Vue |
| Backend API  | Node.js, Java Spring Boot, or Go |
| Database     | PostgreSQL, MongoDB |
| Search       | Elasticsearch |
| Cache        | Redis |
| Messaging    | Apache Kafka |
| Deployment   | AWS (ECS/EKS, Lambda for serverless tasks), GCP, or Azure |
| CI/CD        | GitHub Actions, Jenkins, ArgoCD |

---

## 📚 References

- Gatys et al., *Designing Data‑Intensive Applications* – Martin Kleppmann  
- [AWS Well‑Architected Framework](https://aws.amazon.com/architecture/well-architected/)  
- [Microservices Patterns – Chris Richardson](https://microservices.io/)

---

## ✨ Notes
This design uses:
- **Event-driven architecture** for scalability & decoupling
- **Polyglot persistence** to optimize storage for each component
- **Security-first** principles to ensure trust and compliance

Trade-offs:
- Slightly increased operational complexity from microservices
- Eventual consistency in some async workflows

---
