# Generated by Django 2.0.4 on 2019-03-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_review_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='bala', max_length=200),
        ),
    ]
