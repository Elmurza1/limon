# Generated by Django 5.0.7 on 2024-07-29 13:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_remove_aboutme_blog_remove_aboutme_i_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
