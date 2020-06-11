# Generated by Django 2.2.12 on 2020-05-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docname', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='userupload/pdf/')),
            ],
        ),
    ]