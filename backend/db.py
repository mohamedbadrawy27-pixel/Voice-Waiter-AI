
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CA_CERT = BASE_DIR / "backend" / "ca.pem"

# Load environment variables
load_dotenv(BASE_DIR / ".env")


# Database configuration
connection_url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)


# Create database engine
engine = create_engine(
    connection_url,
    connect_args={
        "ssl": {
            "ca": str(CA_CERT)
        }
    },
    pool_pre_ping=True
)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connected successfully!")
        print(result.scalar())
