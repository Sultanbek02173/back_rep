from django.test import TestCase, Client
from django.urls import reverse

class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello</h1>"
        expected_header = "Alex"

        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response.status_code, 500) 
        self.assertEqual(response.headers["name"], expected_header)

    def test_get_index(self):
        responce_get = self.client.get(reverse("index-page"))
        responce_post = self.client.post(reverse("index-page"))
        
        expected_get = "Главная страница"
        expected_post = "НЕ тот метод запроса"

        self.assertEqual(responce_get.status_code, 200)
        self.assertEqual(responce_post.status_code, 200)
        self.assertEqual(responce_get.content.decode(), expected_get)
        self.assertEqual(responce_post.content.decode(), expected_post)
        self.assertTrue(responce_get) #Проверка приход на данных