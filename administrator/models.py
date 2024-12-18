import json
from django.db import models

# Create your models here.



from django.db import models


class LoginTable(models.Model):
    username=models.CharField(max_length=30, blank=True,null=True)
    password=models.CharField(max_length=30, blank=True,null=True)
    type=models.CharField(max_length=30, blank=True,null=True)

    # status=models.CharField(max_length=30, blank=True,null=True)
    
class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE)
    name= models.CharField(max_length=30, blank=True,null=True)
    place= models.CharField(max_length=30, blank=True,null=True)
    age=models.IntegerField(blank=True, null=True)
    phone= models.BigIntegerField(blank=True, null=True)
    email= models.CharField(max_length=30, blank=True,null=True)    
    

class FeedbackTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    feedback= models.CharField(max_length=30, blank=True,null=True)
    reply= models.CharField(max_length=30, blank=True,null=True)
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)

    
class ComplaintTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    complaint= models.CharField(max_length=30, blank=True,null=True)
    reply= models.CharField(max_length=30, blank=True,null=True) 
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)


class TrainerTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=30, blank=True,null=True)
    age= models.CharField(max_length=30, blank=True,null=True)
    phone= models.IntegerField(blank=True,null=True) 
    certificate= models.FileField (upload_to='T_certificate', blank=True,null=True)
    email= models.CharField(max_length=30, blank=True,null=True) 

class DietitionTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=30, blank=True,null=True)
    age= models.CharField(max_length=30, blank=True,null=True)
    phone= models.IntegerField(blank=True,null=True) 
    certificate= models.FileField ( upload_to='D_certificate', blank=True,null=True)
    email= models.CharField(max_length=30, blank=True,null=True) 


class BookingdTable(models.Model):
    No=models.CharField(max_length=30, blank=True,null=True)
    DIETITION=models.ForeignKey(DietitionTable, on_delete=models.CASCADE)
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Date = models.CharField(max_length=30, blank=True,null=True)
    time= models.CharField(max_length=30, blank=True,null=True) 
    Status= models.CharField(max_length=30, blank=True,null=True)
    # details = models.CharField(max_length=30,blank=True,null=True) 


class BookingtTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    TRAINER=models.ForeignKey(TrainerTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=30, blank=True,null=True) 
    date= models.CharField(max_length=30, blank=True,null=True)
    time= models.CharField(max_length=30, blank=True,null=True) 
    status= models.CharField(max_length=30, blank=True,null=True)
    # details = models.CharField(max_length=300, blank=True,null=True)


class RatingTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)

    email= models.CharField(max_length=30, blank=True,null=True)
    rating= models.CharField(max_length=30, blank=True,null=True) 





class PostTable(models.Model):
    TRAINER=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=30, blank=True,null=True)
    video= models.FileField(upload_to='training_videos/', blank=True,null=True)
    description= models.CharField(max_length=300, blank=True,null=True) 





class BMI(models.Model):
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE)
    height= models.CharField(max_length=30, blank=True,null=True) 
    weight= models.CharField(max_length=30, blank=True,null=True)
    calorie= models.CharField(max_length=30, blank=True,null=True) 
    preference= models.CharField(max_length=30, blank=True,null=True)
    health_issue= models.CharField(max_length=30, blank=True,null=True)

    
class FoodTable(models.Model):
    DIETITIAN= models.ForeignKey(DietitionTable, on_delete=models.CASCADE)
    foodname= models.CharField(max_length=30, blank=True,null=True)
    receipe= models.CharField(max_length=500, blank=True,null=True)


class ChatTable(models.Model):
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)
    sender= models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="sender")
    receiver= models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="receiver") 
    message= models.CharField(max_length=30, blank=True,null=True)


