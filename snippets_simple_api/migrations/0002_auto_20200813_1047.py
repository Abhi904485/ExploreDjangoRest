# Generated by Django 3.1 on 2020-08-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets_simple_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
