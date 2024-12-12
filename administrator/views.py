from http.client import HTTPResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.views import View
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse






class Login(View):
    def get(self,request):
        return render(request,'ADMINISTRATOR/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        Login_obj = LoginTable.objects.get(username=username,password=password)
        print(Login_obj)
        if Login_obj.type == "admin":
         return HttpResponse('''<script>alert("Welcome to Admin");window.location = "/Adminhome"</script>''')  
        elif Login_obj.type == "Dietition":
         return HttpResponse('''<script>alert("Welcome to dietition");window.location = "/Dietitionhome"</script>''')    
        else:
            return HttpResponse('''<script>alert("INVALID");window.location = "/"</script>''')
                                

# /////////////////////////////////////////// ADMINISTRATOR /////////////////////////////////////////////


class Adminhome(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='user').count()
        obj1=UserTable.objects.filter(LOGINID__type='dietition').count()
        obj2=UserTable.objects.filter(LOGINID__type='trainer').count()
        
        return render(request,'ADMINISTRATOR/adminhome.html',{'val':obj,'val1':obj1,'val2':obj2})
        
    

    
class Verifyuser(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='pending')
        print(obj)
        obj1=UserTable.objects.filter(LOGINID__type='user')


        return render(request,'ADMINISTRATOR/verifyuser.html',{'val':obj,'val1':obj1})
    

class Accept_User(View):
    def get(self, request, u_id):
        try:
            user = UserTable.objects.get(id=u_id)
            print(user)  # Fetch the instance
            user.LOGINID.type = 'user'  # Update the status
            user.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verifyuser/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("User not found", status=404)
        
class Reject_User(View):
    def get(self, request, u_id):
        try:
            user = UserTable.objects.get(id=u_id)  # Fetch the instance
            user.LOGINID.type = 'Rejected'  # Update the status
            user.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/Verifyuser/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("user not found", status=404)


class Feedback(View):
    def get(self,request):
        obj=FeedbackTable.objects.all()
        return render(request,'ADMINISTRATOR/feedback.html',{'val':obj})
    
class Feedbackreply(View):
    def get(self,request,f_id):
        obj=FeedbackTable.objects.get(id=f_id)
        return render(request,'ADMINISTRATOR/feedbackreply.html',{'val':obj} ) 
    def post(self,request,f_id):
        obj=FeedbackTable.objects.get(id=f_id)
        reply=request.POST['reply']
        obj.reply=reply
        obj.save()
        return HttpResponse('''<script>alert("successfully replied");window.location="/Feedback/"</script>''')  


    


class Reply(View):
    def get(self,request): 
        return render(request,'ADMINISTRATOR/reply.html')
    



class Verifydietition(View):
    def get(self,request):
        obj=DietitionTable.objects.filter(LOGIN__type='pending')
        print(obj)
        obj1=DietitionTable.objects.filter(LOGIN__type='Dietition')
        print(obj1)

        return render(request,'ADMINISTRATOR/verifydietiton.html',{'val':obj,'val1':obj1})
    
class Accept_Dietition(View):
    def get(self,request, d_id):
        try:
            dietition = DietitionTable.objects.get(id=d_id)
            print(dietition)  # Fetch the instance
            dietition.LOGIN.type = 'Dietition'  # Update the status
            dietition.LOGIN.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verifydietition/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Dietition found", status=404)
        
class Reject_Dietition(View):
    def get(self, request, d_id):
        try:
            dietition = DietitionTable.objects.get(id=d_id)  # Fetch the instance
            dietition.LOGIN.type = 'Rejected'  # Update the status
            dietition.LOGIN.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/Verifydietition/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Dietition not found", status=404)    
    


class Verifytrainer(View):
    def get(self,request):
        obj=TrainerTable.objects.filter(LOGIN__type='pending')
        print(obj)
        obj1=TrainerTable.objects.filter(LOGIN__type='Trainer')
        print(obj1)


        return render(request,'ADMINISTRATOR/verifytrainer.html',{'val':obj, 'val1':obj1})
    
    
class Accept_Trainer(View):
    def get(self, request, t_id):
        try:
            trainer = TrainerTable.objects.get(id=t_id)
            print(trainer)  # Fetch the instance
            trainer.LOGIN.type = 'Trainer'  # Update the status
            trainer.LOGIN.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verifytrainer/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Trainer found", status=404)
        
class Reject_Trainer(View):
    def get(self, request, t_id):
        try:
            trainer = TrainerTable.objects.get(id=t_id)  # Fetch the instance
            trainer.LOGIN.type = 'Rejected'  # Update the status
            trainer.LOGIN.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/Verifytrainer/"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Trainer not found", status=404)    
    

