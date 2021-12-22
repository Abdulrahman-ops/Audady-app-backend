# Generated by Django 3.2.8 on 2021-12-21 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address1',
            new_name='Governorate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='address2',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='company_name',
            new_name='closest_point',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company_website',
        ),
    ]
