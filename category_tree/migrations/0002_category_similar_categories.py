# Generated by Django 4.2.7 on 2023-12-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_tree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='similar_categories',
            field=models.ManyToManyField(blank=True, to='category_tree.category'),
        ),
    ]
