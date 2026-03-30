import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Application
    app_name: str = "Bulk Email Sender Pro"
    app_version: str = "2.0.0"
    debug: bool = os.getenv("DEBUG", "False") == "True"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/bulk_email")
    database_async_url: str = os.getenv("DATABASE_ASYNC_URL", "postgresql+asyncpg://user:password@localhost:5432/bulk_email")
    
    # Redis
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # JWT
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    # Email
    smtp_server: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port: int = int(os.getenv("SMTP_PORT", 587))
    smtp_username: str = os.getenv("SMTP_USERNAME", "")
    smtp_password: str = os.getenv("SMTP_PASSWORD", "")
    smtp_from_email: str = os.getenv("SMTP_FROM_EMAIL", "noreply@example.com")
    smtp_from_name: str = os.getenv("SMTP_FROM_NAME", "Bulk Email Sender")
    sendgrid_api_key: str = os.getenv("SENDGRID_API_KEY", "")
    
    # CORS
    cors_origins: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # Rate Limiting
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", 100))
    rate_limit_per_hour: int = int(os.getenv("RATE_LIMIT_PER_HOUR", 5000))
    
    # Email Limits
    max_recipients_per_campaign: int = int(os.getenv("MAX_RECIPIENTS_PER_CAMPAIGN", 10000))
    max_campaigns_per_day: int = int(os.getenv("MAX_CAMPAIGNS_PER_DAY", 100))
    emails_per_second: int = int(os.getenv("EMAILS_PER_SECOND", 10))
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()