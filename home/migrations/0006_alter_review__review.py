# Generated by Django 4.2.4 on 2023-08-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_review_review__review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='_review',
            field=models.TextField(default='blank review'),
        ),
    ]
