# Generated by Django 4.1.7 on 2023-05-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0002_alter_author_name_alter_book_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover_photo",
            field=models.ImageField(upload_to="media/"),
        ),
    ]
