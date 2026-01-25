

## COMPLETE END-TO-END FLOW DIAGRAM

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                          COMPLETE REQUEST-TO-RESPONSE FLOW                              │
└──────────────────────────────────────────────────────────────────────────────────────────┘

TIME    LAYER 1         LAYER 2         LAYER 3         LAYER 4         LAYER 5
        CLIENT          HTTP API        AUTH & VAL      SCHEDULER       SUPERVISOR
        ─────           ───────         ─────────       ──────────      ───────────

T=0ms   REQUEST
        POST /api/
        summarize
        {"text"...}
                        │
                        ▼ (Router)
                        Extract route
                        Apply middleware

T=10ms                              │
                                    ▼ (Auth)
                                    Verify JWT
                                    Check roles
                                    Validate input
                                    Generate hash

T=20ms                                          │
                                                ▼ (Scheduler)
                                                Check cache
                                                Create exec
                                                Queue task

T=50ms                                                      │
                                                            ▼ (Supervisor)
                                                            Dequeue task
                                                            Analyze
                                                            Create plan
                                                            Route execution

T=100ms RESPONSE 202 ◄──────────────────────────────────────
        execution_id
        ws_url

        └─────────────────────────────────────────────────────────────────────►
                        ASYNC PROCESSING (Background)

        LAYER 6         LAYER 7         LAYER 8         LAYER 9
        WORKERS         LANGGRAPH       CACHE/QUEUE     DATABASE
        ───────         ─────────       ──────────      ────────

T=100ms │
        │ Worker 1: Dequeue
        │ Load checkpoint
        │
T=200ms │ Node 1: Preprocess
        │ Generate embeddings
        │ Cache (Redis)
        │
        ├─────────────┬─────────────┐
        │ (Parallel)  │ (Parallel)  │
T=500ms │             │             │
        │ Node 2:     │ Node 3:     │ Node 4:
        │ Stream      │ Concepts    │ Insights
        │ Enhanced    │ (parallel)  │ (parallel)
        │ +Emit       │             │
        │ tokens      │             │
        │ (WebSocket) │             │
        │             │             │
T=5500ms│ ◄───────────┴─────────────┘
        │ Node 5: Build Card
        │
T=6500ms│ Node 6: Persist
        │ Save to DB
        │ Cache result
        │ Emit completion
        │
T=8000ms└─► execution_complete event ─────────► Client WebSocket

        Processing:                         Client Experience:
        - Total: 8 seconds                  - HTTP resp: 100ms
        - Parallel saves 3s                 - Token stream: 5s
        - Well-distributed load             - Card appears: 8s
```

---

## TRAFFIC FLOW SUMMARY

```
REQUEST:     HTTP POST with JWT
  ↓
AUTH:        Verify token, check quota
  ↓
VALIDATION:  Validate payload, generate hash
  ↓
CACHE:       Check Redis for duplicate
  ├─ HIT  → Return cached result (< 100ms)
  └─ MISS → Continue to queue
  ↓
SCHEDULER:   Create execution, queue task
  ↓
RESPONSE:    202 Accepted + execution_id (200ms)
  ↓
BACKGROUND:  Worker dequeues task
  ↓
SUPERVISOR:  Analyzes & routes to workers
  ↓
WORKERS:     Execute LangGraph nodes in parallel
  ├─ Preprocess
  ├─ Stream enhanced (+ real-time WebSocket)
  ├─ Extract concepts (parallel)
  ├─ Generate insights (parallel)
  ├─ Build card
  └─ Persist
  ↓
CACHE:       Store result (24h)
  ↓
WEBSOCKET:   Stream events to client
  ├─ Token events (during streaming)
  ├─ Card ready event
  └─ Completion event
  ↓
CLIENT UI:   Display enhanced text + card in real-time
```

---

## Key Performance Metrics

```
Metric                      Target          Actual
────────────────────────────────────────────────────
HTTP Response Time (p50)    < 100ms         ~50-80ms
HTTP Response Time (p99)    < 300ms         ~150-200ms

Cache Hit Rate              > 30%           ~40%
Cache Miss Penalty          < 200ms         ~150ms

