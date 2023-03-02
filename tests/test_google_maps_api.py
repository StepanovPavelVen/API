import json
import allure
from utils.api import Google_maps_api
from utils.checking import Checking

'''Создание изменение и удаление новой локации'''


@allure.epic('Test create place')
class Test_create_place():
    @allure.description('Создание, изменение, удаление локации')
    def test_create_new_place(self):
        print('Метод POST')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(response=result_post, status_code=200)
        Checking.check_json_token(response=result_post,
                                  expected_value=['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(response=result_post, field_name='status', expected_value='OK')

        print('Метод GET POST')
        result_get = Google_maps_api.get_new_place(place_id=place_id)
        Checking.check_status_code(response=result_get, status_code=200)
        Checking.check_json_token(response=result_get,
                                  expected_value=['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                                  'website', 'language'])
        Checking.check_json_value(response=result_get, field_name='address', expected_value='29, side layout, cohen 09')

        print('Метод PUT')
        result_put = Google_maps_api.put_new_place(place_id=place_id)
        Checking.check_status_code(response=result_put, status_code=200)
        Checking.check_json_token(response=result_put, expected_value=['msg'])
        Checking.check_json_value(response=result_put, field_name='msg', expected_value='Address successfully updated')

        print('Метод GET PUT')
        result_get = Google_maps_api.get_new_place(place_id=place_id)
        Checking.check_status_code(response=result_get, status_code=200)
        Checking.check_json_token(response=result_get,
                                  expected_value=['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                                  'website', 'language'])
        Checking.check_json_value(response=result_get, field_name='address', expected_value='100 Lenina street, RU')

        print('Метод DELETE')
        result_delete = Google_maps_api.delete_new_place(place_id=place_id)
        Checking.check_status_code(response=result_delete, status_code=200)
        Checking.check_json_token(response=result_delete, expected_value=['status'])
        Checking.check_json_value(response=result_delete, field_name='status', expected_value='OK')

        print('Метод GET DELETE')
        result_get = Google_maps_api.get_new_place(place_id=place_id)
        Checking.check_status_code(response=result_get, status_code=404)
        Checking.check_json_token(response=result_get, expected_value=['msg'])
        Checking.check_json_value(response=result_get, field_name='msg',
                                  expected_value="Get operation failed, looks like place_id  doesn't exists")

        print('Тестирование создания, изменения и удаления новой локации прошло успешно')
