# Generated by Django 4.2.11 on 2024-03-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_alter_diary_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
