# Generated by Django 3.2 on 2021-04-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_auto_20210427_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image3',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/images/'),
        ),
    ]
