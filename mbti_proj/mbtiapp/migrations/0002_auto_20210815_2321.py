# Generated by Django 3.2.6 on 2021-08-15 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbtiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbtiapp.major'),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbtiapp.school'),
        ),
    ]