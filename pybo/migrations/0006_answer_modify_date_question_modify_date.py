# Generated by Django 4.2 on 2023-06-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0005_answer_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
