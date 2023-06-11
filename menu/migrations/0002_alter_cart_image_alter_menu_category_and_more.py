# Generated by Django 4.2.1 on 2023-06-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('오넛지', '오넛지'), ('카츠', '카츠'), ('더푸리', '더푸리')], max_length=5),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu/'),
        ),
    ]
