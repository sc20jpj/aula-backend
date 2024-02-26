import os
import pytest
import random
import string
from dotenv import load_dotenv
from src.run import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })


    yield app
@pytest.fixture(scope="session",autouse=True)
def load_env():
    """
    Fixture to load environment variables from .env file
    """
    load_dotenv('.env')

@pytest.fixture(scope="function")
def random_code():
    """
    Fixture to generate a random string for the code attribute
    """
    length = 10  # Length of the random string
    characters = string.ascii_letters + string.digits  # Characters to choose from
    return ''.join(random.choice(characters) for _ in range(length))


@pytest.fixture(scope="session")
def bearer_token(load_env):
    """
    Fixture to get bearer token from environment variable
    """
    token = os.getenv('BEARER')
    if not token:
        raise ValueError("Bearer token not found in .env file")
    return token


@pytest.fixture(autouse=True)
def client(app):
    return app.test_client()
