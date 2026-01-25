# System Architecture – Mermaid Diagrams

## 1. End-to-End Request Flow (Left → Right)

```mermaid
flowchart LR
    Client["Client<br/>(React / Streamlit)"]
    API["FastAPI Gateway<br/>routes/summarize.py"]
    Auth["Auth & Validation<br/>(JWT · Quota · Rate Limit)"]
    Cache["Redis Cache<br/>(result_hash)"]
    MQ["RabbitMQ<br/>(summarization_queue)"]

    Client --> API
    API --> Auth
    Auth --> Cache

    Cache -- "cache hit" --> Client
    Cache -- "cache miss" --> MQ


```

---

## 2. Worker Execution Pipeline (Inside the Queue Consumer)

```mermaid
flowchart LR
    Task["Queue Task<br/>(execution_id)"]

    Pre["Preprocessing<br/>(clean · chunk · embed)"]
    Stream["Streaming Enhancement<br/>(LLM tokens)"]
    Concepts["Concept Extraction"]
    Insights["Insight Generation"]
    Build["Summary Card Builder"]
    Persist["Persist Result<br/>(DB / Cache)"]
    Done["Execution Complete"]

    Task --> Pre

    Pre --> Stream
    Pre --> Concepts
    Pre --> Insights

    Stream --> Build
    Concepts --> Build
    Insights --> Build

    Build --> Persist
    Persist --> Done

```

---

## 3.Streaming & State Propagation (Worker ↔ Client)

```mermaid
sequenceDiagram
    participant W as Worker
    participant R as Redis (Pub/Sub)
    participant C as Client (WebSocket)

    W->>R: publish(stream_token)
    R->>C: ws:event(stream_token)

    W->>R: publish(enhanced_text_ready)
    R->>C: ws:event(enhanced_text)

    W->>R: publish(summary_card)
    R->>C: ws:event(final_payload)

    W->>R: publish(execution_complete)


```

---

## 4. Supervisor / Planner Logic (LangGraph Control Plane)

```mermaid
flowchart LR
    Input["Incoming Task"]
    Analyze["Analyze Request"]
    Plan["Create LangGraph Plan"]
    Route["Route to Worker Executor"]

    Input --> Analyze --> Plan --> Route


```
