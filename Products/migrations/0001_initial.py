# Generated by Django 3.2.6 on 2021-08-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=150)),
                ('season', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='Pictures')),
            ],
        ),
    ]
