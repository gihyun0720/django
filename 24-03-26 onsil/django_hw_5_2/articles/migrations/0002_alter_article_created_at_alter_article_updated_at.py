# Generated by Django 4.2.11 on 2024-03-26 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]