# Generated by Django 3.2.9 on 2021-12-02 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0006_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='BlogLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
