# Generated by Django 5.0.7 on 2024-08-02 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_alter_publication_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.category'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='hashtags',
            field=models.ManyToManyField(null=True, related_name='hashtags', to='journal.hashtag'),
        ),
    ]