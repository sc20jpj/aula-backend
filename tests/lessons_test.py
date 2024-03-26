import json
import os
import base64

from http import HTTPStatus
from tests.fixtures import load_env,bearer_token,client,app,random_code

def test_add_file(client,bearer_token ,random_code):
    # powerpoint 
    with open("powerpoint_test.pptx", "rb") as file1:
        file_contents = file1.read()
        base64_string_file_1 = base64.b64encode(file_contents).decode('utf-8')
    # pdf 
    with open("pdf_test.pdf", "rb") as file2:
        file_contents = file2.read()
        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 
    # image 
    with open("image_test.png", "rb") as file3:
        file_contents = file3.read()
        base64_string_file_3 = base64.b64encode(file_contents).decode('utf-8')
        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 




        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

    data = {
            "name": "lesson 1",
            "description": "Test_lesson",
            "files": [
                {   
                    "name": "image_test.png",
                    "base64": base64_string_file_1
                },
                {
                    "name": "pdf_test.pdf",
                    "base64": base64_string_file_2
                },
                {
                    "name": "powerpoint_test.pptx",
                    "base64": base64_string_file_3
                }

                
            ]

    }
    #  this should be change to use a constant 
    response_unauth = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data))

    assert response_unauth.status_code == HTTPStatus.UNAUTHORIZED

    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data),headers=headers)

    print(response.json)
    assert response.status_code == HTTPStatus.OK 
    assert response.json["data"]["name"] == data["name"] and response.json["data"]["description"] == data["description"]




def test_get_lessons_per_module(client,bearer_token ,random_code):
    # powerpoint 
    with open("powerpoint_test.pptx", "rb") as file1:
        file_contents = file1.read()
        base64_string_file_1 = base64.b64encode(file_contents).decode('utf-8')
    # pdf 
    with open("pdf_test.pdf", "rb") as file2:
        file_contents = file2.read()
        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 
    # image 
    with open("image_test.png", "rb") as file3:
        file_contents = file3.read()
        base64_string_file_3 = base64.b64encode(file_contents).decode('utf-8')
        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 




        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

    data = {
            "name": "lesson 1",
            "description": "Test_lesson",
            "files": [
                {   
                    "name": "file1",
                    "base64": base64_string_file_1
                },
                {
                    "name": "file2",
                    "base64": base64_string_file_2
                },
                {
                    "name": "image_file",
                    "base64": base64_string_file_3
                }

                
            ]

    }



    response_unauth = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data))

    assert response_unauth.status_code == HTTPStatus.UNAUTHORIZED

    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data),headers=headers)

    print(response.json)
    assert response.status_code == HTTPStatus.OK 
    assert response.json["data"]["name"] == data["name"] and response.json["data"]["description"] == data["description"]





# assumes modules has lessons will fail otherwise 
def test_all_lessons_for_module(client,bearer_token):


    headers = {
        "Content-Type": "application/json"
    }
    response_unatuh = client.get("/lessons/all/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", headers=headers)
    assert response_unatuh.status_code == HTTPStatus.UNAUTHORIZED
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    # assumes user has modules will fail otherwise 

    response = client.get("/lessons/all/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", headers=headers)

    assert response.status_code == HTTPStatus.OK

# assumes modules has lessons will fail otherwise 
def test_full_lesson(client,bearer_token ,random_code):

    headers = {
        "Content-Type": "application/json"
    }
    response_unatuh = client.get("/lessons/b473ce4f-dc92-4236-8f4d-1b6b9e2c1ac6", headers=headers)
    assert response_unatuh.status_code == HTTPStatus.UNAUTHORIZED
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    # assumes user has modules will fail otherwise 

    print(bearer_token)
    response = client.get("/lessons/b473ce4f-dc92-4236-8f4d-1b6b9e2c1ac6", headers=headers)

    assert response.status_code == HTTPStatus.OK


def test_edit_lesson(client,bearer_token ,random_code):
    
    data = {
            "name": "lesson 3",
            "description": "Test_lesson_edit",


    }
    headers = {
        "Content-Type": "application/json"
    }
    print(bearer_token)
    response_unauth = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data), headers=headers)

    assert response_unauth.status_code == HTTPStatus.UNAUTHORIZED

    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = client.post("/lessons/2b2e2c30-ec2c-44e9-bcde-d2b9fd61150a", data=json.dumps(data),headers=headers)



    with open("powerpoint_test.pptx", "rb") as file1:
        file_contents = file1.read()
        base64_string_file_1 = base64.b64encode(file_contents).decode('utf-8')
    # pdf 
    with open("pdf_test.pdf", "rb") as file2:
        file_contents = file2.read()
        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 
    # image 
    with open("image_test.png", "rb") as file3:
        file_contents = file3.read()
        base64_string_file_3 = base64.b64encode(file_contents).decode('utf-8')
        # this encodes it into a Encode the bytes-like object s using Base64 and return a bytes object.
        # then it is decode into ut-8 string 




        base64_string_file_2 = base64.b64encode(file_contents).decode('utf-8')

    data_with_files = {
            "name": "lesson 1",
            "description": "Test_lesson",
            "files": [
                {   
                    "name": "image_test.png",
                    "base64": base64_string_file_1
                },
                {
                    "name": "pdf_test.pdf",
                    "base64": base64_string_file_2
                },
                {
                    "name": "powerpoint_test.pptx",
                    "base64": base64_string_file_3
                }

                
            ]

    }


    response = client.post(f"/lessons/edit/{response['data']['id']}", data=json.dumps(data_with_files),headers=headers)

    assert response.status_code == HTTPStatus.OK