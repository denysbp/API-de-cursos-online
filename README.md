# API-de-cursos-online


## **Descrição**
Esta é uma **API RESTful** desenvolvida com **Django** e **Django REST Framework** para gerenciar cursos online.  
Ela permite:

- **Gerenciar usuários** (alunos e professores)
- **Criar e listar cursos** e seus módulos
- **Permitir que alunos se inscrevam** em cursos
- **Gerenciar avaliações** de cursos
- **Controlar permissões** entre alunos e professores

> Ideal para aprendizado de backend e prática de desenvolvimento de APIs REST seguras.

---

## **Funcionalidades**

- Cadastro e autenticação de usuários (aluno e professor)
- CRUD de cursos e módulos (**somente professores podem criar/editar**)
- Inscrição de alunos em cursos
- Avaliações de cursos com nota e comentário
- Endpoints customizados para progresso e cursos populares
- Permissões e autenticação com DRF

---

## **Endpoints da API**

| **Endpoint** | **Método** | **Descrição** |
|--------------|------------|---------------|
| `/perfil/`   | GET        | Retorna informações do perfil do usuário logado |
| `/curso/`    | POST       | Visualizar ou criar um curso (**somente professores podem criar**) |
| `/cursos/`   | GET        | Lista todos os cursos disponíveis |
| `/cursos/user/` | GET     | Lista os cursos em que o aluno está inscrito |
| `/cursos/alunos/inscritos/<int:curso_id>/` | GET | Lista todos os alunos inscritos em um curso (**somente professores do curso**) |
| `/curso/inscrever/<int:curso_id>/` | POST | Permite que um aluno se inscreva em um curso |
| `/register/professor/` | POST | Cria um usuário do tipo professor |
| `/register/aluno/` | POST | Cria um usuário do tipo aluno |
| `/cursos/<int:curso_id>/modulo/` | POST | Visualizar ou criar um módulo em um curso (**somente professores podem criar**) |
| `/cursos/<int:curso_id>/modulos/` | GET | Listar todos os módulos de um curso |
| `/avaliar/<int:curso_id>/` | POST | Permite que o aluno avalie um curso |
| `/avaliacoes/` | GET | Lista todas as avaliações existentes |

---

## **Permissões**

- **Professores**: podem criar/editar cursos e módulos
- **Alunos**: podem se inscrever em cursos e avaliar
- **Usuários não autenticados**: não podem acessar endpoints

---

## **Administração**

O Django Admin permite gerenciar:

- Usuários
- Cursos
- Módulos
- Avaliações

> Acesse em: `http://127.0.0.1:8000/admin/`

---

## **Segurança e Variáveis Secretas**

- **Nunca inclua a SECRET_KEY** diretamente no repositório.
- Use **variáveis de ambiente** ou arquivos `.env` para armazenar informações sensíveis.

---

## **Contribuição**

- Pull requests são bem-vindos!
- Garanta que **nenhum arquivo sensível** seja enviado.
- Teste todas as funcionalidades antes de enviar alterações.

---

## **Licença**

Este projeto é **open source** e pode ser usado para estudo, modificação e aprendizado.