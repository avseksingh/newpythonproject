# Generated by Django 3.2.13 on 2022-06-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0005_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]