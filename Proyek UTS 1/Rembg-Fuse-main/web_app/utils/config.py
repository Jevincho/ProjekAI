"""
Configuration module for Rembg-Fuse Web App
"""

import os
from pathlib import Path

class Config:
    """Base configuration"""
    
    # Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('FLASK_ENV', 'production') == 'development'
    
    # Upload config
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'}
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size
    
    # Processing config
    ALLOWED_MODELS = ['u2netp', 'u2net', 'isnet-general-use', 'silueta', 'birefnet-general']
    DEFAULT_MODEL = 'u2netp'
    
    # Cleanup config (remove old files after N hours)
    FILE_CLEANUP_AGE_HOURS = 24

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'test_uploads')
