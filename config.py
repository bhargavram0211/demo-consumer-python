"""
Configuration file for the demo application
"""

import os

class Config:
    """Base configuration"""
    
    # Application Settings
    APP_NAME = "Demo Consumer API"
    VERSION = "1.0.0"
    DEBUG = True
    
    # INTENTIONAL TEST SECRET - Slack Webhook
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
    
    # INTENTIONAL TEST SECRET - Stripe API Key
    STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dcTESTKEY"
    
    # INTENTIONAL TEST SECRET - SendGrid API Key
    SENDGRID_API_KEY = "SG.xxxxxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    
    # Database Configuration (using environment variables - CORRECT WAY)
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    # Note: DB password should come from environment, not hardcoded
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')  # Get from environment!
    
    # Redis Configuration
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    
    # INTENTIONAL TEST SECRET - JWT Secret Key
    JWT_SECRET_KEY = "super-secret-jwt-key-that-should-never-be-committed-12345"
    
    # INTENTIONAL TEST SECRET - Private SSH Key (partial)
    # PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
    # MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyz...
    # -----END RSA PRIVATE KEY-----"""
    
    # Feature Flags
    ENABLE_API_RATE_LIMITING = True
    ENABLE_CORS = True
    MAX_REQUESTS_PER_MINUTE = 60


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # In production, all secrets should come from secure sources like:
    # - Environment variables
    # - AWS Secrets Manager
    # - HashiCorp Vault
    # - Azure Key Vault
    # etc.


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
