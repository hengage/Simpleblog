# Generated by Django 3.2.4 on 2021-06-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Simple Blog', max_length=255),
        ),
    ]
