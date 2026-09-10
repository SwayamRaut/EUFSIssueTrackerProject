# app/dependencies.py
from functools import lru_cache

class Settings:
    data_dir: str = "data"
    issues_file: str = "issues.json"
    components_file: str = "components.json"

@lru_cache
def get_settings() -> Settings:
    return Settings()