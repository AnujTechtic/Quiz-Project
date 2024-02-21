from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    date = models.DateField()
    total_marks= models.IntegerField()
    def __str__(self):
        return self.subject

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length = 200)
    option_1 = models.CharField(max_length = 200)
    option_2 = models.CharField(max_length = 200)
    option_3 = models.CharField(max_length = 200)
    option_4 = models.CharField(max_length = 200)
    correct_option = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text
    
class quizCreator(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, null = True, blank = True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200, default='something')
    email = models.EmailField()
    password = models.CharField(max_length=32)
    def __str__(self):
        return str(self.username)

