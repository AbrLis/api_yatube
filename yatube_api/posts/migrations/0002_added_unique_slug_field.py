# Generated by Django 2.2.16 on 2022-10-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='group',
            constraint=models.UniqueConstraint(fields=('slug',), name='unique_slug'),
        ),
    ]
