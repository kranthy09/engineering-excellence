# Portfolio Website Implementation Plan

## Architecture Overview

We will adopt a **Decoupled Architecture** (Headless CMS pattern) to ensure separation of concerns, scalability, and flexibility.

### 1. Frontend (Presentation Layer)
- **Framework**: Next.js 14+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS (with a focus on premium aesthetics)
- **Rendering**: Hybrid (SSR for SEO, CSR for interactivity, ISR for static content updates)
- **Role**: Consumes APIs from the backend to display content. Handles the "Admin Dashboard" UI.

### 2. Backend (Content & Logic Layer)
- **Framework**: FastAPI (Python)
- **Database**: SQLite (Development) -> PostgreSQL (Production)
- **ORM**: SQLModel (Pydantic + SQLAlchemy)
- **Role**: Serves as the "Headless CMS". Manages data for Projects, Blogs, Experience, and Profile. Provides REST APIs.

### 3. Domain & Deployment Strategy
- **Frontend**: Deployed on Vercel (optimized for Next.js).
- **Backend**: Deployed on a cloud provider (e.g., Railway, Render, or AWS EC2) or Vercel (as Serverless Functions, though FastAPI is better as a standalone service for this use case).
- **Domain Management**:
    - `kranthi.com` -> Frontend (Main Portfolio)
    - `api.kranthi.com` -> Backend API
    - `admin.kranthi.com` -> Redirects to `kranthi.com/admin` (Protected Route)

## Implementation Phases

### Phase 1: Foundation Setup
- [ ] Initialize Monorepo structure (`/portfolio/frontend`, `/portfolio/backend`).
- [ ] **Backend**: Setup FastAPI, SQLModel, and basic configuration.
- [ ] **Frontend**: Setup Next.js, Tailwind CSS, and basic layout (Hero, Navbar, Footer).
- [ ] Define shared types/interfaces.

### Phase 2: Backend Core (The "Engine")
- [ ] Design Database Schema (Projects, Blogs, Experience, Profile).
- [ ] Implement CRUD APIs for all resources.
- [ ] Implement Image Upload handling (Local storage for dev, S3/Cloudinary for prod).
- [ ] Add Basic Authentication (OAuth2 with Password or JWT) for Admin routes.

### Phase 3: Frontend Implementation (The "Face")
- [ ] **Design System**: Define colors, typography, and reusable UI components (Cards, Buttons, Inputs).
- [ ] **Public Pages**:
    - Homepage (Hero, Featured Projects, Latest Blogs).
    - Projects Listing & Detail Page.
    - Blog Listing & Detail Page (Markdown rendering).
    - About & Experience Timeline.
    - Contact Section.
- [ ] **API Integration**: Connect Frontend to FastAPI endpoints.

### Phase 4: Admin Dashboard (The "Control Center")
- [ ] Create `/admin` routes in Next.js.
- [ ] Implement Login view.
- [ ] Build Editors:
    - Markdown Editor for Blogs.
    - Forms for Projects and Experience.
    - Profile settings editor.
- [ ] Secure these routes with Auth guards.

### Phase 5: Polish & Optimization
- [ ] **SEO**: Meta tags, Open Graph, Sitemap generation.
- [ ] **Performance**: Image optimization, Code splitting.
- [ ] **Animations**: Framer Motion for smooth transitions.
- [ ] **Testing**: Basic unit tests for Backend, Component tests for Frontend.

## Technical Specifications

### Backend (FastAPI)
- **Dependency Management**: `poetry` or `pip` with `requirements.txt`.
- **Structure**:
  ```
  backend/
  ├── app/
  │   ├── api/ (endpoints)
  │   ├── core/ (config, security)
  │   ├── models/ (SQLModel classes)
  │   ├── services/ (business logic)
  │   └── main.py
  └── ...
  ```

### Frontend (Next.js)
- **Structure**:
  ```
  frontend/
  ├── src/
  │   ├── app/ (pages)
  │   ├── components/ (ui, features)
  │   ├── lib/ (api clients, utils)
  │   └── types/
  └── ...
  ```

## Next Steps
1. Create the directory structure.
2. Initialize the FastAPI backend.
3. Initialize the Next.js frontend.
