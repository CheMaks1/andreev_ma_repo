import pytest
import requests
from endpoints.create_meme import CreateObject
from endpoints.update_meme import UpdateObject
from endpoints.modify_meme import ModifyObject
from endpoints.delete_meme import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def modify_object_endpoint():
    return ModifyObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_new_object_endpoint(headers=None):
    payload = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
                                                        "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
    response = requests.post(
        url='https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    return response


@pytest.fixture()
def meme_id(auth_token, post_endpoint):
    token, user = auth_token
    body = {
        "text": "some_text",
        "url": "example.com",
        "tags": [
            1,
            2,
            3
        ],
        "info": {
            "one": 1,
            "two": 2
        }
    }
    headers = {'Authorization': f'{token}'}
    response = requests.post('http://167.172.172.115:52355/meme', json=body, headers=headers)
    meme_id_ = response.json()['id']
    yield meme_id_
    print('delete meme')
    requests.delete(f'http://167.172.172.115:52355/{meme_id_}')
