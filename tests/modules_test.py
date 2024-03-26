import json
import os

from http import HTTPStatus
from tests.fixtures import load_env,bearer_token,client,app,random_code


def test_add_module(client,bearer_token ,random_code):
    
    data = {
        "name": "Example Module",
        "code": random_code  
    }


    response_unauth = client.post("/modules", data=json.dumps(data))

    assert response_unauth.status_code == HTTPStatus.UNAUTHORIZED

    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = client.post("/modules", data=json.dumps(data),headers=headers)

    print(response.json)
    assert response.status_code == HTTPStatus.OK 
    assert response.json["data"]["name"] == data["name"] and response.json["data"]["code"] == data["code"]

def test_delete_module(client,bearer_token ,random_code):

    data = {
        "name": "Example Module",
        "code": random_code  
    }
    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response_post = client.post("/modules", data=json.dumps(data),headers=headers)
    assert  response_post.status_code == HTTPStatus.OK

    module_id = response_post.json["data"]["id"] 

    response_delete = client.delete(f"/modules/{module_id}", headers=headers)

    delete_id = response_delete.json["data"]["id"]
    print("delete response is " ,response_delete)
    assert  response_delete.status_code == HTTPStatus.OK and delete_id == module_id




# assumes user has modules will fail otherwise 
def test_all_modules_for_user(client,bearer_token):
    headers = {
        "Content-Type": "application/json"
    }
    response_unatuh = client.get("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", headers=headers)
    assert response_unatuh.status_code == HTTPStatus.UNAUTHORIZED

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = client.get("/modules/>", headers=headers)

    assert response.status_code == HTTPStatus.OK
