from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker

from database import engine
from main import app

# warningを無視する
def pytest_collection_modifyitems(config, items):
    config.addinivalue_line("filterwarnings", "ignore::DeprecationWarning")

@pytest.fixture
def db() -> Generator:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def fake():
    return Faker()