WebSocket Connection        < 500ms         ~200-300ms
First Token Latency         < 2s            ~1s

Processing Time             8-12s           ~8-12s
  - With warm cache         -10%            ~7-9s

Worker Success Rate         > 99%           >99%
Queue Depth (p50)           < 10            ~3-5
Queue Depth (p99)           < 100           ~20-30

Database Query              < 50ms          ~10-30ms
Redis Query                 < 10ms          ~2-5ms
```

---

## Architecture Summary

| Layer | Component | Technology | Purpose |
|-------|-----------|-----------|---------|
| 1 | Client | React/Streamlit | Entry point |
| 2 | API Gateway | FastAPI | Route requests |
| 3 | Auth & Validation | JWT + Pydantic | Security |
| 4 | Scheduler | Route handler | Queue tasks |
| 5 | Supervisor | LangGraph | Orchestration |
| 6 | Workers | Python async | Task execution |
| 7 | Workflow | LangGraph nodes | Business logic |
| 8 | Cache | Redis | Performance |
| 9 | Queue | RabbitMQ | Async processing |
| 10 | Database | PostgreSQL | Persistence |# Complete Backend System Flow: Left-to-Right Architecture

## Full System Overview

```
REQUEST FLOW:  Client → API → Auth → Scheduler → Supervisor → Executors → Services → Database
                    ↓      ↓      ↓        ↓           ↓           ↓         ↓         ↓
