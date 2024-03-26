import json
import os
import base64

from http import HTTPStatus
from tests.fixtures import load_env,bearer_token,client,app,random_code


# assumes modules has lessons will fail otherwise 
def test_all_documents_for_lessson(client,bearer_token ,random_code):

    headers = {
        "Content-Type": "application/json"
    }
    response_unatuh = client.get("/documents/e522270f-61b6-4bb8-a57c-a1b1b0004c3c", headers=headers)
    assert response_unatuh.status_code == HTTPStatus.UNAUTHORIZED
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    # assumes user has modules will fail otherwise 

    print(bearer_token)
    response = client.get("/documents/e522270f-61b6-4bb8-a57c-a1b1b0004c3c", headers=headers)

    assert response.status_code == HTTPStatus.OK