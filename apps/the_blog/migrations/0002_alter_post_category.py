# Generated by Django 3.2.4 on 2021-11-09 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='django', on_delete=django.db.models.deletion.PROTECT, related_name='category', to='the_blog.postcategory'),
        ),
    ]
