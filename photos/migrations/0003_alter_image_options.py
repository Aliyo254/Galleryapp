# Generated by Django 4.0.4 on 2022-06-02 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
    ]
