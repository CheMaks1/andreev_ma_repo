import pytest

TEST_DATA = [
    {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
                                              "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook Pro 19", "data": {"year": 2021, "price": 1849.99,
                                              "CPU model": "M1", "Hard disk size": "2 TB"}}
]

NEGATIVE_DATA = [
    {"name": ["Apple MacBook Pro 16"], "data": {"year": 2019, "price": 1849.99,
                                                "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": {"Apple MacBook Pro 19": ''}, "data": {"year": 2021, "price": 1849.99,
                                                    "CPU model": "M1", "Hard disk size": "2 TB"}}
]

PATCH_DATA = [
    {"name": "Apple MacBook Pro 11", "data": {"price": 2000.99, "CPU model": "Intel Core i9"}}
]

UPDATE_DATA = [
    {"name": "Apple MacBook Pro 24", "data": {"year": 2012, "price": 184.99,
                                              "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_new_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_response_status_code_is_200()
    create_object_endpoint.check_response_name_for_object(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_object_with_array_in_title(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_bad_request()


@pytest.mark.parametrize('data', UPDATE_DATA)
def test_put_a_object(update_object_endpoint, create_new_object_endpoint, data):
    update_object_endpoint.make_changes_in_object(create_new_object_endpoint.json()['id'], data)
    update_object_endpoint.check_response_status_code_is_200()
    update_object_endpoint.check_response_name_for_object(data['name'])


@pytest.mark.parametrize('data', PATCH_DATA)
def test_patch_a_object(modify_object_endpoint, create_new_object_endpoint, data):
    modify_object_endpoint.partial_update_in_object(create_new_object_endpoint.json()['id'], data)
    modify_object_endpoint.check_response_name_for_object(data['name'])


@pytest.mark.parametrize('body', UPDATE_DATA)
def test_update_meme(put_endpoint, body, meme_id, auth_token):
    token, user = auth_token
    body["id"] = int(meme_id)
    put_endpoint.update_meme(meme_id=meme_id, body=body, headers={'Authorization': f'{token}'})
    put_endpoint.check_response_code()
    put_endpoint.check_response_id(put_endpoint.response.json()['id'])


def test_delete_a_object(delete_object_endpoint, create_new_object_endpoint):
    delete_object_endpoint.delete_object(create_new_object_endpoint.json()['id'])
    delete_object_endpoint.check_response_status_code_is_200()
