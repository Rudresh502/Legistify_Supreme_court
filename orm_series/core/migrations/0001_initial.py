# Generated by Django 4.2.4 on 2023-08-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Final_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_hearing', models.DateField()),
                ('description', models.TextField()),
                ('pdf_link', models.TextField()),
            ],
        ),
    ]
