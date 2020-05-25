# Generated by Django 3.0.5 on 2020-05-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('pic', models.FileField(upload_to='images/')),
                ('postedby', models.CharField(max_length=50)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField()),
            ],
        ),
    ]
