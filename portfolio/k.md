# V1 Build Plan - Divided into Achievable Parts

## Part 0: Foundation (Pre-V1)

Setup infrastructure that everything else depends on
Tasks:

### 1.Docker Infrastructure (V0.1)

- Create docker-compose.yml with 3 services
- Frontend Dockerfile with Next.js 14
- Backend Dockerfile with FastAPI
- PostgreSQL service configuration
- Verify all containers build and start

### 2.Health & Connectivity (V0.2 + V0.3)

Backend: GET /api/v1/health endpoint
Database connection verification
Frontend: Basic page that fetches backend health
Hot reload setup for both services
Volume mounts configuration

#### Acceptance:

```
docker compose up
→ Frontend: localhost:3000 shows "Backend: Connected"
→ Backend: localhost:8000/api/v1/health returns healthy
→ Changes in code reflect without restart
```

---

### **Part 1: Design System & UI Foundation**

_Build the visual language before content_

**Tasks:**

1. **Design Tokens** (DESIGN.md implementation)

   - CSS variables setup (colors, spacing, typography)
   - Light/dark theme toggle
   - `globals.css` with design tokens
   - Tailwind config extending tokens

2. **Core UI Components** (`components/ui/`)

   - Button (variants: primary, secondary, ghost)
   - Card (interactive, elevated)
   - Badge
   - Input
   - Export from `components/ui/index.ts`

3. **Layout Components** (`components/layout/`)
   - Container (narrow, default, wide)
   - Navbar (responsive, mobile hamburger)
   - Footer

**Acceptance:**

- Storybook-style page showing all UI components
- Theme toggle works
- Mobile responsive navbar

---

### **Part 2: Type System & Data Contracts**

_Define the shape of data before building features_

**Tasks:**

1. **Frontend Types** (`src/types/`)

   - `project.ts` - ProjectListItem, Project
   - `blog.ts` - BlogListItem, Blog
   - `case-study.ts` - CaseStudyListItem, CaseStudy
   - `index.ts` - Unified exports

2. **Backend Schemas** (`backend/app/schemas/`)

   - Pydantic models for all entities
   - List vs Detail response shapes
   - Validation rules

3. **API Client** (`src/lib/api.ts`)
   - Typed fetch wrappers
   - Error handling pattern
   - Base URL configuration

**Acceptance:**

- TypeScript compiles with no errors
- API client typed correctly
- Mock data matches schema

---

### **Part 3: Static Content Pipeline**

_Get content flowing before databases_

**Tasks:**

1. **Content Structure** (`frontend/content/`)

   - Create markdown files for projects (3 samples)
   - Create markdown files for blogs (3 samples)
   - Create markdown files for case studies (3 samples)
   - Consistent frontmatter format

2. **Content Loader** (`src/lib/content.ts`)

   - Parse markdown with gray-matter
   - Transform to typed objects
   - Sort by publishedAt
   - Filter published only

3. **Content Renderer** (`components/content/`)
   - `ContentRenderer.tsx` - Markdown to HTML
   - Syntax highlighting setup
   - Responsive image handling

**Acceptance:**

- 9 markdown files with valid frontmatter
- Content loader returns typed data
- Markdown renders with code highlighting

---

### **Part 4: Home Page**

_The gateway that showcases everything_

**Tasks:**

1. **Section Components** (`components/sections/`)

   - `HeroSection.tsx` - Name, tagline, CTA
   - `ProjectsSection.tsx` - 3 featured projects
   - `BlogSection.tsx` - 3 recent posts
   - `CaseStudiesSection.tsx` - 3 recent studies

2. **Home Page Assembly** (`app/page.tsx`)
   - Compose all sections
   - Fetch static content
   - Stagger animations
   - Proper spacing rhythm

**Acceptance:**

- Home page loads in <2s
- All sections visible
- Smooth scroll to sections
- Mobile responsive

---

### **Part 5: Projects Feature**

_Complete vertical slice_

**Tasks:**

1. **Project Card** (`components/content/ProjectCard.tsx`)

   - Display: title, tech stack, summary, thumbnail
   - Hover animation
   - Link to detail page

2. **Projects List** (`app/projects/page.tsx`)

   - Grid layout (1/2/3 columns)
   - Client-side filter by tech stack
   - Load all published projects
   - Empty state

3. **Project Detail** (`app/projects/[slug]/page.tsx`)
   - Full content rendering
   - Metadata display
   - Links to deployed/codebase
   - Related projects suggestions
   - Static generation for all slugs

**Acceptance:**

- `/projects` shows grid of cards
- Filter works client-side
- `/projects/[slug]` renders full content
- Build generates static pages

---

### **Part 6: Blog Feature**

_Replicate pattern established by projects_

**Tasks:**

1. **Blog Card** (`components/content/BlogCard.tsx`)

   - Display: title, category, tags, read time, date
   - Category badge styling
   - Hover effects

2. **Blog List** (`app/blog/page.tsx`)

   - Grid layout
   - Filter by category dropdown
   - Sort by date (newest first)

3. **Blog Detail** (`app/blog/[slug]/page.tsx`)
   - Content rendering
   - Category + tags display
   - Related posts (same category)
   - Static generation

**Acceptance:**

- `/blog` shows all posts
- Category filter functional
- Detail pages render markdown
- Read time displayed

---

### **Part 7: Case Studies Feature**

_Final content type_

**Tasks:**

1. **Case Study Card** (`components/content/CaseStudyCard.tsx`)

   - Similar to blog card
   - Emphasis on category visual

2. **Case Studies List** (`app/case-studies/page.tsx`)

   - Category tabs (Architecture, Design, Research)
   - Grid layout
   - Sort by date

3. **Case Study Detail** (`app/case-studies/[slug]/page.tsx`)
   - Structured sections (Problem → Approach → Outcome)
   - Related studies
   - Static generation

**Acceptance:**

- `/case-studies` with category tabs
- Detail pages structured properly
- All pages static generated

---

### **Part 8: About Page**

_Simple but complete_

**Tasks:**

1. **About Content** (`app/about/page.tsx`)
   - Introduction section
   - Skills grid
   - Experience timeline (optional)
   - Contact information
   - Social links

**Acceptance:**

- `/about` page exists
- Content is readable
- Mobile responsive
- Contact CTA clear

---

### **Part 9: Polish & Performance**

_Final touches before launch_

**Tasks:**

1. **SEO & Metadata**

   - `metadata` exports for all pages
   - Open Graph images
   - Sitemap generation
   - robots.txt

2. **Animations & Micro-interactions**

   - Page transition animations
   - Stagger list items
   - Hover states polish
   - Loading states

3. **Accessibility Audit**

   - Keyboard navigation
   - Focus indicators
   - Alt text for images
   - ARIA labels where needed

4. **Performance Optimization**
   - Image optimization (next/image)
   - Font optimization
   - Bundle analysis
   - Lighthouse score >90

**Acceptance:**

- Lighthouse: 90+ on all metrics
- No console errors
- Keyboard navigation works
- All images have alt text

---

## **Suggested Build Order**

```

Part 0 (Foundation)
↓
Part 1 (Design System)
↓
Part 2 (Types)
↓
Part 3 (Content Pipeline)
↓
Part 4 (Home)
↓
Part 5 (Projects) ←─ Full vertical slice
↓
Part 6 (Blog) ←────── Replicate pattern
↓
Part 7 (Case Studies) ← Replicate pattern
↓
Part 8 (About)
↓
Part 9 (Polish)
```
