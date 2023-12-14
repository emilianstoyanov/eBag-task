import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "category_tree_project.settings")
django.setup()

from automatic_recording_db import populate_model_with_data
from category_tree.models import Category

populate_model_with_data(Category, 50)
