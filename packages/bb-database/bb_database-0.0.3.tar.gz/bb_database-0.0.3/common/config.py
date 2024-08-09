import os
from pathlib import Path

from dotenv import load_dotenv


base_dir = Path.cwd()
env_path = base_dir / ".env"
load_dotenv(dotenv_path=env_path)


DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = int(os.environ["DB_PORT"])

SCHEMA = os.environ["DB_SCHEMA"]
VERSION_TABLE_NAME = "bb_alembic_version"

CONNECTION_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/bb_database"
)
