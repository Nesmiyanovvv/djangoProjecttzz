from django.test import TestCase, RequestFactory
from myapp.views import memories

class MemoriesViewTestCase(TestCase):
    def setUp(self):
        # Создаем экземпляр RequestFactory для создания запросов
        self.factory = RequestFactory()

    def test_memories_view_get(self):
        # Создаем GET-запрос к memories view
        request = self.factory.get('/memories/')
        response = memories(request)

        # Проверяем, что получили ожидаемый HTTP-ответ
        self.assertEqual(response.status_code, 200)

    def test_memories_view_post(self):
        # Создаем POST-запрос к memories view
        request = self.factory.post('/memories/', {
            'location': 'Test Location',
            'title': 'Test Title',
            'comment': 'Test Comment'
        })
        response = memories(request)

        # Проверяем, что получили ожидаемый HTTP-ответ
        self.assertEqual(response.status_code, 200)