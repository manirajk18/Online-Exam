from django.db import models

# Create your models here.
class questionbank(models.Model):
    qno=models.IntegerField(primary_key=True)
    que=models.TextField()
    a=models.TextField()
    b=models.TextField()
    c=models.TextField()
    d=models.TextField()
    mark=models.IntegerField()
    def __str__(self):
        s=str(self.qno)+"  "+self.que+"  "+self.a+"  "+self.b+"  "+self.c+"  "+self.d+"  "+str(self.mark)
        return s

class examiner(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        s=self.username+"  "+self.password
        return s


