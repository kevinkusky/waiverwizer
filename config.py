"""config.py"""
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@localhost/waiverwizer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
