# Generated by Django 3.2.13 on 2022-06-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
