# Generated by Django 3.2.6 on 2021-08-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_cartitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=150)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('adress', models.CharField(max_length=500)),
                ('iban', models.CharField(max_length=150)),
                ('bank', models.CharField(max_length=150)),
                ('registrationnumber', models.CharField(max_length=150)),
                ('delivery', models.CharField(max_length=150)),
                ('payment', models.CharField(max_length=150)),
                ('comments', models.CharField(max_length=150)),
                ('totalamount', models.FloatField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
