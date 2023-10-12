import os
from Chroma.config import Settings

CHROMA_SETTINGS = Settings(
    chroma_db_impl = 'sqlite',
    persist_directory = "db",
    anonymized_telementry = False,
)