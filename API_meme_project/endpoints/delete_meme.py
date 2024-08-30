import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Request to delete created object')
    def delete_object(self, post_id):
        self.response = requests.delete(
            f'{self.url}/{post_id}'
        )
        return self.response
