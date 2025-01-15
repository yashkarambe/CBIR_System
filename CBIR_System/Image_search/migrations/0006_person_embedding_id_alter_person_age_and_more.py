# Generated by Django 4.2.17 on 2025-01-15 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image_search', '0005_alter_person_gender_alter_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='embedding_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default='0000'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 1, 15, 9, 7, 40, 876141)),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='zip',
            field=models.PositiveIntegerField(default='0000'),
        ),
    ]
