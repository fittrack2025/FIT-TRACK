from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class UserSerializer(ModelSerializer):
    trainer_login_id = serializers.PrimaryKeyRelatedField(source='trainerid.LOGIN.id', queryset=LoginTable.objects.all(), required=False)
    dietition_login_id = serializers.PrimaryKeyRelatedField(source='dietitionid.LOGIN.id', queryset=LoginTable.objects.all(), required=False)

    class Meta:
        model=UserTable
        fields=['id','name','place','age', 'gender','phone','email','height','weight','bmi','calorie','preference','health_issue','dietitionid','trainerid','trainer_login_id','dietition_login_id']



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
    LOGIN = serializers.PrimaryKeyRelatedField(queryset=LoginTable.objects.all())  # This includes only the ID of LoginTable
    class Meta:
        model=TrainerTable
        fields=['id','name','age','phone','certificate','email','LOGIN']


class WorkoutstatusSerializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields=['name','video','description']   


class DietitionSerializer(ModelSerializer):
    LOGIN = serializers.PrimaryKeyRelatedField(queryset=LoginTable.objects.all())  # This includes only the ID of LoginTable
    
    class Meta:
        model=DietitionTable
        fields=['id','name','age','phone','certificate','email','LOGIN']



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
class ChattedUsersSerializer1(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()  # Add a custom field for the name

    class Meta:
        model = LoginTable
        fields = ['id', 'username', 'type', 'name']  # Include the custom name field

    def get_name(self, obj):
        # Fetch the related UserTable instance for the given LoginTable instance
        user = UserTable.objects.filter(LOGINID=obj).first()
        return user.name if user else None 
from rest_framework import serializers
from .models import UserTable

class UserSerializer1(serializers.ModelSerializer):
    user_login_id=serializers.IntegerField(source='LOGINID.id',read_only=True)
    class Meta:
        model = UserTable
        fields = ['id', 'name', 'place', 'age', 'gender', 'phone', 'email', 'height', 'weight', 'bmi', 'calorie', 'preference', 'health_issue','user_login_id']


