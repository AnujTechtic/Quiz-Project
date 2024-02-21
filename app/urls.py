from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quizCreatorLogin', views.quizCreatorLogin, name='login-page'),
    path('quizCreatorLogout', views.quizCreatorLogout, name='logout-page'),
    path('viewQuiz', views.viewQuiz, name='viewQuiz'),
    path('createQuiz', views.createQuiz, name='createQuiz'),
    path('editQuiz/<int:pk>', views.editQuiz, name='editQuiz'),
    path('deleteQuiz/<int:pk>', views.deleteQuiz, name='deleteQuiz'),
    path('viewQuestion/<int:pk>', views.viewQuestion, name='viewQuestion'),
    path('addQuestion/<int:pk>', views.addQuestion, name='addQuestion'),
    path('editQuestion/<int:pk>', views.editQuestion, name='editQuestion'),
    path('deleteQuestion/<int:pk>', views.deleteQuestion, name='deleteQuestion'),
    path('viewQuizStudent', views.viewQuizStudent, name='viewQuizStudent'),
    
   
]