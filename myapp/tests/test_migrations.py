from django.test import TestCase
from django.db.migrations.executor import MigrationExecutor
from myapp.models import Memory


class MigrationTestCase(TestCase):
    def test_migrations(self):
        # Создаем миграцию и применяем ее
        executor = MigrationExecutor(connection)
        executor.migrate(['myapp'])

        # Проверяем, что модель Memory была создана
        self.assertTrue(Memory.objects.exists())