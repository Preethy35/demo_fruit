# Generated by Django 3.2.9 on 2021-11-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
