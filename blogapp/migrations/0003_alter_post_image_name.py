# Generated by Django 4.1 on 2022-08-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_author_first_name_alter_author_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(upload_to='blogapp'),
        ),
    ]
