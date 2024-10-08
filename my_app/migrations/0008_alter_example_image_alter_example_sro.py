# Generated by Django 5.1.1 on 2024-09-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_example_sro_alter_example_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='example',
            name='sro',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/SRO'),
        ),
    ]
