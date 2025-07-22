# 🚀 Development Guide

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.9+
- Docker 
- Supabase CLI
- Fly.io CLI
- Ollama (for local LLM)
- Rust (for Gemini CLI)
- Notion account
- Git LFS (for model storage)
- Sentry CLI (for monitoring)

### Installing Gemini CLI

1. Clone the open-source Gemini CLI:
   ```bash
   git clone https://github.com/gemini-pad/gemini-cli
   cd gemini-cli
   cargo build --release
   ```

2. Add to PATH:
   ```bash
   # Add to your Windows PATH
   set PATH=%PATH%;%CD%\target\release
   ```

### Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   pip install -r requirements.txt
   ```
3. Set up local environment:
   ```bash
   cp .env.example .env
   ```
4. Start local Supabase:
   ```bash
   supabase start
   ```
5. Run development server:
   ```bash
   npm run dev
   ```

## Testing

### Unit Tests
```bash
npm test
pytest tests/
```

### Integration Tests
```bash
npm run test:integration
pytest tests/integration/
```

### E2E Tests
```bash
npm run test:e2e
pytest tests/e2e/
```

## Deployment

### Development
```bash
fly deploy --remote-only
```

### Production
```bash
fly deploy --app production
```

## Environment Variables

### Required Variables
```bash
# Database
SUPABASE_URL=
SUPABASE_KEY=

# Payments
STRIPE_KEY=
STRIPE_WEBHOOK_SECRET=

# Communication
TELEGRAM_TOKEN=
DISCORD_TOKEN=
NOTION_API_KEY=
NOTION_DATABASE_ID=

# AI Services
OPENROUTER_API_KEY=
GEMINI_MODEL_PATH=./models/trading-assistant

# Monitoring
SENTRY_DSN=
```

### Optional Variables
```bash
# Development
DEBUG=true
LOG_LEVEL=debug
NODE_ENV=development

# Performance
CACHE_DURATION=3600
MAX_RETRIES=3
RATE_LIMIT=100

# AI Configuration
AI_TEMPERATURE=0.7
MAX_TOKENS=2048
USE_LOCAL_LLM=true
```

## Common Issues

### Supabase Connection
If you can't connect to local Supabase:
1. Check if services are running: `supabase status`
2. Verify environment variables
3. Reset if needed: `supabase db reset`

### Payment Processing
If Stripe webhooks fail:
1. Check webhook endpoint in Stripe Dashboard
2. Verify STRIPE_KEY is correct
3. Check webhook logs in Supabase

### Bot Commands
If bot commands don't work:
1. Verify bot tokens
2. Check rate limiting settings
3. Review bot logs

## Best Practices

### Code Style
- Follow PEP 8 for Python
- Use ESLint for JavaScript/TypeScript
- Write clear commit messages

### Security
- Never commit secrets
- Use environment variables
- Implement rate limiting
- Validate all inputs

### Testing
- Write tests for new features
- Run full test suite before deployment
- Use CI/CD pipeline
