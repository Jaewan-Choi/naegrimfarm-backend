# Generated by Django 4.0.5 on 2022-07-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='이미지'),
        ),
    ]
