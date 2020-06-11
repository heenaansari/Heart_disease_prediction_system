# Generated by Django 2.2.12 on 2020-05-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0004_auto_20200506_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('vemail', models.EmailField(max_length=254)),
                ('vdob', models.CharField(max_length=10)),
                ('vpassword', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]