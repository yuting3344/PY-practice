# Generated by Django 5.0.4 on 2024-04-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nanny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=2)),
                ('path', models.TextField()),
            ],
        ),
    ]
