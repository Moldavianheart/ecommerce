# Generated by Django 2.0.4 on 2018-05-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180502_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imgage_id',
            new_name='image_id',
        ),
    ]
