# 📘 Getting Started Guide

## Introduction

This guide will help you get started with the Binance Automation Trading Bot project.

## Prerequisites

Before you begin, ensure you have:

- Node.js 18+ installed
- Python 3.9+ installed
- Docker installed
- A Binance account
- Basic understanding of trading concepts

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/binance-automation-bot.git

# Install dependencies
cd binance-automation-bot
npm install
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

### 3. Development

```bash
# Start local services
supabase start
npm run dev
```

## Basic Usage

### Telegram Commands

- `/start` - Begin bot interaction
- `/status` - Check subscription status
- `/trade` - View recent trades
- `/help` - Get command list

### Web Dashboard

1. Navigate to `http://localhost:3000`
2. Log in with your credentials
3. Access trading dashboard

## Next Steps

1. Read the [Technical Architecture](./technical-architecture.md)
2. Review the [Development Guide](./development-guide.md)
3. Check [Project Structure](./project-structure.md)
4. Join our Discord community

## Support

- GitHub Issues: [Report bugs](https://github.com/yourusername/binance-automation-bot/issues)
- Discord: [Join community](https://discord.gg/yourinvite)
- Documentation: [Read more](https://docs.yourdomain.com)
