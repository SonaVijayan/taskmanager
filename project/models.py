from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    language=models.CharField(max_length=100)
    image=models.ImageField(upload_to='project_images')
    
    

    
