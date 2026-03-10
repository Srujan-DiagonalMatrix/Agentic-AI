# Agentic-AI
This is a simple Agentic AI project for a simple demo

### Project Architecture
```text
┌──────────────────────────────────────────────┐
│                Simple Web UI                 │
│      React or plain HTML/JS frontend         │
│  Chat box + tool trace + task/reminder view  │
└──────────────────────┬───────────────────────┘
                       │ HTTP
                       ▼
┌──────────────────────────────────────────────┐
│                 FastAPI App                  │
│  - /chat                                     │
│  - /tasks                                    │
│  - /reminders                                │
│  - /health                                   │
│  - /audit                                    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              Agent Orchestrator              │
│  - receives user goal                        │
│  - decides tool sequence                     │
│  - calls MCP tools                           │
│  - combines outputs                          │
│  - returns final answer + trace              │
└───────────────┬─────────────────────┬────────┘
                │                     │
                │                     ▼
                │          ┌──────────────────────┐
                │          │  Azure OpenAI LLM    │
                │          │  reasoning/planning  │
                │          └──────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│                 MCP Server                   │
│   exposes all business tools in one place    │
└───────┬───────────┬───────────┬──────────────┘
        │           │           │
        ▼           ▼           ▼
┌─────────────┐ ┌───────────┐ ┌─────────────────┐
│ RAG Tools   │ │ M365 Tools│ │ HubSpot Tools   │
│ local docs  │ │ email/cal │ │ CRM read/write  │
└─────┬───────┘ └─────┬─────┘ └────────┬────────┘
      │               │                │
      ▼               ▼                ▼
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ Ollama      │ │ Microsoft    │ │ HubSpot CRM  │
│ Embeddings  │ │ Graph API    │ │ API          │
└─────┬───────┘ └──────────────┘ └──────────────┘
      │
      ▼
┌─────────────┐
│ Vector DB   │
│ pgvector or │
│ Chroma      │
└─────────────┘
```

Additional supporting tools:
- Google Search tool
- Reminder scheduler
- Postgres app database
- Local audit/logging

### Folder plan
```text
agentic_ai_mvp/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── agent.py
│   ├── prompts.py
│   ├── dependencies.py
│   │
│   ├── api/
│   │   ├── routes_chat.py
│   │   ├── routes_tasks.py
│   │   ├── routes_reminders.py
│   │   ├── routes_health.py
│   │   └── schemas.py
│   │
│   ├── llm/
│   │   ├── azure_openai_client.py
│   │   └── ollama_embeddings.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── retriever.py
│   │   ├── chunking.py
│   │   └── vectorstore.py
│   │
│   ├── mcp/
│   │   ├── server.py
│   │   ├── tool_registry.py
│   │   └── schemas.py
│   │
│   ├── tools/
│   │   ├── knowledge_tools.py
│   │   ├── hubspot_tools.py
│   │   ├── outlook_tools.py
│   │   ├── task_tools.py
│   │   ├── reminder_tools.py
│   │   ├── search_tools.py
│   │   └── audit_tools.py
│   │
│   ├── db/
│   │   ├── postgres.py
│   │   ├── models.py
│   │   ├── repositories.py
│   │   └── migrations/
│   │
│   ├── services/
│   │   ├── task_service.py
│   │   ├── reminder_service.py
│   │   ├── audit_service.py
│   │   └── scheduler_service.py
│   │
│   └── ui/
│       └── optional frontend files
│
├── data/
│   └── raw_docs/
│
├── scripts/
│   ├── ingest_docs.py
│   ├── seed_tasks.py
│   └── run_scheduler.py
│
├── tests/
├── .env
├── requirements.txt
└── README.md
```

### Exact role of each major module
#### 1. agent.py
Main orchestrator. Receives a user request, decides tools, calls MCP tools, and creates the final answer.

#### 2. mcp/server.py
Exposes all tools to the agent in MCP format. MCP is specifically designed for tools and resources that LLM applications can invoke.

#### 3. llm/azure_openai_client.py
Calls Azure OpenAI for reasoning and final responses.

#### 4. llm/ollama_embeddings.py
Creates embeddings for documents and queries.

#### 5. rag/
Handles ingestion, chunking, and retrieval of local documents.

#### 6. tools/hubspot_tools.py
Reads HubSpot contacts, deals, and notes, and can create CRM notes.

#### 7. tools/outlook_tools.py
Drafts Outlook emails and creates Outlook calendar events using Microsoft Graph.

#### 8. tools/reminder_tools.py
Creates reminders in Postgres.

#### 9. services/scheduler_service.py
Checks due reminders and marks them ready for notification or action.

#### 10. db/
Stores tasks, reminders, logs, and configuration.