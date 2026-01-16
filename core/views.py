from rest_framework.views import APIView
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,ModulosSerializer,CursoComModulosSerializer,AvaliacaoSerializer
from .models import Curso,models,Professor,Aluno,Avaliacao,Inscricoes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsProfessor,IsAluno
from django.db.models import Avg
from django.shortcuts import get_object_or_404

#Autoriza apenas os professores a criarem os cursos
class CursoAPIView(APIView):
    permission_classes=[IsAuthenticated,IsProfessor]
    def post(self,request):
        serializer=CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(professor=request.user.professor)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class ModuloAPIView(APIView):
    permission_classes=[IsAuthenticated,IsProfessor]
    def post(self,request,curso_id):
        cursos=get_object_or_404(Curso,id=curso_id)
        serializer=ModulosSerializer(data=request.data,context={'cursos':cursos})
        serializer.is_valid(raise_exception=True)
        serializer.save(cursos=cursos)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class VerModuloAPIView(APIView):
    permission_classes=[IsAuthenticated,IsAluno]
    def get(self,request,modulo_id):
        curso=get_object_or_404(Curso,id=modulo_id)
        modulos=curso.modulos.all()
        serializer=ModulosSerializer(modulos,many=True)
        return Response(serializer.data)


#Criar modulo avaliação e criar o metodo post e get da avaliçao

class AvaliacaoAPIView(APIView):
    permission_classes=[IsAuthenticated,IsAluno]
    def post(self,request,curso_id):
        try:
            aluno=request.user.aluno
            curso=get_object_or_404(Curso,id=curso_id)
        except:
            if Aluno.DoesNotExist:
                return Response(
                    {'Apenas alunos podem avaliar cursos'},
                    status=status.HTTP_403_FORBIDDEN
                )
            if Curso.DoesNotExist:
                return Response(
                    {'Este curso não existe'},status=status.HTTP_400_BAD_REQUEST
                )
        serializer=AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(aluno=aluno,curso=curso)#aqui ele preenche o campo aluno automaticamente
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AvaliacoesAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        avaliacao=Avaliacao.objects.all()
        serializer=AvaliacaoSerializer(avaliacao,many=True)
        return Response(serializer.data)

class CursosAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        cursos=Curso.objects.annotate(media_avalicoes=Avg('avaliacoes__nota'))
        serializer=CursoSerializer(cursos,many=True)
        return Response(serializer.data)

class CursosDosAlunosAPIView(APIView):
    permission_classes=[IsAuthenticated,IsAluno]
    def get(self,request):
        aluno=request.user.aluno
        cursos=aluno.cursos.all()
        serializer=CursoComModulosSerializer(cursos,many=True)
        return Response(serializer.data)

class AlunosDoMeuCursoAPIView(APIView):
    permission_classes=[IsAuthenticated,IsProfessor]
    def get(self,request,curso_id):
        curso=Curso.objects.get(
            id=curso_id,
            professor=request.user.professor
        )
        incricoes=curso.inscricoes.select_related('aluno').all()

        dados=[]

        for inscrito in incricoes:
            dados.append({
                'aluno':inscrito.aluno.nome,
                'email':inscrito.aluno.email,
                'data_inscricao':inscrito.data_inscricao
            })
        return Response(dados)

class InscreverNoCursoAPI(APIView):
    permission_classes=[IsAuthenticated,IsAluno]
    def post(self,request,curso_id):
        aluno=request.user.aluno
        curso=get_object_or_404(Curso,id=curso_id)
        Inscricoes.objects.get_or_create(
            aluno=aluno,
            curso=curso
        )
        return Response({"msg":"Inscrição realizada com sucesso"},status=status.HTTP_201_CREATED)
        

#criar api para criação de professor e aluno

class CriarProfessorAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=ProfessorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class CriarAlunoAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=AlunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#usuario logado

class PerfilAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request,user

        if hasattr(user,'aluno'):
            aluno=user.aluno
            serializer=AlunoSerializer(aluno)
            return Response(serializer.data)
        
        if hasattr(user,'professor'):
            professor=user.professor
            serializer=ProfessorSerializer(professor)
            return Response(serializer.data)