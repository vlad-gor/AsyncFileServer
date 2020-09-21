import unittest
import requests

class TestStorage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # проверка сервера
    def test_server(self):
        resp = requests.get('http://127.0.0.1:8080/')
        self.assertEqual(resp.status_code,200)

    # загрузка файла
    def test_upload_file(self):
        pass
        # files = {'file': open('README.md', 'rb')}
        # resp = requests.post('http://127.0.0.1:8080/upload_file',files=files)
        # self.assertEqual(resp.status_code,200)

    # выгрузка файла
    def test_download_file(self):
        pass

    # удаление файла
    def test_delete_file(self):
        pass

if __name__ == "__main__":
    unittest.main()