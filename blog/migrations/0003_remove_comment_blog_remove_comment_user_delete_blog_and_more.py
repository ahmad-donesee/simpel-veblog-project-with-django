# Generated by Django 5.0.2 on 2024-02-10 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
