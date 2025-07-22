# 📁 Project Structure Documentation

## Overview
Detailed breakdown of the project's file and folder organization.

## Root Structure
```bash
automation-with-ag-bot/
├── apps/
│   ├── web-ui/                # Next.js + Tailwind dashboard UI
│   ├── telegram-bot/          # Telegram bot Python handlers + commands
│   └── discord-bot/           # Discord bot commands & alerts
├── packages/
│   ├── core/                  # Core trade logic, utils, API clients
│   ├── ai-agents/            # AI integration (LangChain, Gemini, Ollama)
│   └── docs/                 # Notion integration and documentation sync
├── infra/
│   ├── docker/               # Dockerfiles, container configs
│   ├── fly/                 # Fly.io deployment config (fly.toml)
│   └── notion/              # Notion workspace templates and config
├── scripts/                   # CLI scripts (trade runner, db cleanup)
├── tests/                     # Unit + integration tests (pytest)
├── .github/workflows/         # CI/CD workflows (GitHub Actions)
├── config/                    # Configs: OpenRouter, supabase, stripe, secrets.env
├── README.md
└── Dockerfile
```

## Detailed Structure
```bash
automation-with-ag-bot/
├── app/
│   └── components/SubscribeButton.tsx
├── pages/
│   ├── api/
│   │   ├── auth/
│   │   │   └── [...nextauth].ts
│   │   ├── create-checkout-session.ts
│   │   ├── subscription-status.ts
│   │   └── webhook.ts
│   └── auth/telegram-login.ts
├── telegram_bot/
│   ├── commands/
│   │   ├── auth.ts
│   │   └── payment.ts
│   └── index.ts
├── lib/
│   ├── db.ts
│   ├── payments.ts
│   ├── stripeClient.ts
│   ├── authGuard.ts
│   └── your_tools.ts
├── tests/
│   ├── test_tools.py
│   ├── test_agent_executor.py
│   ├── test_prompts.py
│   └── test_agent_evals.py
└── .github/workflows/
    ├── ci.yml
    └── staging-deploy.yml
```
