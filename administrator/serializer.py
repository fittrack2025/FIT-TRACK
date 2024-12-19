from .models import DietitionTable, LoginTable, PostTable, TrainerTable, UserTable
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['LOGINID','name','place','age','phone','email']



class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['username']


class TrainerSerializer(ModelSerializer):
    class Meta:
        model=TrainerTable
        fields=['LOGIN','name','age','phone','certificate','email']


class WorkoutstatusSerializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields=['TRAINER','name','video','description']   


class DietitionSerializer(ModelSerializer):
    class Meta:
        model=DietitionTable
        fields=['LOGIN','name','age','phone','certificate','email']



class Postserializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields=['TRAINER','name','video','description']   


