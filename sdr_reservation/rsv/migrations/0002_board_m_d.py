# Generated by Django 3.0.8 on 2020-08-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='m_d',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
