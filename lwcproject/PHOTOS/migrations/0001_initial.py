# Generated by Django 3.1.6 on 2021-06-17 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=1000)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PHOTOS.category')),
            ],
        ),
    ]
