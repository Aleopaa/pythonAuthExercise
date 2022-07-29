from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)


#WHAT IS HAPPENING IN THIS MODELS.PY FILE?

#THE MODEL COMMUNICATES WITH THE DB 
#IT IS THE SINGLE DIFINITIVE SOURCE OF INFORMATION ABOUT YOUR DATA 
#CONTAINS ESSENTIAL FEATURES OF OUR DATA 
#HERE ABOVE WE HAVE OUR CLASSES OF DATA AND OUR CONSTRAINTS 
#WHEN WE RUN THE MIGRATIONS COMMANDS IT USES THESE CLASSES HERE TO CREATE THEM
