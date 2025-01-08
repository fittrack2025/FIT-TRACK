from django.urls import path
from.views import *

urlpatterns = [
    # //////////////////////////////////// ADMIN ////////////////////////////////////
    path('',Login.as_view()),
    path('Feedback/',Feedback.as_view()),
    path('Complaints/',Complaints.as_view()),

    path('Verifyuser/',Verifyuser.as_view()),
    path('Accept_User/<int:u_id>/',Accept_User.as_view(),name="Accept_User"),
    path('Reject_User/<int:u_id>/',Reject_User.as_view(),name="Reject_User"),

    path('Reply/<int:pk>',Reply.as_view(), name='reply'),
    path('Feedbackreply/<int:f_id>',Feedbackreply.as_view()),

    path('Verifydietition/',Verifydietition.as_view()),
    path('Accept_Dietition/<int:d_id>/',Accept_Dietition.as_view(),name="Accept_Dietition"),
    path('Reject_Dietition/<int:d_id>/',Reject_Dietition.as_view(),name="Reject_Dietition"),    

    path('Verifytrainer/',Verifytrainer.as_view()),
    path('Accept_Trainer/<int:t_id>/',Accept_Trainer.as_view(),name="Accept_Trainer"),
    path('Reject_Trainer/<int:t_id>/',Reject_Trainer.as_view(),name="Reject_Trainer"),

    path('Rating/',Rating.as_view()),
    path('Adminhome/',Adminhome.as_view()),
    
    

    # //////////////////////////////////DIETITION /////////////////////////////////////
    
    path('Bookingd/',Bookingd.as_view()),
    path('Dietitionhome/',Dietitionhome.as_view()),
    path('Dietitionuser/<int:i_id>/',Dietitionuser.as_view()),
    path('Logind/',Logind.as_view()),
    path('Users/',Users.as_view()),
    path('Trainers/',Trainers.as_view()),
    path('Dietchat/',DietitionChat.as_view()),
    path('Trainchat/',TrainerChat.as_view()),


    #//////////////////////////////// TRAINER //////////////////////////////////////////

    path('Logint/',Logint.as_view()),
    path('Bookingt/',Bookingt.as_view()),
    path('Trainerhome/',Trainerhome.as_view()),
    path('Traineruser/<int:i_id>/',Traineruser.as_view()),
    path('Managepost/',Managepost.as_view()),
    path('Editpost/<int:pk>/',Editpost.as_view()),
    path('deletep/<int:pk>/',DeletePost.as_view()),
    path('Addpost/',Addpost.as_view()),




    #////////////////////////////////API////////////////


    path('LoginPage',LoginPage.as_view(),name='LoginPage'),
    path('register',Userreg.as_view(),name='register'),
    path('submitfeedback',SubmitFeedback.as_view(),name='submitfeedback'),
    path('submitcomplaint',submitcomplaint.as_view(),name='submitcomplaint'),
    path('ViewTrainerAPI',ViewTrainerAPI.as_view(),name='ViewTrainerAPI'),
    path('ViewDietitionAPI',ViewDietitionAPI.as_view(),name='ViewDietitionAPI'),
    path('ViewPostsAPI', ViewPostsAPI.as_view(), name='ViewPostsAPI'),
    path('ViewProfileAPI/<int:id>',UserProfileView.as_view(),name='ViewProfileAPI'),
    path('EditProfile',EditProfile.as_view(),name='EditProfile'),
    path('ViewPostAPIbytrainerid/<int:id>',ViewPostAPIbytrainerid.as_view(),name='ViewPostAPIbytrainerid'),
    path('ViewPostnamedescriptionAPIbytrainerid/<int:id>',ViewPostnamedescriptionAPIbytrainerid.as_view(),name='ViewPostnamedescriptionAPIbytrainerid'),
    path('ViewPostAPIbytraineridday/<int:id>/<int:day>',ViewPostAPIbytraineridday.as_view(),name='ViewPostAPIbytraineridday'),
    path('chat/<int:sender_id>/<int:receiver_id>', ChatAPIView.as_view(), name='chat-api'),
    path('chatted-users/<int:userid>', ChattedUsersAPIView.as_view(), name='chatted-users'),
    path('api/users/', UserListView.as_view(), name='user-list'),





]
