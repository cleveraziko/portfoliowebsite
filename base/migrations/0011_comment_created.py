# Generated by Django 3.2.8 on 2021-11-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