class Rating(View):
    def get(self,request):
        obj=RatingTable.objects.all()
        return render(request,'ADMINISTRATOR/rating.html',{'val':obj})    
    
  



# /////////////////////////////////////////////// DIETITION ////////////////////////////////////////
 
class Bookingd(View):
    def get(self,request):
        obj=BookingdTable.objects.all()
        return render(request,'DIETITION/bookingd.html',{'val':obj})
    
    
class Dietitionhome(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='user').count()
        obj1=UserTable.objects.filter(LOGINID__type='bookedusers').count()
        obj2=UserTable.objects.filter(LOGINID__type='trainer').count()
        obj3=UserTable.objects.filter(LOGINID__type='products').count()

        
        return render(request,'DIETITION/dietitionhome.html',{'val':obj,'val1':obj1,'val2':obj2, 'val3':obj3})
        

    
class Dietitionuser(View):
    def get(self,request):
        obj=UserTable.objects.all()
        return render(request,'DIETITION\dietitionuser.html')    
    
class Logind(View):
    def get(self,request):
        return render(request,'DIETITION/logind.html') 
    def post(self,request):
            name = request.POST['name']
            age = request.POST['age']
            phone = request.POST['phone']
            certificate = request.POST['certificate']
            email = request.POST['email']
            password = request.POST['password']
            login_obj = LoginTable()
            login_obj.username = name
            login_obj.password = password
            login_obj.type = 'pending'
            login_obj.save()
            obj = DietitionTable()
            obj.name=name
            obj.age=age
            obj.phone=phone
            obj.certificate=certificate
            obj.email=email
            obj.LOGIN=login_obj
            obj.save()
            return HttpResponse('''<script>alert("successfully registered");window.location="/"</script>''')  

    




    #/////////////////////////  TRAINER  //////////////////////////////


class Logint(View):
    def get(self,request):
        return render(request,'TRAINER/logint.html')   
    def post(self,request):
            name = request.POST['name']
            age = request.POST['age']
            phone = request.POST['phone']
            certificate = request.POST['certificate']
            email = request.POST['email']
            password = request.POST['password']
            login_obj = LoginTable()
            login_obj.username = name
            login_obj.password = password
            login_obj.type = 'pending'
            login_obj.save()
            obj = TrainerTable()
            obj.name=name
            obj.age=age
            obj.phone=phone
            obj.certificate=certificate
            obj.email=email
            obj.LOGIN=login_obj
            obj.save()
            return HttpResponse('''<script>alert("successfully registered");window.location="/"</script>''')  

    

class Bookingt(View):
    def get(self,request):
        obj=BookingtTable.objects.all()
        return render(request,'TRAINER/bookingt.html',{'val':obj})    
    

class Trainerhome(View):
    def get(self,request):
        return render(request,'TRAINER/trainerhome.html')   
        

class Traineruser(View):
    def get(self,request):
        return render(request,'TRAINER/traineruser.html')   


class Managepost(View):
    def get(self,request):
        obj=PostTable.objects.all()
        return render(request,'TRAINER/managepost.html',{'val':obj})    
 
class Complaints(View):
    def get(self,request):
        obj=ComplaintTable.objects.all()
        return render(request,'ADMINISTRATOR/complaints.html',{'val':obj})
  

class Reply(View):
    def get(self,request,pk):
        obj=ComplaintTable.objects.get(pk=pk)
        return render(request,'ADMINISTRATOR/reply.html',{'val':obj} ) 
    def post(self,request,pk):
        obj=ComplaintTable.objects.get(pk=pk)
        reply=request.POST['reply']
        obj.reply=reply
        obj.save()
        return HttpResponse('''<script>alert("noted");window.location="/Complaints/"</script>''')  

