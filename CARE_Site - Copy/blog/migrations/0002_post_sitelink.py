# Generated by Django 4.2.2 on 2023-07-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sitelink',
            field=models.URLField(blank=True, null=True),
        ),
    ]