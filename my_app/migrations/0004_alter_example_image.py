# Generated by Django 5.1.1 on 2024-09-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_rename_name_example_title_remove_example_example_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
