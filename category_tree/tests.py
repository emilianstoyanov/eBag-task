import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "category_tree_project.settings")
django.setup()

from django.test import TestCase
from .models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            description='Test description',
            image='test_image.jpg',
            parent=None
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'Test description')
        self.assertEqual(self.category.image, 'test_image.jpg')
        self.assertIsNone(self.category.parent)

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), 'Test Category')
