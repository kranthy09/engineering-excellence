# PROJECTS ROADMAP - Bridge DSA to Real Engineering

**Purpose:** Build projects that apply DSA patterns to real-world engineering problems
**Timeline:** Weeks 9-12 (after DSA foundation is solid)
**Goal:** Portfolio pieces that demonstrate both algorithmic thinking and engineering skills

---

## Table of Contents

1. [Quick-Win Games (Week 9)](#quick-wins)
2. [Portfolio Projects (Weeks 10-12)](#portfolio-projects)
3. [Pattern-to-Project Mapping](#pattern-mapping)
4. [Tech Stack Recommendations](#tech-stack)
5. [Implementation Guide](#implementation-guide)

---

## Quick-Win Games (Week 9) {#quick-wins}

### Game 1: PathFinder Arena

**Time:** 2-3 days
**DSA Patterns:** BFS, DFS, Dijkstra, A\*, Priority Queue

**Features:**

- Visual grid with draggable start/end points
- Multiple algorithms running side-by-side
- Real-time visualization (colored cells showing exploration)
- Statistics: nodes visited, path length, time elapsed
- Obstacles and weighted terrain
- Speed control slider

**Tech Stack:**

- Frontend: React + HTML Canvas or React Flow
- Styling: Tailwind CSS
- State: React hooks

**Learning Outcomes:**

- Graph traversal in action
- Performance comparison (BFS vs Dijkstra vs A\*)
- UI for algorithm visualization

**Showcase Value:**

- Popular GitHub topic (easy stars)
- Demonstrates graph algorithm mastery
- Interactive resume piece

**Implementation Steps:**

1. Create grid component with cell states (empty/wall/start/end/visited/path)
2. Implement BFS algorithm with step-by-step execution
3. Add visualization queue (dequeue states slowly for animation)
4. Add DFS, Dijkstra, A\* implementations
5. Add UI controls (algorithm selector, speed, reset)
6. Deploy on Vercel/Netlify

---

### Game 2: Sorting Visualizer

**Time:** 1-2 days
**DSA Patterns:** Sorting algorithms, recursion, divide-and-conquer

**Features:**

- Bar chart showing array elements
- Animate: Bubble Sort, Merge Sort, Quick Sort, Heap Sort
- Compare algorithms side-by-side
- Adjustable array size and animation speed
- Sound effects for comparisons/swaps (fun!)
- Complexity shown in real-time

**Tech Stack:**

- Frontend: React + D3.js or Chart.js
- Audio: Web Audio API

**Learning Outcomes:**

- Recursion visualization
- Complexity differences in action
- Animation timing control

**Showcase Value:**

- Classic visualization project
- Shows understanding of fundamental algorithms
- Engaging demonstration

---

### Game 3: N-Queens Solver with Backtracking

**Time:** 2 days
**DSA Patterns:** Backtracking, recursion

**Features:**

- Interactive chessboard (4x4 to 12x12)
- Manual mode: user places queens, system shows conflicts
- Auto-solve mode: visualize backtracking algorithm
- Highlight invalid positions in real-time
- Show solution count
- Animation of backtracking (place → conflict → undo)

**Tech Stack:**

- Frontend: React + CSS Grid
- State: Recursive solver with visualization hooks

**Learning Outcomes:**

- Backtracking pruning visualization
- Constraint satisfaction problems
- Recursive state management

**Showcase Value:**

- Classic CS problem
- Shows ability to explain complex recursion
- Interactive learning tool

---

### Game 4: Binary Search Tree Visualizer

**Time:** 2 days
**DSA Patterns:** Tree DFS, BFS, BST operations

**Features:**

- Visual tree representation (SVG nodes and edges)
- Insert, delete, search operations with animation
- Show traversals: inorder, preorder, postorder, level-order
- Balance check and AVL rotation visualization
- Path highlighting for search operations

**Tech Stack:**

- Frontend: React + D3.js for tree layout
- Layout: D3 tree layout algorithm

**Learning Outcomes:**

- Tree structure visualization
- BST property maintenance
- Tree traversal patterns

**Showcase Value:**

- Demonstrates tree algorithm understanding
- Clean visualization of abstract concept
- Educational tool value

---

### Game 5: Sudoku Solver

**Time:** 2-3 days
**DSA Patterns:** Backtracking, constraint satisfaction

**Features:**

- 9x9 Sudoku grid
- User can input puzzle or generate random
- Solve button with animated backtracking
- Show algorithm trying and undoing choices
- Validation for user inputs
- Difficulty levels (easy/medium/hard)

**Tech Stack:**

- Frontend: React + CSS Grid
- Backend: FastAPI for puzzle generation (optional)

**Learning Outcomes:**

- Practical backtracking application
- Constraint checking optimization
- Game logic implementation

**Showcase Value:**

- Recognizable problem
- Shows problem-solving methodology
- Potential mobile app

---

## Portfolio Projects (Weeks 10-12) {#portfolio-projects}

### Project 1: CodeCollab - Real-time Collaborative Code Editor

**Time:** 5-7 days
**DSA Patterns:** Trie (autocomplete), String algorithms, CRDT/OT

**Core Features:**

- Monaco editor integration (VS Code engine)
- Real-time multi-user editing
- Syntax highlighting for Python/JavaScript
- Autocomplete using Trie
- Cursor position sharing
- Conflict resolution for simultaneous edits

**Advanced Features:**

- Code execution (sandboxed)
- Chat alongside editor
- File tree navigation
- Share via unique URL

**Tech Stack:**

- Frontend: Next.js + Monaco Editor
- Backend: FastAPI + WebSockets
- State sync: Yjs (CRDT library) or custom OT
- Code execution: Docker containers or Piston API
- Database: PostgreSQL for sessions

**Learning Outcomes:**

- Distributed state management
- Real-time systems with WebSockets
- Operational Transformation / CRDT algorithms
- Security (code sandboxing)

**Showcase Value:**

- Complex distributed system
- Directly applicable to Google Docs, Figma, Replit
- Shows full-stack + algorithms
- Can discuss in system design rounds

**Implementation Steps:**

1. Setup Next.js + Monaco, basic editor
2. Add WebSocket server in FastAPI
3. Implement user connection management
4. Add text sync (start simple: send full text, then optimize)
5. Study and implement Yjs for CRDT
6. Add autocomplete with Trie structure
7. Deploy with Docker (frontend + backend + DB)

---

### Project 2: SmartCache - Distributed Caching System

**Time:** 5-7 days
**DSA Patterns:** Hash Map, LRU Cache (DLL + HashMap), Consistent Hashing

**Core Features:**

- Multi-node cache cluster (3+ nodes)
- LRU eviction policy
- Consistent hashing for key distribution
- REST API (GET, SET, DELETE)
- Cache statistics dashboard

**Advanced Features:**

- TTL (time-to-live) for keys
- Cache warming strategies
- Replication for fault tolerance
- Admin dashboard with metrics

**Tech Stack:**

- Backend: Python/Go for cache nodes
- Coordination: Redis/etcd for node discovery
- Dashboard: React + Chart.js
- Load testing: Locust or custom script

**Learning Outcomes:**

- LRU cache implementation (interview favorite!)
- Consistent hashing algorithm
- Distributed systems fundamentals
- Performance testing and profiling

**Showcase Value:**

- Shows understanding of caching (critical topic)
- Demonstrates distributed systems knowledge
- Directly relates to Redis, Memcached internals
- Great system design discussion piece

**Implementation Steps:**

1. Implement LRU cache in Python (DLL + HashMap)
2. Add REST API wrapper (FastAPI)
3. Implement consistent hashing ring
4. Setup multiple cache instances
5. Add client library that hashes keys to nodes
6. Build dashboard showing cache hits/misses, node load
7. Write load tests, optimize performance

---

### Project 3: AlgoViz - Interactive Algorithm Learning Platform

**Time:** 7-10 days
**DSA Patterns:** ALL patterns from your learning

**Core Features:**

- 20 algorithm visualizations (all patterns you learned)
- Step-by-step execution with state visualization
- User input custom test cases
- Code shown alongside visualization
- Complexity analysis in real-time
- Explanations for each step

**Advanced Features:**

- User authentication (save progress)
- Problem sets grouped by pattern
- "Challenge mode" - user predicts next step
- Shareable visualizations (unique URLs)
- Commenting system

**Tech Stack:**

- Frontend: React + D3.js/Canvas for visualizations
- Backend: FastAPI for user management
- Code execution: Sandboxed (Docker or VM)
- Database: PostgreSQL for users/progress
- Auth: JWT

**Learning Outcomes:**

- Teaching through visualization (deepest learning)
- Complex state management
- Secure code execution
- Building educational tools

**Showcase Value:**

- Shows DEEP understanding (teaching = mastery)
- Open source potential (community value)
- Demonstrates full-stack + DSA + UI/UX
- Perfect for interviews: "I built this to learn/teach"
- Can monetize or use for tutoring

**Implementation Steps:**

1. Design component architecture for visualizations
2. Implement 5 core visualizations (Two Pointers, Sliding Window, BFS, DFS, DP)
3. Create reusable visualization framework
4. Add user authentication
5. Build problem set database
6. Add remaining 15 visualizations
7. Create landing page, documentation
8. Deploy with CI/CD
9. Add to GitHub with good README
10. Share on Reddit/HackerNews for feedback

---

### Project 4: GraphDB Lite - Graph Database with Query Language

**Time:** 7-10 days
**DSA Patterns:** Graph DFS/BFS, Union Find, Topological Sort, Dijkstra

**Core Features:**

- Store nodes and relationships
- Query language (subset of Cypher/Gremlin)
- Graph traversal queries (shortest path, connected components)
- CRUD operations on nodes/edges
- REST API and CLI interface

**Advanced Features:**

- Query optimization
- Indexing for fast lookups
- Aggregation queries
- Import/export (JSON, CSV)
- Web UI for graph visualization

**Tech Stack:**

- Backend: Python/Go
- Storage: File-based or SQLite initially
- Query parser: PLY (Python Lex-Yacc) or ANTLR
- Visualization: React + D3.js force-directed graph

**Learning Outcomes:**

- Graph algorithms at scale
- Query language design and parsing
- Database internals
- Performance optimization

**Showcase Value:**

- Ambitious project (shows initiative)
- Combines multiple algorithms
- Demonstrates database understanding
- Research potential (publish findings)

---

### Project 5: Rate Limiter Service

**Time:** 3-5 days
**DSA Patterns:** Sliding Window, Queue, Hash Map

**Core Features:**

- Multiple algorithms: Token Bucket, Leaky Bucket, Fixed Window, Sliding Window
- REST API to check if request is allowed
- Per-user rate limiting
- Per-IP rate limiting
- Configurable limits

**Advanced Features:**

- Distributed rate limiting (Redis-backed)
- Different tiers (free/premium users)
- Rate limit headers (X-RateLimit-\*)
- Analytics dashboard
- Burst allowance

**Tech Stack:**

- Backend: FastAPI or Go
- Storage: Redis for distributed state
- Dashboard: React + Chart.js
- Testing: Locust for load testing

**Learning Outcomes:**

- Sliding window algorithm in production
- Distributed systems patterns
- API design
- Performance at scale

**Showcase Value:**

- Directly applicable to every API company
- Common interview system design question
- Shows understanding of real-world constraints

---

### Project 6: Autocomplete Search Engine

**Time:** 4-6 days
**DSA Patterns:** Trie, Heap (Top K), String algorithms

**Core Features:**

- Trie-based prefix search
- Ranking by frequency/recency
- Handle typos (edit distance)
- Fast autocomplete (<50ms)
- Millions of words/phrases

**Advanced Features:**

- Fuzzy matching
- Multi-language support
- Personalized suggestions (user history)
- Trending searches
- Analytics on search patterns

**Tech Stack:**

- Backend: Python + C extension for Trie (performance) or Go
- Frontend: React with debounced input
- Database: PostgreSQL for phrase frequencies
- Cache: Redis for hot prefixes

**Learning Outcomes:**

- Trie implementation and optimization
- Top-K problem with heaps
- String similarity algorithms
- Performance optimization (profiling)

**Showcase Value:**

- Powers every search box (Google, Amazon)
- Common interview question
- Performance engineering showcase

---

## Pattern-to-Project Mapping {#pattern-mapping}

### Two Pointers

- **PathFinder Arena** - Boundary checking
- **Merge K Sorted Lists Visualizer** - Merging with pointers

### Sliding Window

- **Rate Limiter Service** - Time window management
- **Streaming Analytics Dashboard** - Moving averages

### Hash Map

- **SmartCache** - Core data structure
- **Anagram Finder Tool** - Word frequency

### DFS/BFS

- **PathFinder Arena** - Core algorithms
- **GraphDB Lite** - Query traversals
- **Maze Generator/Solver** - Grid traversal

### Trees

- **Binary Search Tree Visualizer** - All tree operations
- **File System Explorer** - Tree structure UI
- **Expression Evaluator** - Parse tree

### Dynamic Programming

- **Sequence Alignment Tool** - Edit distance
- **Stock Portfolio Optimizer** - DP optimization
- **Text Diff Viewer** - LCS algorithm (Git-like)

### Backtracking

- **N-Queens Solver** - Classic backtracking
- **Sudoku Solver** - Constraint satisfaction
- **Regex Matcher** - Pattern matching with backtracking

### Graphs

- **Social Network Analyzer** - Graph metrics
- **Dependency Resolver** - Topological sort
- **Network Flow Optimizer** - Max flow algorithms

### Heap

- **Task Scheduler** - Priority queue
- **Real-time Leaderboard** - Top K scores
- **Merge K Sorted Files** - External sort

### Trie

- **Autocomplete Search Engine** - Prefix matching
- **IP Router Simulator** - Longest prefix match

### Union Find

- **Percolation Simulator** - Dynamic connectivity
- **Network Partition Detector** - Component detection
- **Image Segmentation Tool** - Connected components

---

## Tech Stack Recommendations {#tech-stack}

### For Quick-Win Games (Weeks 9)

**Frontend:** React + Vite (fast setup)
**Styling:** Tailwind CSS
**Visualization:** D3.js or HTML Canvas
**Deployment:** Vercel or Netlify

### For Portfolio Projects (Weeks 10-12)

**Frontend:** Next.js (for SEO, SSR)
**Backend:** FastAPI (Python) or Fiber (Go)
**Database:** PostgreSQL + Redis
**Real-time:** WebSockets (Socket.IO or native)
**Auth:** JWT + bcrypt
**Deployment:** Docker + DigitalOcean/AWS
**CI/CD:** GitHub Actions

### Your Advantage

- **Python:** Use for algorithms (clear, readable)
- **Next.js:** Frontend framework you know
- **FastAPI:** Backend framework you know
- **Django:** For projects needing full auth/admin

---

## Implementation Guide {#implementation-guide}

### Week 9: Quick Wins (Build 3-4 Games)

**Monday-Tuesday: PathFinder Arena**

- 4 hours: Grid + UI
- 4 hours: BFS + DFS implementations
- 2 hours: Visualization logic

**Wednesday: Sorting Visualizer**

- 3 hours: Bar chart component
- 3 hours: 3 sorting algorithms
- 2 hours: Animation + controls

**Thursday-Friday: N-Queens or Sudoku**

- 4 hours: Board UI + interaction
- 4 hours: Backtracking algorithm
- 2 hours: Visualization + polish

**Weekend: Deploy + Document**

- Create README with GIFs
- Deploy to Vercel
- Add to resume/portfolio site

---

### Week 10: Portfolio Project #1 (CodeCollab)

**Day 1-2: Basic Editor**

- Setup Next.js + Monaco
- Basic styling and layout
- Single-user editing works

**Day 3-4: WebSocket + Multi-user**

- FastAPI WebSocket server
- User connection management
- Basic text synchronization

**Day 5-6: CRDT/OT + Features**

- Integrate Yjs or custom OT
- Cursor position sharing
- Chat feature

**Day 7: Polish + Deploy**

- Error handling
- Loading states
- Deploy with Docker
- Documentation

---

### Week 11: Portfolio Project #2 (SmartCache or AlgoViz)

Choose based on interest:

- **SmartCache:** If you want to focus on distributed systems
- **AlgoViz:** If you want comprehensive DSA showcase

Follow similar daily breakdown:

- Days 1-2: Core functionality
- Days 3-4: Advanced features
- Days 5-6: Optimization + testing
- Day 7: Deploy + document

---

### Week 12: Polish + Interview Prep

**Mon-Wed: Final Project Touch-ups**

- Add analytics/monitoring
- Performance testing
- Security hardening
- Better UI/UX

**Thu-Fri: Documentation**

- README with architecture diagrams
- API documentation
- Setup instructions
- Demo videos/GIFs

**Weekend: Portfolio Site**

- Create portfolio site showcasing all projects
- Write blog posts about technical decisions
- Prepare project talking points for interviews

---

## Project Presentation Guide

### For Resume

```
PathFinder Arena - Interactive Algorithm Visualizer
- Implemented BFS, DFS, Dijkstra, A* with real-time visualization
- React + Canvas API, 500+ lines of optimized JavaScript
- Demonstrates graph algorithm mastery and UI engineering
```

### For Interviews

**When asked "Tell me about a project":**

```
"I built CodeCollab, a real-time collaborative code editor.

The interesting challenge was handling concurrent edits from multiple
users. I implemented Operational Transformation to resolve conflicts
when users type simultaneously.

Technically, I used WebSockets for real-time communication, Monaco
editor for the UI, and FastAPI for the backend.

The hardest part was debugging race conditions in the state sync logic.
I solved it by adding detailed logging and writing comprehensive tests
for edge cases like conflicting deletes and inserts.

The project taught me a lot about distributed systems and real-time
data synchronization, which directly relates to systems like Google
Docs or Figma."
```

**Follow-up questions they might ask:**

- "How did you handle network failures?" → Retry logic, buffering
- "What about security?" → Input sanitization, sandboxed execution
- "How would you scale this?" → Lead into system design discussion

---

## Success Metrics

### You're on Track When:

**Week 9 End:**

- ✅ 3 games deployed and working
- ✅ All on GitHub with good READMEs
- ✅ Can explain DSA patterns used in each

**Week 10 End:**

- ✅ 1 portfolio project feature-complete
- ✅ Deployed and accessible via URL
- ✅ Architecture documented

**Week 11 End:**

- ✅ 2 portfolio projects complete
- ✅ Can discuss technical decisions confidently
- ✅ Projects linked on resume

**Week 12 End:**

- ✅ Portfolio site live
- ✅ All projects documented
- ✅ Ready to discuss in interviews
- ✅ GitHub profile looks strong

---

## GitHub Best Practices

### README Template

```markdown
# Project Name

![Demo GIF](demo.gif)

## What It Does

[One sentence description]

## Why I Built It

[Learning goals, DSA patterns applied]

## Tech Stack

- Frontend: [tech]
- Backend: [tech]
- Algorithms: [patterns used]

## Key Features

- [Feature 1]
- [Feature 2]

## Technical Highlights

- Implemented [algorithm] achieving O(n) complexity
- Optimized [component] reducing latency by 50%
- [Other technical achievement]

## Demo

[Live URL] | [Video Demo]

## Setup

[Installation instructions]

## What I Learned

[Key takeaways]
```

### Repository Structure

```
project-name/
├── frontend/
├── backend/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── ALGORITHMS.md
├── tests/
├── docker-compose.yml
└── README.md
```

---

## Resources

### Learning

- **CRDT algorithms:** https://crdt.tech/
- **System design patterns:** https://github.com/donnemartin/system-design-primer
- **Algorithm visualization:** https://visualgo.net/

### Inspiration

- **Pathfinding:** https://qiao.github.io/PathFinding.js/visual/
- **Sorting:** https://www.toptal.com/developers/sorting-algorithms
- **Algorithm viz:** https://algorithm-visualizer.org/

### Deployment

- **Frontend:** Vercel, Netlify
- **Backend:** Railway, Render, DigitalOcean
- **Full-stack:** Fly.io, Heroku

---

## Final Checklist

**Before starting projects:**

- [ ] DSA fundamentals solid (Week 8 complete)
- [ ] 120+ problems solved
- [ ] Pattern recognition fast (<2 min)

**For each project:**

- [ ] Clear learning goal defined
- [ ] Tech stack chosen
- [ ] Daily milestones set
- [ ] Git commits frequent (show progress)

**Before interviews:**

- [ ] 3+ projects deployed
- [ ] Can explain every technical decision
- [ ] Portfolio site live
- [ ] GitHub profile polished
- [ ] Talking points prepared

---

**These projects transform you from "solved LeetCode problems" to "built real systems using DSA principles."**

That's the difference Google/Microsoft are looking for. 🚀
