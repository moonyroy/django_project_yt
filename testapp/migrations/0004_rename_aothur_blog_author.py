# Generated by Django 3.2.9 on 2021-12-01 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_blog_aothur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='aothur',
            new_name='author',
        ),
    ]