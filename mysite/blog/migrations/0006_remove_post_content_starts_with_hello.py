# Generated by Django 4.2.10 on 2024-03-11 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_content_starts_with_hello'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='post',
            name='content_starts_with_hello',
        ),
    ]
