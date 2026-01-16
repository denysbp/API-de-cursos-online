from django.db import models
from django.contrib.auth.models import User
NUMEROS_CHOICES = [(i, str(i)) for i in range(11)]
class Professor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nome=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.nome
class Curso(models.Model):
    
    titulo=models.CharField(max_length=250)
    descricao=models.TextField(max_length=300)
    criacao=models.DateTimeField(auto_now_add=True)
    professor=models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='cursos_criados'
    )
    def __str__(self):
        return self.titulo
class Modulos(models.Model):
    cursos=models.ForeignKey(
        Curso,
        related_name='modulos',
        on_delete=models.CASCADE)
    modulo=models.CharField(max_length=250)
    descricao=models.TextField(max_length=300)
    criacao=models.DateTimeField(auto_now_add=True)
    link=models.URLField()
    def __str__(self):
        return f'{self.modulo} ({self.cursos})'

class Aluno(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='aluno')
    nome=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    cursos=models.ManyToManyField(Curso,related_name='alunos',through='Inscricoes')
    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    aluno=models.ForeignKey(Aluno,on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE,related_name='avaliacoes')
    nota=models.IntegerField(choices=NUMEROS_CHOICES)
    comentario=models.TextField(max_length=300)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno} - {self.curso}'

class Inscricoes(models.Model):
    aluno=models.ForeignKey(Aluno,on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE,related_name='inscricoes')
    data_inscricao=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno} - {self.curso}'
    