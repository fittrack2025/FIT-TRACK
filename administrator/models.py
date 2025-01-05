import json
from django.db import models

# Create your models here.



from django.db import models


class LoginTable(models.Model):
    username=models.CharField(max_length=100, blank=True,null=True)
    password=models.CharField(max_length=100, blank=True,null=True)
    type=models.CharField(max_length=100, blank=True,null=True)

    # status=models.CharField(max_length=100, blank=True,null=True)

class TrainerTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE,blank=True,null=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    age= models.CharField(max_length=100, blank=True,null=True)
    phone= models.IntegerField(blank=True,null=True) 
    certificate= models.FileField (upload_to='T_certificate', blank=True,null=True)
    email= models.CharField(max_length=100, blank=True,null=True) 

class DietitionTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE,blank=True,null=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    age= models.CharField(max_length=100, blank=True,null=True)
    phone= models.IntegerField(blank=True,null=True) 
    certificate= models.FileField ( upload_to='D_certificate', blank=True,null=True)
    email= models.CharField(max_length=100, blank=True,null=True) 



class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    place= models.CharField(max_length=100, blank=True,null=True)
    age=models.IntegerField(blank=True, null=True)
    phone= models.BigIntegerField(blank=True, null=True)
    email= models.CharField(max_length=100, blank=True,null=True)
    height= models.CharField(max_length=100, blank=True,null=True)
    weight= models.CharField(max_length=100, blank=True,null=True)
    bmi= models.CharField(max_length=100, blank=True,null=True)
    trainerid=models.ForeignKey(TrainerTable,on_delete=models.CASCADE,blank=True,null=True)
    dietitionid=models.ForeignKey(DietitionTable,on_delete=models.CASCADE,blank=True,null=True)
    calorie= models.CharField(max_length=100, blank=True,null=True) 
    preference= models.CharField(max_length=100, blank=True,null=True)
    health_issue= models.CharField(max_length=100, blank=True,null=True)
    


class FeedbackTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE,blank=True,null=True)
    feedback= models.CharField(max_length=100, blank=True,null=True)
    reply= models.CharField(max_length=100, blank=True,null=True)
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)

    
class ComplaintTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE,blank=True,null=True)
    complaint= models.CharField(max_length=100, blank=True,null=True)
    reply= models.CharField(max_length=100, blank=True,null=True) 
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)




class BookingdTable(models.Model):
    No=models.CharField(max_length=100, blank=True,null=True)
    DIETITION=models.ForeignKey(DietitionTable, on_delete=models.CASCADE,blank=True,null=True)
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE,blank=True,null=True)
    Date = models.CharField(max_length=100, blank=True,null=True)
    time= models.CharField(max_length=100, blank=True,null=True) 
    Status= models.CharField(max_length=100, blank=True,null=True)
    # details = models.CharField(max_length=100,blank=True,null=True) 


class BookingtTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE,blank=True,null=True)
    TRAINER=models.ForeignKey(TrainerTable, on_delete=models.CASCADE,blank=True,null=True)
    name= models.CharField(max_length=100, blank=True,null=True) 
    date= models.CharField(max_length=100, blank=True,null=True)
    time= models.CharField(max_length=100, blank=True,null=True) 
    status= models.CharField(max_length=100, blank=True,null=True)
    # details = models.CharField(max_length=1000, blank=True,null=True)


class RatingTable(models.Model):
    USER=models.ForeignKey(UserTable, on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at=models.DateField(auto_now=True, blank=True,null=True)

    email= models.CharField(max_length=100, blank=True,null=True)
    rating= models.CharField(max_length=100, blank=True,null=True) 


class PostTable(models.Model):
    TRAINER=models.ForeignKey(TrainerTable,on_delete=models.CASCADE,null=True,blank=True)
    type=models.CharField(max_length=100, blank=True,null=True)
    workoutday=models.CharField(max_length=100, blank=True,null=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    videos= models.FileField(upload_to='training_videos/', blank=True,null=True)
    description= models.CharField(max_length=1000, blank=True,null=True) 







    
class FoodTable(models.Model):
    DIETITIAN= models.ForeignKey(DietitionTable, on_delete=models.CASCADE,blank=True,null=True)
    # dietchart=models.CharField(max_length=100, blank=True,null=True)
    foodname= models.CharField(max_length=100, blank=True,null=True)
    receipe= models.CharField(max_length=500, blank=True,null=True)


from django.db import models

class Chat(models.Model):
    sender = models.ForeignKey(
        'LoginTable', 
        related_name='sent_messages', 
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        'LoginTable', 
        related_name='received_messages', 
        on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}"


