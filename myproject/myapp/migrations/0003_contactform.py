# Generated by Django 4.1.1 on 2022-09-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_members_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
