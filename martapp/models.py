from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    dob=models.DateField(null=True)
    about=models.TextField(max_length=500,null=True)
    profileimage=models.ImageField(default="proerror.png",null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname
class Posts(models.Model):
    CATEGORY=(
        ('Book','Book'),
        ('Electronic','Electronic'),
        ('Vehical','Vehical'),
        ('Furniture','Furniture')
        )
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    cost=models.FloatField(null=True)
    contact=models.CharField(max_length=10,null=True)
    time=models.CharField(max_length=40,null=True)
    category=models.CharField(max_length=20,null=True,choices=CATEGORY)
    detail=models.TextField(max_length=1000,null=True)
    p1=models.ImageField(default="dftimg.png",null=True,blank=True)
    p2=models.ImageField(default="dftimg.png",null=True,blank=True)
    p3=models.ImageField(default="dftimg.png",null=True,blank=True)
    p4=models.ImageField(default="dftimg.png",null=True,blank=True)
    video=models.FileField(upload_to='static/media/%y',null=True,blank=True)
    dop=models.DateTimeField(auto_now_add=True)


