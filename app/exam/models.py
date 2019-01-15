from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    answer_text = models.TextField()
    answer_value = models.FloatField()

    def __str__(self):
        return f'{self.answer_text} ({self.answer_value})'


class Question(models.Model):
    question_text = models.TextField()
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question_text


class Exam(models.Model):
    questions = models.ManyToManyField(Question)
    title = models.CharField(max_length=255)
    pass_percentage = models.FloatField()

    def __str__(self):
        return self.title


class CompletedExam(models.Model):
    exam = models.ForeignKey(Exam, models.SET_NULL, null=True)
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

    def __str__(self):
        return f'{self.user}: {self.exam} ({self.score:.2f} / {self.exam.pass_percentage})'
