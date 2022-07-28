# Generated by Django 4.0.6 on 2022-07-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=20)),
                ('last_name', models.CharField(default=True, max_length=20)),
                ('date_of_birth', models.DateField(auto_now_add=True, null=True)),
                ('age', models.IntegerField(default=True)),
                ('relationship', models.CharField(max_length=10)),
                ('gender', models.CharField(default=True, max_length=10, null=True)),
            ],
        ),
    ]