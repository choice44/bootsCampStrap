# Generated by Django 4.2 on 2023-04-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='이름')),
                ('password', models.CharField(max_length=32, verbose_name='이름')),
                ('bio', models.CharField(max_length=32, verbose_name='이름')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
