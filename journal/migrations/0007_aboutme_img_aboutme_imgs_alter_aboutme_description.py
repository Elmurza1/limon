# Generated by Django 5.0.7 on 2024-07-31 12:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_aboutme_description_alter_aboutme_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='imgs',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
