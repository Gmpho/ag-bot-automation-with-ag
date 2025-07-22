# 📋 Project Instructions and Guidelines

## Project Overview

The Binance Automation Trading Bot is a sophisticated automated trading system that leverages AI and modern cloud infrastructure for efficient cryptocurrency trading.

## Core Principles

1. **Code Quality**
   - Follow PEP 8 style for Python
   - Use TypeScript for frontend
   - Maintain comprehensive documentation
   - Write clear commit messages

2. **AI Integration**
   - Use local LLM when possible
   - Implement fallback mechanisms
   - Cache AI responses appropriately
   - Validate AI suggestions before execution

3. **Security**
   - Validate all inputs
   - Implement rate limiting
   - Use role-based access control
   - Follow security best practices

4. **Documentation**
   - Keep Notion workspace updated
   - Document all API endpoints
   - Maintain clear code comments
   - Update technical diagrams

## Development Workflow

1. **Feature Development**
   - Create feature branch
   - Write tests first
   - Implement feature
   - Update documentation
   - Submit PR for review

2. **Code Review Process**
   - Automated Gemini review
   - Human peer review
   - Security check
   - Performance analysis

3. **Deployment**
   - Test in staging
   - Verify monitoring
   - Gradual rollout
   - Monitor metrics

## Best Practices

### Python Code
```python
# Example of good Python code style
from typing import Dict, Any

class TradingStrategy:
    """Trading strategy implementation with AI integration."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize trading strategy with configuration."""
        self.config = config
        self.validate_config()
    
    def validate_config(self) -> None:
        """Validate strategy configuration."""
        required_fields = ['risk_level', 'max_position']
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field: {field}")
```

### TypeScript Code
```typescript
// Example of good TypeScript code style
interface TradingConfig {
  riskLevel: 'low' | 'medium' | 'high';
  maxPosition: number;
}

class StrategyManager {
  private config: TradingConfig;
  
  constructor(config: TradingConfig) {
    this.config = this.validateConfig(config);
  }
  
  private validateConfig(config: TradingConfig): TradingConfig {
    if (!['low', 'medium', 'high'].includes(config.riskLevel)) {
      throw new Error('Invalid risk level');
    }
    return config;
  }
}
```

## Documentation Standards

1. **Code Documentation**
   - Clear function docstrings
   - Type hints
   - Usage examples
   - Edge cases noted

2. **API Documentation**
   - OpenAPI/Swagger specs
   - Request/response examples
   - Error scenarios
   - Rate limits

3. **Architecture Documentation**
   - Component diagrams
   - Data flow
   - Integration points
   - Security measures

## Monitoring and Maintenance

1. **Performance Monitoring**
   - Use Sentry for errors
   - Monitor API latencies
   - Track AI response times
   - Log trading performance

2. **Security Monitoring**
   - Track failed auth attempts
   - Monitor API usage
   - Check for unusual patterns
   - Regular security audits

## Communication

1. **Team Communication**
   - Use Discord for daily updates
   - Notion for documentation
   - GitHub for code reviews
   - Email for formal communication

2. **User Communication**
   - Telegram for alerts
   - Email for reports
   - Discord for community
   - Web UI for dashboard
