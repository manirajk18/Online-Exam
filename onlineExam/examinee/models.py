from django.db import models

# Create your models here.
class examinee(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20,default='')
    rollno=models.CharField(max_length=20,default='')
    email=models.CharField(max_length=20,default='')
    marks=models.IntegerField()

    def __str__(self):
        s=self.name+"  "+self.rollno+"  "+self.email+"  "+str(self.marks)+"  "+self.username+"  "+self.password
        return s
    