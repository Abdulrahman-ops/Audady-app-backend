# Generated by Django 3.2.8 on 2021-12-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_alter_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default=str, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
