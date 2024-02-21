from django.forms import ModelForm, NumberInput
from django import forms
from .models import Quiz, Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

        widgets = {
            'date':forms.DateInput(attrs={'class': 'datepicker'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__( *args, **kwargs)

        self.fields['subject'].widget.attrs.update({'class':'input', 'placeholder':'Name of the Subject', })

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', })