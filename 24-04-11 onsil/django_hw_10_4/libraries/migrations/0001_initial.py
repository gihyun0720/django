# Generated by Django 4.2.8 on 2024-04-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField(max_length=10)),
                ('author', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]
