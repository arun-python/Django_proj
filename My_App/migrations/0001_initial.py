# Generated by Django 4.1.4 on 2023-01-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default='')),
                ('address', models.CharField(default='', max_length=20)),
                ('contact', models.IntegerField(default='')),
                ('email', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
