from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    description = models.TextField()
    learningInfo = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    materials = models.TextField(blank=True, null=True)
    discussion = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Faq(models.Model):
    title = models.CharField(max_length=50)


class FaqData(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField()
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE)


class Quiz(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    headline = models.TextField(blank=True, null=True)


class QuizData(models.Model):
    question = models.CharField(blank=True, null=True, max_length=100)
    first_answer = models.CharField(blank=True, null=True, max_length=100)
    second_answer = models.CharField(blank=True, null=True, max_length=100)
    third_answer = models.CharField(blank=True, null=True, max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)

