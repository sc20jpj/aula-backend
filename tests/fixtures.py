import os
import pytest
import random
import string
import boto3
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
def bearer_token():
    client = boto3.client('cognito-idp',region_name=os.getenv("REGION"))
    print(os.getenv("COGNITO_USERNAME"))
    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': os.getenv("COGNITO_USERNAME"),
                'PASSWORD': os.getenv("COGNITO_PASSWORD")
            },
            ClientId=os.getenv("CLIENT_ID"),


        )

        return response['AuthenticationResult']['AccessToken']

    except client.exceptions.NotAuthorizedException as e:
        print("Authentication failed:", e)
    except client.exceptions.UserNotFoundException as e:
        print("User not found:", e)
    except Exception as e:
        print("Error:", e)



@pytest.fixture(autouse=True)
def client(app):
    return app.test_client()
