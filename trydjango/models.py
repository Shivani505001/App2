from django.db import models

# Create your models here.
#step 1: makemigrations 
#step 2 : python manage.py migrate
class article(models.Model): #all django models inherit from models.Model onli 
    title=models.TextField()
    content=models.TextField()