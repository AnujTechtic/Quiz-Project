from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import quizCreator

def createquizCreator(sender, instance, created, **kwargs):
    if created:
        user = instance 
        quizCreate = quizCreator.objects.create(
            user = user,
            username = user.username,
            email = user.email, 
            name = user.first_name
            

        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user 
    user.delete()


post_save.connect(createquizCreator, sender=User)
post_delete.connect(deleteUser, sender=quizCreator)