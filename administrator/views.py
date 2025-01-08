from http.client import HTTPResponse
from urllib import request
from django.shortcuts import redirect, render

# Create your views here.
from django.views import View

from administrator.serializer import *
from .form import Edit_post
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.response import Response


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from .models import LoginTable






class Login(View):
    def get(self,request):
        return render(request,'ADMINISTRATOR/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        Login_obj = LoginTable.objects.get(username=username,password=password)
        request.session['lid']=Login_obj.id
        print(Login_obj)
        if Login_obj.type == "admin":
         return HttpResponse('''<script>alert("Welcome to Admin panel");window.location = "/Adminhome"</script>''')  
        elif Login_obj.type == "Dietition":
         return HttpResponse('''<script>alert("Welcome to Dietition Dashboard");window.location = "/Dietitionhome"</script>''')   
        elif Login_obj.type == "Trainer": 
         return HttpResponse('''<script>alert("Welcome to Trainer Dashboard");window.location = "/Trainerhome/"</script>''')     
        else:
            return HttpResponse('''<script>alert("INVALID");window.location = "/"</script>''')
                                

# /////////////////////////////////////////// ADMINISTRATOR /////////////////////////////////////////////


class Adminhome(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='user').count()
        obj1=DietitionTable.objects.filter(LOGIN__type='Dietition').count()
        print(obj1)
        obj2=TrainerTable.objects.filter(LOGIN__type='Trainer').count()
        
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
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%",obj)
        obj1=DietitionTable.objects.filter(LOGIN__type='Dietition')
        print("########################",obj1)

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
        obj1 = BookingdTable.objects.all().count()
        obj2=TrainerTable.objects.filter(LOGIN__type='Trainer').count()
        obj3=UserTable.objects.filter(LOGINID__type='products').count()
        print(obj,obj1,obj2,obj3)

        
        return render(request,'DIETITION/dietitionhome.html',{'val':obj,'val1':obj1,'val2':obj2, 'val3':obj3})
        


class Users(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='user')
        print(obj)
        return render(request,'DIETITION/users.html',{'val':obj})    
    
class Trainers(View):
    def get(self,request):
        obj=TrainerTable.objects.filter(LOGIN__type='Trainer')
        print(obj)
        return render(request,'DIETITION/trainers.html',{'val':obj})    
       
    
class Dietitionuser(View):
    def get(self,request, i_id):
        obj=BMI.objects.filter(USER_id=i_id)
        return render(request,'DIETITION/dietitionuser.html',{'val':obj})    
    
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
    def get(self,request ):
        obj=BookingtTable.objects.all()
        return render(request,'TRAINER/bookingt.html',{'val':obj})    
    

class Trainerhome(View):
    def get(self,request):
        obj=UserTable.objects.filter(LOGINID__type='user').count()
        obj1 = BookingtTable.objects.all().count()
        obj2=PostTable.objects.all().count()
        obj3=UserTable.objects.filter(LOGINID__type='products').count()
        print(obj,obj1,obj2,obj3)

        
        return render(request,'TRAINER/trainerhome.html',{'val':obj,'val1':obj1,'val2':obj2, 'val3':obj3}) 
        

class Traineruser(View):
    def get(self,request, i_id):
        obj=BMI.objects.filter(USER_id=i_id)

        return render(request,'TRAINER/traineruser.html')   


class Managepost(View):
    def get(self,request):
        obj=PostTable.objects.all()
        return render(request,'TRAINER/managepost.html',{'val':obj})

class Editpost(View):
    def get(self,request,pk):
        obj=PostTable.objects.get(pk=pk) 
        return render(request,'TRAINER/editPost.html',{'val':obj})

    def post(get, request, pk):
        obj=PostTable.objects.get(pk=pk) 
        c = Edit_post(request.POST, request.FILES, instance=obj)
        if c.is_valid():
            c.save()
            return HttpResponse('<script>alert("updated!");window.location="/Managepost/"</script>')
        
class DeletePost(View):
    def get(self, request, pk):
        obj=PostTable.objects.get(pk=pk) 
        obj.delete()
        return HttpResponse('<script>alert("deleted!");window.location="/Managepost/"</script>')



class Addpost(View):
    def get(self, request):
        # Fetch all posts (if needed)
        obj = PostTable.objects.all()
        return render(request, 'TRAINER/addpost.html', {'val': obj})

    def post(self, request):
        # Retrieve the trainer ID from session (assuming it's stored in session as 'lid')
        trainer_id = request.session.get('lid')
        name = request.POST['name']
        type = request.POST['type']
        video = request.FILES['video']
        description = request.POST['description']
        workoutday = request.POST['workoutday']

        # Fetch the corresponding TrainerTable object using the session ID
        try:
            trainer = TrainerTable.objects.get(LOGIN=trainer_id)  # Fetch the TrainerTable object
        except TrainerTable.DoesNotExist:
            return HttpResponse('<script>alert("Trainer not found!");window.location="/Managepost/"</script>')

        # Create a new PostTable object and assign the fields
        obj = PostTable()
        obj.name = name
        obj.type = type
        obj.TRAINER = trainer  # Assign the trainer (TrainerTable object) to the foreign key field
        obj.videos = video
        obj.description = description
        obj.workoutday = workoutday

        # Save the object to the database
        obj.save()

        # Return a success message
        return HttpResponse('<script>alert("Post added!");window.location="/Managepost/"</script>')


 
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


class DietitionChat(View):
    def get(self,request):
        return render(request,'DIETITION/chat.html')
    

class TrainerChat(View):
    def get(self,request):
        return render(request,'TRAINER/chat.html')



# /////////////////////////////////////// USER API //////////////////////////////////////////////////


class ViewTrainerAPI(APIView):
     def get(self,request):
        Response_dict = {}
        trainer=TrainerTable.objects.all()
        trainer_serializer=TrainerSerializer(trainer,many=True)
        Dietition=DietitionTable.objects.all()
        Dietition_serializer=DietitionSerializer(Dietition,many=True)

        Response_dict={
            'trainer':trainer_serializer.data,
            'dietition':Dietition_serializer.data
        }
        return Response(Response_dict)

class SubmitFeedback(APIView):
    def post(self, request):
        # Print the request data (for debugging purposes)
        print("#################", request.data)
        user_id=request.data.get('user_id')
        user_obj = UserTable.objects.get(id=user_id)
        serial = FeedbackSerializer(data=request.data)
        if serial.is_valid():
            serial.save(USER=user_obj)
            return Response(serial.data, status=status.HTTP_201_CREATED)

class submitcomplaint(APIView):
    def post(self, request):
        # Print the request data (for debugging purposes)
        print("#################", request.data)
        user_id=request.data.get('user_id')
        user_obj = UserTable.objects.get(id=user_id)
        serial = ComplaintSerializer(data=request.data)
        if serial.is_valid():
            serial.save(USER=user_obj, repy="pending")
            return Response(serial.data, status=status.HTTP_201_CREATED)

        # If validation failed, return error details
    
    
   

class ViewWorkoutstatusAPI(APIView):
     def get(self,request):
        Workoutstatus=PostTable.objects.all()
        Workoutstatus_serializer=WorkoutstatusSerializer(Workoutstatus,many=True)
        return Response(Workoutstatus_serializer.data)

class ViewDietitionAPI(APIView):
     def get(self,request):
        Dietition=DietitionTable.objects.all()
        Dietition_serializer=DietitionSerializer(Dietition,many=True)
       
        return Response(Dietition_serializer.data)        


class ViewPostsAPI(APIView):
     def get(self,request):
        Posts=PostTable.objects.all()
        Posts_serializer=Postserializer1(Posts,many=True)
        print("$$$$$$$$$$$$$$$$$$$", Posts_serializer)
        return Response(Posts_serializer.data)  
       
class ViewPostAPIbytrainerid(APIView):
    def get(self, request,id, *args, **kwargs):
        # Fetch data from PostTable
        posts = PostTable.objects.filter(TRAINER__id=id).all()
        
        # Serialize the data
        serialized_data = Postserializer2(posts, many=True).data
        
        # Transform the data to desired output format
        grouped_data = {}
        for post in serialized_data:
            workoutday = post['workoutday']
            type_ = post['type']

            if (workoutday, type_) not in grouped_data:
                grouped_data[(workoutday, type_)] = {
                    "workoutday": workoutday,
                    "type": type_,
                    "videos": []
                }

            grouped_data[(workoutday, type_)]["videos"].append({
                "name": post['name'],
                "videos": post['videos'],
                "description": post['description'],
                "workoutday": post['workoutday'],
                "type": post['type'],
                "trainer_id": post['trainer_id']
            })

        # Format the grouped data as a list of dictionaries
        output = list(grouped_data.values())

        return Response(output)
    
class ViewPostAPIbytraineridday(APIView):
    def get(self,request,id,day):
        Posts=PostTable.objects.filter(TRAINER__id=id,workoutday=day).all()
        Posts_serializer=Postserializer1(Posts,many=True)
        print("$$$$$$$$$$$$$$$$$$$", Posts_serializer)
        return Response(Posts_serializer.data)  
class ViewPostnamedescriptionAPIbytrainerid(APIView):
    def get(self,request,id):
        Posts=PostTable.objects.filter(TRAINER__id=id).all()
        Posts_serializer=Postserializer2(Posts,many=True)
        print("$$$$$$$$$$$$$$$$$$$", Posts_serializer)
        return Response(Posts_serializer.data)  
     
         
# class ViewDietchartsAPI(APIView):
#      def get(self,request):
#         Dietcharts=FoodTable.objects.all()
#         Dietcharts_serializer=DietchartsSerializer(Dietcharts,may=True)
#         print("---------------->Dietcharts images"Dietcharts_serializer)
#         return Response(Dietcharts.data)


# class ViewRewardsAPI(APIView):
#      def get(self,request):
#         Rewards=.objects.all()
#         Rewards_serializer=RewardsSerializer(Rewards,may=True)
#         print("---------------->Rewards images"Rewards_serializer)
#         return Response(Rewards.data)       


class Userreg(APIView):
    def post(self, request):
        # Print the request data (for debugging purposes)
        print("#################")
        print("#################", request.data)

        # Initialize serializers with request data
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        # Validate both serializers
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()
        trainer_id= request.data.get('trainerid')
        dietition_id= request.data.get('dietitionid')
        print("^^^^^^^^^^^^^^^^^^^^^", trainer_id)
        print("^^^^^^^^^^^^^^^^^^^^^", dietition_id)
        trainer = TrainerTable.objects.get(id=trainer_id)
        dietition = DietitionTable.objects.get(id=dietition_id)
        # Check if both validations passed
        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&&&")

            # Extract password and save login profile

            login_profile = login_serial.save(type='USER')

            # Save the user with the login profile
            user_serial.save(LOGINID=login_profile, trainerid=trainer, dietitionid=dietition)

            # Return successful response with user data
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        # If validation failed, return error details
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    




class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        print(username)
        password = request.data.get("password")
        print(password)
        
        # Validate input: ensure both username and password are provided
        if not username or not password:
            response_dict["message"] = "Both username and password are required."
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        try:
            t_user = LoginTable.objects.get(username=username,password=password)
        except LoginTable.DoesNotExist:
            response_dict["message"] = "User not found."
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Check password using check_password
        # Uncomment the following line if you want to enable password checking
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "Incorrect password."
        #     return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Build the response dictionary
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id  

        # Return the response
        return Response(response_dict, status=HTTP_200_OK)
    


class UserProfileView(APIView):
    def get(self, request,id):
        try:
            print("###########profileeeeee ##########", id)
            user_profile = UserTable.objects.filter(LOGINID_id=id).first()
            print("sdfg",user_profile)

            if not user_profile:
                return Response(
                    {"message": "Profile not found for the logged-in user."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Serialize the profile data
            serialized_data = UserSerializer(user_profile).data
            print(serialized_data)
            
            # Return the profile data
            return Response(
                serialized_data,
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {"message": "An error occurred while retrieving the profile.", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    # def post(self,request,id):
    #         user_profile = UserTable.objects.filter(LOGINID__id=id).first()
            

class EditProfile(APIView):
    def post(self, request):
        # Print the request data (for debugging purposes)
        print("#################")
        print("#################", request.data)
        user_id = request.data.get('id')
        try:
            # Retrieve the user by ID
            user = UserTable.objects.get(id=user_id)
        except UserTable.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Initialize the serializer with the current user data and the new data from the request
        user_serial = UserSerializer(user, data=request.data, partial=True)  # Use partial=True to allow partial updates

        # Validate the serializer
        if user_serial.is_valid():
            # Save the updated user profile
            user_serial.save()
            # Return successful response with updated user data
            return Response(user_serial.data, status=status.HTTP_200_OK)

        # If validation failed, return error details
        return Response(user_serial.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ChatAPIView(APIView):

    def get(self, request,sender_id,receiver_id):
        user = request.user
        
        if not receiver_id:
            return Response({"error": "receiver_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver = LoginTable.objects.get(id=receiver_id)
        except LoginTable.DoesNotExist:
            return Response({"error": "Receiver does not exist"}, status=status.HTTP_404_NOT_FOUND)

        chats = Chat.objects.filter(
            (models.Q(sender=sender_id) & models.Q(receiver=receiver_id)) |
            (models.Q(sender=receiver_id) & models.Q(receiver=sender_id))
        ).order_by('timestamp')

        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request,sender_id,receiver_id):
        """
        Send a chat message from the logged-in user to a specific receiver.
        """
        user = sender_id
        receiver_id=receiver_id
        data = request.data
        data['sender'] = user 
        data['receiver']= receiver_id# Set the sender to the logged-in user

        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChattedUsersAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request,userid):
        """
        Get a list of users the logged-in user has chatted with.
        """
        user = userid  # Logged-in user
        
        # Fetch all users the logged-in user has sent or received messages with
        sent_chats = Chat.objects.filter(sender=user).values_list('receiver', flat=True)
        received_chats = Chat.objects.filter(receiver=user).values_list('sender', flat=True)
        
        # Combine and get unique user IDs
        chatted_user_ids = set(sent_chats) | set(received_chats)
        
        # Fetch user details for these IDs
        chatted_users = LoginTable.objects.filter(id__in=chatted_user_ids)
        
        # Serialize the user details
        serializer = ChattedUsersSerializer(chatted_users, many=True)
        
        return Response(serializer.data)


class UserListView(APIView):
    def get(self, request):
        users = UserTable.objects.all()  # Get all users
        serializer = UserSerializer1(users, many=True)
        return Response(serializer.data)