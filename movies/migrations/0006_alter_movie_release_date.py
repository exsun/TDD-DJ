# Generated by Django 4.0.5 on 2022-06-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
