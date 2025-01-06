from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['id','name','place','age', 'gender','phone','email','height','weight','bmi','calorie','preference','health_issue']



class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['username','password']

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model=FeedbackTable
        fields=['feedback']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['complaint']


class TrainerSerializer(ModelSerializer):
    class Meta:
        model=TrainerTable
        fields=['id','name','age','phone','certificate','email']


class WorkoutstatusSerializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields=['name','video','description']   


class DietitionSerializer(ModelSerializer):
    class Meta:
        model=DietitionTable
        fields=['id','name','age','phone','certificate','email']



class Postserializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields=['name','videos','description','workoutday', 'type']   

class Postserializer1(ModelSerializer):
    trainer_id=serializers.IntegerField(source='TRAINER.id',read_only=True)
    class Meta:
        model=PostTable
        fields=['name','videos','description','workoutday', 'type', 'trainer_id']   

class Postserializer2(ModelSerializer):
    trainer_id=serializers.IntegerField(source='TRAINER.id',read_only=True)
    class Meta:
        model=PostTable
        fields=['name','videos','description','workoutday', 'type', 'trainer_id']   


class ChatSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp', 'sender_username', 'receiver_username']
class ChattedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['id', 'username', 'type']

