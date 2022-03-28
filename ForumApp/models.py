from django.db import models

# Create your models here.



class Questions(models.Model):
    QuestionId = models.AutoField(primary_key=True)
    description=models.CharField(max_length=500)

class CommentQuestions(models.Model):
    CommentQuestionId= models.AutoField(primary_key=True)
    description=models.CharField(max_length=500)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

class Answers(models.Model):
    AnswerId = models.AutoField(primary_key=True)
    question = models.OneToOneField(Questions, on_delete=models.CASCADE)
    description=models.CharField(max_length=500)

class CommentAnswers(models.Model):
    CommentAnswerId= models.AutoField(primary_key=True)
    description=models.CharField(max_length=500)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)


class Tags(models.Model):
    TagId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