RESPONSE:      Status  Token  Quota   Queue Task  Graph Node  Worker    Cache/Queue  Persist
```

---

## LAYER 1: CLIENT ENTRY POINT

```yaml
┌────────────────────────────────────────────────┐
│         CLIENT LAYER                           │
│  (React/Streamlit HTTP Request)                │
├────────────────────────────────────────────────┤
│                                                │
│  POST /api/summarize                           │
│  {                                             │
│    "text": "long text...",                     │
│    "style": "technical",                       │
│    "max_length": 500,                          │
│    "Authorization": "Bearer JWT_TOKEN"         │
│  }                                             │
│                                                │
│  Originating from:                             │
│  - React Frontend (http://localhost:3000)      │
│  - Streamlit Admin (http://localhost:8501)     │
│                                                │
└────────────────────────────────────────────────┘
                    │
                    │ HTTP POST
                    │
                    ▼
```

---

## LAYER 2: HTTP API GATEWAY

```yaml
┌─────────────────────────────────────────────────────────────┐
│  FASTAPI ROUTER (app/api/routes/summarize.py)              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  @router.post("/summarize")                                 │
│  async def create_summarization(                            │
│      request: SummarizeRequest,                             │
│      background_tasks: BackgroundTasks,                     │
│      ...                                                    │
│  ) -> ExecutionResponse:                                    │
│                                                             │
│  MIDDLEWARE STACK (Applied before route):                  │
│  ├─ CORS Handler                                           │
│  ├─ Request Logger                                         │
│  ├─ Rate Limiter                                           │
│  ├─ Error Handler                                          │
│  └─ Request Timer                                          │
│                                                             │
│  HTTP Response Code:                                       │
│  ├─ 200: Success (cached)                                  │
│  ├─ 202: Accepted (new task)                               │
│  ├─ 400: Bad Request                                       │
│  ├─ 401: Unauthorized                                      │
│  ├─ 429: Rate Limited                                      │
│  └─ 500: Server Error                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                    │
                    │ Dependency Injection
                    │
                    ▼
```

---

## LAYER 3: AUTHENTICATION & VALIDATION

```yaml
┌──────────────────────────────────────────────────────────────┐
│  AUTH SERVICE (app/services/auth.py)                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Step 1: Extract & Verify JWT Token                          │
│  ├─ Extract from header: "Bearer <token>"                   │
│  ├─ Check signature (RS256 algorithm)                       │
│  ├─ Verify expiration                                       │
│  └─ Extract claims: user_id, email, roles                  │
│                                                              │
│  Step 2: Cache Token (Redis)                                │
│  ├─ Key: auth:token:{user_id}                              │
│  ├─ Value: {"user_id", "email", "roles", "tier"}           │
│  ├─ TTL: 3600 seconds (1 hour)                             │
│  └─ Hit rate: ~90% (saves JWT decode)                      │
│                                                              │
│  Step 3: Check Role-Based Access                           │
│  ├─ Required role: "user" (all) or "admin"                │
│  ├─ Check subscription status                              │
│  ├─ Verify API key not revoked                             │
│  └─ Return: User object or 403 error                       │
│                                                              │
│  Step 4: Check Quota/Rate Limit                            │
│  ├─ Query PostgreSQL: user_quota table                     │
│  ├─ Check: monthly_used < monthly_limit                    │
│  ├─ Update: monthly_used counter                           │
│  └─ Return: QuotaInfo or 429 error                         │
│                                                              │
│  Output:                                                     │
│  {                                                           │
│    "user_id": "uuid",                                        │
│    "email": "user@example.com",                              │
│    "tier": "pro",                                            │
│    "monthly_quota": 1000,                                    │
│    "monthly_used": 342,                                      │
│    "is_authorized": True                                     │
│  }                                                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                    │
                    │ If Auth Fails → Return 401/403/429
                    │
                    ▼ (Auth Success)
│
│  VALIDATION SERVICE (app/api/dependencies.py)
│
│  Step 1: Validate Input (Pydantic)
│  ├─ text: str, length 100-100,000 chars
│  ├─ style: enum ["technical", "casual", "formal"]
│  ├─ max_length: int, 100-2000 range
│  └─ Return: Validated SummarizeRequest
│
│  Step 2: Generate Content Hash
│  ├─ Hash = SHA256(text + style + max_length)
│  ├─ Purpose: Deduplication key
│  └─ Return: Hash string
│
│  Step 3: Create Metadata
│  ├─ char_count, word_count
│  ├─ estimated_processing_time
│  └─ Return: RequestMetadata
│
└──────────────────────────────────────────────────────────────┘
                    │
                    │ (Validated & Authorized)
                    │
                    ▼
```

---

## LAYER 4: SCHEDULER & ROUTING

```yaml
┌──────────────────────────────────────────────────────────────┐
│  ROUTE HANDLER LOGIC                                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  FAST PATH (Cache Hit):                                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ STEP 1: Check Redis Cache                           │    │
│  │ ├─ Key: result:{content_hash}                      │    │
│  │ ├─ TTL: 24 hours                                   │    │
│  │ ├─ Miss rate: ~60% (new requests)                  │    │
│  │ └─ Update execution status to "complete"
│  ├─ Checkpoint: Save persisted state
│  └─ Output: final_result
│  │
│  └──────────────────────────────────────────────────────────┘
│
│  Graph Edges (Execution Flow):
│  preprocess → stream_enhance
│              ↘
│  extract_concepts (parallel to stream_enhance)
│  generate_insights (parallel to stream_enhance)
│              ↓
│  build_card (waits for concepts + insights)
│              ↓
│  persist_results
│              ↓
│  END
│
│  Parallel Execution Benefit:
│  Sequential: 5s + 2s + 3s + 1s = 11s
│  Parallel:   5s (enhance) + 3s (insights) = 8s total
│  Savings: 3 seconds (27% faster)
│
└────────────────────────────────────────────────────────────────┘
                    │
                    │ Results available
                    │
                    ▼ Hit rate: ~40% (duplicate requests)             │    │
│  │                                                     │    │
│  │ If CACHE HIT:                                       │    │
│  │ ├─ Retrieve full result                            │    │
│  │ ├─ Generate new execution_id (for tracking)        │    │
│  │ ├─ Mark as from_cache: True                        │    │
│  │ └─ Return Response (< 100ms)                       │    │
│  │                                                     │    │
│  │ Response:                                           │    │
│  │ {                                                   │    │
│  │   "execution_id": "new-uuid",                      │    │
│  │   "from_cache": True,                              │    │
│  │   "enhanced_text": "...",                          │    │
│  │   "summary_card": {...},                           │    │
│  │   "cached_at": "2026-01-20T10:30:00Z"             │    │
│  │ }                                                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                 │                                            │
│                 │ Cache Miss ▼                               │
│                                                              │
│  SLOW PATH (New Task):                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ STEP 2: Create Execution Record (PostgreSQL)       │    │
│  │ ├─ Table: executions                               │    │
│  │ ├─ Columns:                                        │    │
│  │ │  - id: UUID (primary key)                       │    │
│  │ │  - user_id: UUID (foreign key)                  │    │
│  │ │  - content_hash: VARCHAR                        │    │
│  │ │  - original_text: TEXT                          │    │
│  │ │  - style: ENUM                                  │    │
│  │ │  - max_length: INT                              │    │
│  │ │  - status: ENUM (queued, processing, complete)  │    │
│  │ │  - created_at: TIMESTAMP                        │    │
│  │ │  - completed_at: TIMESTAMP (nullable)           │    │
│  │ └─ Insert new execution record                     │    │
│  │                                                     │    │
│  │ STEP 3: Queue Task to Message Broker (RabbitMQ)   │    │
│  │ ├─ Queue: summarization                            │    │
│  │ ├─ Task Payload:                                   │    │
│  │ │  {                                               │    │
│  │ │    "execution_id": "uuid",                       │    │
│  │ │    "user_id": "uuid",                            │    │
│  │ │    "text": "long text...",                       │    │
│  │ │    "style": "technical",                         │    │
│  │ │    "max_length": 500,                            │    │
│  │ │    "content_hash": "sha256-hash",                │    │
│  │ │    "timestamp": "2026-01-24T10:30:00Z"          │    │
│  │ │  }                                               │    │
│  │ ├─ Priority: 10 (high)                            │    │
│  │ ├─ TTL: 3600 seconds (1 hour)                     │    │
│  │ └─ Acknowledgment: Required                        │    │
│  │                                                     │    │
│  │ STEP 4: Return Execution ID (< 200ms)             │    │
│  │ ├─ Response Code: 202 Accepted                     │    │
│  │ ├─ Response Body:                                  │    │
│  │ │  {                                               │    │
│  │ │    "execution_id": "abc123",                     │    │
│  │ │    "status": "processing",                       │    │
│  │ │    "ws_url": "ws://localhost/ws/abc123",        │    │
│  │ │    "estimated_time_seconds": 8,                 │    │
│  │ │    "from_cache": False                           │    │
│  │ │  }                                               │    │
│  │ └─ Client gets ID immediately                      │    │
│  │                                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                    │
                    │ execution_id queued
                    │
                    ▼
```

---

## LAYER 5: LANGGRAPH SUPERVISOR

```yaml
┌────────────────────────────────────────────────────────────────┐
│  LANGGRAPH SUPERVISOR (app/agents/patterns/supervisor.py)     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Supervisor Graph (StateGraph)                                │
│  ┌──────────────────────────────────────────────────────────┐│
│  │ SupervisorState (TypedDict)                             ││
│  │ ├─ execution_id: str                                    ││
│  │ ├─ task: TaskDefinition                                 ││
│  │ ├─ analysis: AnalysisResult                             ││
│  │ ├─ plan: ExecutionPlan                                  ││
│  │ ├─ worker_tasks: List[WorkerTask]                       ││
│  │ ├─ task_results: Dict[str, Any]                         ││
│  │ ├─ final_result: Any                                    ││
│  │ └─ checkpoints: List[Checkpoint]                        ││
│  └──────────────────────────────────────────────────────────┘│
│                                                                │
│  ┌─────────────────────────────────────────────────────────────┐
│  │ NODE 1: analyze_task                                      │
│  │                                                             │
│  │ Input: execution_id, text, style, max_length             │
│  │                                                             │
│  │ Decisions:                                                 │
│  │ - Is text simple or complex?                            │
│  │   • Complexity = len(text) * number_of_topics           │
│  │   • Simple: < 3000 chars, single topic                 │
│  │   • Complex: >= 3000 chars, multiple topics             │
│  │                                                             │
│  │ - Should run inline or async?                            │
│  │   • Inline: Simple tasks (< 1s processing)             │
│  │   • Async: Complex tasks (> 1s processing)              │
│  │                                                             │
│  │ Checkpoint: Save analysis decision                       │
│  │ {                                                          │
│  │   "stage": "analysis_complete",                          │
│  │   "complexity_score": 7,                                │
│  │   "char_count": 5000,                                   │
│  │   "execution_strategy": "async_workers",                │
│  │   "timestamp": "2026-01-24T10:30:01Z"                  │
│  │ }                                                          │
│  │                                                             │
│  │ Output: AnalysisResult                                   │
│  └─────────────────────────────────────────────────────────────┘
│                      │
│                      ▼
│  ┌─────────────────────────────────────────────────────────────┐
│  │ NODE 2: create_plan                                       │
│  │                                                             │
│  │ Input: AnalysisResult                                     │
│  │                                                             │
│  │ Create task breakdown:                                    │
│  │ ├─ Task 1: Preprocess & Generate Embeddings              │
│  │ ├─ Task 2: Stream Enhanced Text                          │
│  │ ├─ Task 3: Extract Key Concepts (Parallel to 2)          │
│  │ ├─ Task 4: Generate Insights (Parallel to 2)             │
│  │ ├─ Task 5: Build Summary Card (Depends on 3,4)          │
│  │ └─ Task 6: Persist Results (Final step)                 │
│  │                                                             │
│  │ Dependencies Graph:                                       │
│  │ 1 → 2, 3, 4                                               │
│  │ 2 ↘                                                        │
│  │ 3 ──→ 5 → 6                                               │
│  │ 4 ↗                                                        │
│  │                                                             │
│  │ Checkpoint: Save plan                                     │
│  │ {                                                          │
│  │   "stage": "plan_created",                               │
│  │   "tasks": [...],                                        │
│  │   "execution_strategy": "parallel_then_sequential",      │
│  │   "estimated_total_time": 8                              │
│  │ }                                                          │
│  │                                                             │
│  │ Output: ExecutionPlan                                     │
│  └─────────────────────────────────────────────────────────────┘
│                      │
│                      ▼
│  ┌─────────────────────────────────────────────────────────────┐
│  │ NODE 3: route_to_execution (Conditional)                │
│  │                                                             │
│  │ Condition: analysis.execution_strategy == ?              │
│  │                                                             │
│  │ ├─ "inline" ──→ Execute in synchronous path              │
│  │ │  └─ Single LLM call, return quickly                   │
│  │ │                                                         │
│  │ └─ "async_workers" ──→ Queue parallel workers            │
│  │    └─ Multiple workers, coordinate results              │
│  │                                                             │
│  │ This is the critical fork point:                         │
│  │ For text summarization: ALWAYS "async_workers"          │
│  │                                                             │
│  │ Outputs to different downstream nodes                    │
│  └─────────────────────────────────────────────────────────────┘
│         │                              │
│         │ (inline)                     │ (async_workers)
│         ▼                              ▼
│  ┌────────────────────┐      ┌─────────────────────────┐
│  │ Node 4a:           │      │ Node 4b:                │
│  │ Execute Inline     │      │ Queue Worker Tasks      │
│  │                    │      │                         │
│  │ Direct LLM call    │      │ Create 6 worker tasks  │
│  │ Return result      │      │ Queue to RabbitMQ      │
│  │ (fast, < 1s)       │      │ Monitor completion     │
│  │                    │      │ (slower, 8-12s)        │
│  └────────────────────┘      │                         │
│         │                     │ ┌─────────────────────┐│
│         │                     │ │ Task Queue:         ││
│         │                     │ │ ├─ Worker 1: Embed  ││
│         │                     │ │ ├─ Worker 2: Enhance││
│         │                     │ │ ├─ Worker 3: Concepts
│         │                     │ │ ├─ Worker 4: Insights
│         │                     │ │ ├─ Worker 5: Card   ││
│         │                     │ │ └─ Worker 6: Persist││
│         │                     │ └─────────────────────┘│
│         │                     └─────────────────────────┘
│         │                              │
│         └──────────────┬───────────────┘
│                        │
│                        ▼
│  ┌─────────────────────────────────────────────────────────────┐
│  │ NODE 5: aggregate_and_persist                            │
│  │                                                             │
│  │ Combine all results:                                      │
│  │ - enhanced_text from workers                             │
│  │ - summary_card from workers                              │
│  │ - metadata                                                │
│  │                                                             │
│  │ Checkpoint: Save final state                              │
│  │ Persist to PostgreSQL                                     │
│  │ Cache in Redis (24h TTL)                                 │
│  │                                                             │
│  │ Output: FinalResult                                       │
│  └─────────────────────────────────────────────────────────────┘
│                      │
│                      ▼ (END)
│
│  Supervisor Flow Summary:
│  1. Task arrives in queue
│  2. Supervisor analyzes complexity
│  3. Creates execution plan (DAG)
│  4. Routes to inline or async workers
│  5. (Async path) Queues individual worker tasks
│  6. Workers execute in parallel/sequential
│  7. Results aggregated
│  8. Persisted to DB & cached
│
└────────────────────────────────────────────────────────────────┘
                    │
                    │ supervision complete
                    │
                    ▼
```

---

## LAYER 6: EXECUTOR WORKERS

```yaml
┌────────────────────────────────────────────────────────────────┐
│  BACKGROUND WORKERS (app/workers/background_tasks.py)         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Worker Process Flow:                                         │
│  ┌──────────────────────────────────────────────────────────┐│
│  │ Worker Instance (runs 3-5 copies)                       ││
│  │                                                          ││
│  │ LOOP:                                                    ││
│  │  1. Dequeue task from RabbitMQ                          ││
│  │  2. Load checkpoint (if resuming)                       ││
│  │  3. Run LangGraph executor                              ││
│  │  4. Save checkpoint                                     ││
│  │  5. Emit result to Pub/Sub                              ││
│  │  6. Acknowledge task                                    ││
│  │  7. Next iteration                                      ││
│  │                                                          ││
│  └──────────────────────────────────────────────────────────┘│
│                                                                │
│  Task Dequeue (RabbitMQ):                                     │
│  ├─ Queue: summarization                                    │
│  ├─ Prefetch: 1 (each worker handles 1 task)               │
│  ├─ Timeout: 300 seconds (5 minutes)                        │
│  └─ Auto-ACK: False (manual acknowledgment)                 │
│                                                                │
│  Worker State:                                                │
│  {                                                            │
│    "execution_id": "abc123",                                 │
│    "task_input": {...},                                      │
│    "iterations": 0,                                          │
│    "checkpoint_data": None,  # Loaded from Redis            │
│    "result": None                                            │
│  }                                                            │
│                                                                │
│  Executor (LangGraphWorkerExecutor):                         │
│  ├─ Converts worker state to LangGraph state                │
│  ├─ Runs the LangGraph workflow                             │
│  ├─ Converts output back to worker state                    │
│  └─ Handles streaming via Redis Pub/Sub                     │
│                                                                │
│  Checkpoint Management:                                       │
│  ├─ Key: execution:{execution_id}:{stage}                   │
│  ├─ Stored in PostgreSQL (checkpoints table)                │
│  ├─ Used for resumability on worker crash                   │
│  ├─ TTL: 1 hour (auto-cleanup)                             │
│  └─ Each node saves state                                   │
│                                                                │
│  Error Handling:                                              │
│  ├─ Max retries: 3                                          │
│  ├─ Backoff strategy: exponential (2^n seconds)             │
│  ├─ Retry queue: summarization_retry                        │
│  ├─ Dead letter queue: summarization_dlq                    │
│  └─ Alert sent on DLQ entry                                 │
│                                                                │
│  Worker Health:                                               │
│  ├─ Heartbeat: every 30 seconds                            │
│  ├─ Metric: tasks_processed_counter                         │
│  ├─ Metric: tasks_failed_counter                            │
│  ├─ Metric: processing_time_histogram                       │
│  └─ Alert if no heartbeat for 2 minutes                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
                    │
                    │ Worker processes LangGraph nodes
                    │
                    ▼
```

---

## LAYER 7: LANGGRAPH WORKFLOW NODES

```yaml
┌────────────────────────────────────────────────────────────────┐
│  LANGGRAPH WORKER EXECUTOR NODES                              │
│  (app/workers/langgraph_workflow.py)                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐│
│  │ SummarizationWorkflow Graph                             ││
│  │                                                          ││
│  │ NODE 1: preprocess                                       ││
│  │ ├─ Input: raw text                                      ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ Clean text (remove extra whitespace)            ││
│  │ │  ├─ Check embeddings cache (Redis)                 ││
│  │ │  ├─ If not cached: Generate embeddings (LLM)       ││
│  │ │  └─ Cache embeddings (1 hour TTL)                  ││
│  │ ├─ Checkpoint: Save embeddings                        ││
│  │ └─ Output: preprocessed_state                         ││
│  │                                                          ││
│  │ NODE 2: stream_enhance                                  ││
│  │ ├─ Input: embeddings, text, style                     ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ LLM streaming call                             ││
│  │ │  ├─ For each token:                                ││
│  │ │  │  ├─ Accumulate to enhanced_text                 ││
│  │ │  │  ├─ Emit token to Redis Pub/Sub                 ││
│  │ │  │  │  Key: execution:{id}:events                  ││
│  │ │  │  │  Message: {"type": "streaming_token", ...}  ││
│  │ │  │  └─ WebSocket receives & streams to client      ││
│  │ │  ├─ Cache full enhanced text                        ││
│  │ │  └─ Emit completion event                           ││
│  │ ├─ Checkpoint: Save enhanced_text                     ││
│  │ └─ Output: enhanced_text                              ││
│  │                                                          ││
│  │ NODE 3: extract_concepts (PARALLEL)                    ││
│  │ ├─ Input: enhanced_text, embeddings                   ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ Use semantic understanding                      ││
│  │ │  ├─ LLM extracts key concepts                       ││
│  │ │  ├─ Limited to 8 concepts                           ││
│  │ │  └─ Cache concepts                                   ││
│  │ ├─ Checkpoint: Save concepts                          ││
│  │ └─ Output: concepts list                              ││
│  │                                                          ││
│  │ NODE 4: generate_insights (PARALLEL)                  ││
│  │ ├─ Input: concepts, enhanced_text                     ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ Analyze deeper meaning                          ││
│  │ │  ├─ LLM generates insights                          ││
│  │ │  ├─ Limited to 5 insights                           ││
│  │ │  └─ Cache insights                                   ││
│  │ ├─ Checkpoint: Save insights                          ││
│  │ └─ Output: insights list                              ││
│  │                                                          ││
│  │ NODE 5: build_card                                      ││
│  │ ├─ Input: concepts, insights, enhanced_text, metadata ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ Calculate metadata                              ││
│  │ │  │  ├─ reading_time = word_count / 200             ││
│  │ │  │  ├─ char_count, word_count                      ││
│  │ │  │  └─ generated_at timestamp                       ││
│  │ │  ├─ Structure card JSON                            ││
│  │ │  │  ├─ title (from first concept)                  ││
│  │ │  │  ├─ summary (first 200 chars)                   ││
│  │ │  │  ├─ key_points (concepts)                       ││
│  │ │  │  ├─ insights (generated insights)               ││
│  │ │  │  └─ metadata (reading time, etc.)               ││
│  │ │  └─ Cache card                                      ││
│  │ ├─ Checkpoint: Save card                              ││
│  │ └─ Output: summary_card                               ││
│  │                                                          ││
│  │ NODE 6: persist_results                                ││
│  │ ├─ Input: enhanced_text, card, concepts, insights     ││
│  │ ├─ Process:                                             ││
│  │ │  ├─ Save to PostgreSQL (results table)             ││
│  │ │  │  ├─ id, enhanced_text, summary_card            ││
│  │ │  │  ├─ concepts, insights, metadata               ││
│  │ │  │  └─ created_at                                  ││
│  │ │  ├─ Cache complete result (24h)                    ││
│  │ │  │  Key: result:{content_hash}                    ││
│  │ │  │  Value: full result object                     ││
│  │ │  ├─ Emit completion event to Pub/Sub             ││
│  │ │  │  Message: {"type": "execution_complete", ...} ││
│  │ │  └─