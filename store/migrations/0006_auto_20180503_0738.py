# Generated by Django 2.0.4 on 2018-05-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]
