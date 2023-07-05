# Generated by Django 4.0 on 2023-06-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_why_choose_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='clients_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user-images')),
                ('paragraph', models.TextField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
