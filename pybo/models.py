from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField(null=True)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    create_date = models.DateTimeField()