from rest_framework import serializers
from .models import Aluno,Professor,Curso,Modulos,Avaliacao
from django.contrib.auth.models import User


class ProfessorSerializer(serializers.ModelSerializer):
    username=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Professor
        fields=(
            'nome',
            'email',
            'username',
            'password')
        
    def create(self, validated_data):
        username=validated_data.pop('username')
        password=validated_data.pop('password')
        user=User.objects.create_user(
            username=username,
            password=password)
        professor=Professor.objects.create(user=user,**validated_data)
        return professor
    
    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Já existe um usuario com estás credencias!')
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email já esta em uso por um usuario')
        return value
    
class AlunoSerializer(serializers.ModelSerializer):
    username=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Aluno

        fields=(
            'username',
            'password',
            'nome',
            'email',
            'cursos')

    def create(self, validated_data):
        username=validated_data.pop('username')
        password=validated_data.pop('password')
        user=User.objects.create_user(
            username=username,
            password=password)
        aluno=Aluno.objects.create(user=user,**validated_data)
        return aluno
    
    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Já existe um usuario com estás credencias!')
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email já esta em uso por um usuario')
        return value
class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modulos
        fields=[
            'id',
            'modulo',
            'descricao',
            'link',
            'criacao'
        ]
        def create(self, validated_data):
            curso = self.context['cursos']
            return Modulos.objects.create(curso=curso, **validated_data)
        

class CursoSerializer(serializers.ModelSerializer):
    modulos=ModulosSerializer(
        many=True,
        read_only=True
    )
    media_avaliacoes=serializers.FloatField(read_only=True)
    class Meta:
        model=Curso
        fields=[
            'id',
            'titulo',
            'descricao',
            'professor',
            'criacao',
            'modulos',
            'media_avaliacoes',
        ]
        read_only_fields=['professor']



class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avaliacao
        fields=[
            'curso',
            'nota',
            'comentario',
        ]
        read_only_fields=['curso']
class CursoComModulosSerializer(serializers.ModelSerializer):
    modulos=ModulosSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model=Curso
        fields=[
            'titulo',
            'modulos'
        ]
