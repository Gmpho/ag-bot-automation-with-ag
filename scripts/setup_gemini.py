#!/usr/bin/env python3
"""
Gemini CLI Setup and Integration Script
"""
import os
import yaml
import shutil
from pathlib import Path

def setup_gemini_environment():
    """Setup Gemini CLI environment and directories"""
    # Create necessary directories
    directories = [
        './models/trading-assistant',
        './.cache/gemini',
        './logs/gemini',
        './.cache/langchain'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def validate_configuration():
    """Validate Gemini configuration"""
    config_file = Path('./config/gemini.yml')
    
    if not config_file.exists():
        raise FileNotFoundError("Gemini configuration file not found!")
        
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
        
    required_keys = ['model', 'local', 'trading', 'code_review']
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required configuration section: {key}")
            
    print("Configuration validation successful!")

def setup_model_integration():
    """Setup model integration with Ollama"""
    # Check if Ollama is running
    if os.system("curl -s http://localhost:11434/health > /dev/null") != 0:
        print("Warning: Ollama is not running. Please start Ollama for fallback support.")
    else:
        print("Ollama integration verified!")

def main():
    try:
        print("Starting Gemini CLI setup...")
        
        # Setup directories
        setup_gemini_environment()
        
        # Validate configuration
        validate_configuration()
        
        # Setup model integration
        setup_model_integration()
        
        print("\nGemini CLI setup completed successfully!")
        print("\nNext steps:")
        print("1. Update your .env file with Gemini configuration")
        print("2. Start your development server")
        print("3. Run initial tests with 'python scripts/test_gemini.py'")
        
    except Exception as e:
        print(f"Error during setup: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
