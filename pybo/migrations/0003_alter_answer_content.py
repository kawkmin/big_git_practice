# Generated by Django 4.2 on 2023-05-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0002_alter_question_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="content",
            field=models.TextField(null=True),
        ),
    ]