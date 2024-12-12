from django.urls import path,include
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
    path('Dietitionuser/',Dietitionuser.as_view()),
    path('Logind/',Logind.as_view()),


    #//////////////////////////////// TRAINER //////////////////////////////////////////

    path('Logint/',Logint.as_view()),
    path('Bookingt/',Bookingt.as_view()),
    path('Trainerhome/',Trainerhome.as_view()),
    path('Traineruser/',Traineruser.as_view()),
    path('Managepost/',Managepost.as_view())



]
