# Generated by Django 4.2.10 on 2024-03-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_author'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='post',
            constraint=models.CheckConstraint(check=models.Q(('content__startswith', 'Hello')), name='content_starts_with_hello'),
        ),
    ]
