# Generated by Django 5.0.7 on 2024-07-29 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_category_hashtag_publication_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='i',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='img',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='imgs',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='project',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='skills',
        ),
    ]
