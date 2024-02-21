from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .forms import QuestionForm, QuizForm
from .models import Quiz, Question, quizCreator

# Create your views here.
def home(request):
    return render(request, 'app/Home.html')

def quizCreatorLogin(request):
    if request.user.is_authenticated:
      return redirect('viewQuiz')
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      try:
         user = User.objects.get(username = username)
      except:
        messages.error(request, "Username does not exist")
        
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user )
         return redirect('home')
      else:
         messages.error(request, "Username or Password is Incorrect")
    return render(request, 'app/login-register.html')


def quizCreatorLogout(request):
    logout(request)
    messages.info(request, "User was Logged Out")
    return redirect('login-page')

def createQuiz(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewQuiz')
    context = {'form':form }
    return render(request, 'app/createQuiz.html',context)

def viewQuiz(request):
    quiz = Quiz.objects.all()
    context = {'quizs':quiz}
    return render(request, 'app/viewQuiz.html', context)

def editQuiz(request, pk):
    id = Quiz.objects.get(id=pk)
    form = QuizForm(instance=id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('viewQuiz')
    context = {'form':form }
    return render(request, 'app/createQuiz.html',context)

def deleteQuiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    context = {'object':quiz}
    if request.method == 'POST':
        quiz.delete()
        return redirect('viewQuiz')
    return render(request, 'app/deleteConfirm.html',context)

def addQuestion(request, pk):
    quiz = Quiz.objects.filter(id=pk)
    id = Quiz.objects.get(id=pk)
    form = QuestionForm()
    print(id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewQuiz')
    context = {'form':form, 'quiz':quiz, 'id':id}
    return render(request, 'app/addQuestion.html', context)

def viewQuestion(request, pk):
    question = Question.objects.filter(quiz=pk)
    quiz = Quiz.objects.filter(id=pk)
    quiz_id = Quiz.objects.get(id=pk)
    context = {'quizs':question, 'ids': quiz_id, 'ques':quiz}
    return render(request, 'app/viewQuestion.html',context)

def editQuestion(request, pk):
    quiz = Quiz.objects.filter(id=pk)
    quizi = Question.objects.get(id=pk)
    id = Question.objects.get(id=pk)
    form = QuestionForm(instance=quizi)
    print(id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=quizi)
        if form.is_valid():
            form.save()
            return redirect('viewQuiz')
    context = {'form':form, 'quiz':quiz, 'id':id}
    return render(request, 'app/addQuestion.html', context)

def deleteQuestion(request, pk):
    question = Question.objects.get(id=pk)
    context = {'object':question}
    if request.method == 'POST':
        question.delete()
        return redirect('viewQuiz')
    return render(request, 'app/deleteConfirm.html',context)

def viewQuizStudent(request):
    quiz = Quiz.objects.all()
    context = {'quizs':quiz}
    return render(request, 'app/viewQuizStudent.html', context)
