# Generated by Django 3.2.6 on 2021-08-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbtiapp', '0003_auto_20210815_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]