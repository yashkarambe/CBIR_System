# Generated by Django 4.2.17 on 2025-01-15 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image_search', '0004_alter_person_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]