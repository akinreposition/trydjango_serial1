# Generated by Django 3.0.4 on 2020-08-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=120)),
                ('Topic', models.TextField()),
            ],
        ),
    ]
