from django.urls import path
from .views import CriarAlunoAPIView,CursoAPIView,CursosAPIView,CursosDosAlunosAPIView,AvaliacaoAPIView,AvaliacoesAPIView,PerfilAPIView,ModuloAPIView,CriarProfessorAPIView,AlunosDoMeuCursoAPIView,InscreverNoCursoAPI,VerModuloAPIView


urlpatterns = [
    path('perfil/',PerfilAPIView.as_view(),name='perfil'),
    path('curso/',CursoAPIView.as_view(),name='curso'),
    path('cursos/',CursosAPIView.as_view(),name='cursos'),
    path('cursos/user/',CursosDosAlunosAPIView.as_view(),name='cursos_inscritos'),
    path('cursos/alunos/inscritos/<int:curso_id>/',AlunosDoMeuCursoAPIView.as_view(),name='alunos_inscritos'),
    path('curso/inscrever/<int:curso_id>/',InscreverNoCursoAPI.as_view(),name='inscrever_curso'),
    path('register/professor/',CriarProfessorAPIView.as_view(),name='professor_register'),
    path('register/aluno/',CriarAlunoAPIView.as_view(),name='aluno_register'),
    path('cursos/<int:curso_id>/modulo/',ModuloAPIView.as_view(),name='modulo'),
    path('cursos/<int:curso_id>/modulos/',VerModuloAPIView.as_view(),name='ver_modulos'),
    path('avaliar/<int:curso_id>/',AvaliacaoAPIView.as_view(),name='avaliar'),
    path('avaliacoes/',AvaliacoesAPIView.as_view(),name='avaliacoes')
]
