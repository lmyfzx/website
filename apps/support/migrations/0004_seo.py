# Generated by Django 2.0.12 on 2019-07-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_qq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
            ],
        ),
    ]
