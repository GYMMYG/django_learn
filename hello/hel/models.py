from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''
    class:book model
    '''
    #charfield:string max_length:the largest length
    btitle = models.CharField(max_length=20)
    #datefield:date
    bpub_data = models.DateField()
    def __str__(self):
        #return btitle
        return self.btitle
    #python manage.py makemigrations   : Generate the migration file

    #python manage.py migrate   :    excute the migrate

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    #Defining relationship attributes in multiple classes :use foreignkey
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname
