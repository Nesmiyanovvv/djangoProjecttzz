from django.test import TestCase
from myapp.models import Memory

class MemoryModelTestCase(TestCase):
    def test_model_fields(self):
        # Создаем объект модели
        memory = Memory.objects.create(
            location='Test Location',
            title='Test Title',
            comment='Test Comment'
        )

        # Проверяем, что поля модели определены корректно
        self.assertEqual(memory.location, 'Test Location')
        self.assertEqual(memory.title, 'Test Title')
        self.assertEqual(memory.comment, 'Test Comment')

    def test_model_save(self):
        # Проверяем сохранение объекта модели
        count_before = Memory.objects.count()
        memory = Memory.objects.create(
            location='Test Location',
            title='Test Title',
            comment='Test Comment'
        )
        count_after = Memory.objects.count()
        self.assertEqual(count_after, count_before + 1)

    def test_model_delete(self):
        # Проверяем удаление объекта модели
        memory = Memory.objects.create(
            location='Test Location',
            title='Test Title',
            comment='Test Comment'
        )
        count_before = Memory.objects.count()
        memory.delete()
        count_after = Memory.objects.count()
        self.assertEqual(count_after, count_before - 1)