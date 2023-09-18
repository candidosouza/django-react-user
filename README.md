# Py Users

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Documentação da API](#documentação-da-api)
- [Endpoints de Autenticação](#endpoints-de-autenticação)
- [Endpoints da API](#endpoints-da-api)
- [Endpoints do Frontend](#endpoints-do-frontend)
- [testes](#testes)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

Este projeto consiste em uma aplicação que envolve uma API backend desenvolvida com Django e Django Rest Framework e um frontend construído com React e TypeScript. A aplicação é voltada para gerenciar usuários, permitindo operações como criar, atualizar, visualizar e excluir contas de usuário incluindo autenticação via JWT.

## Dependências


- Docker

## Tecnologias

- Django
- Django REST framework
- React
- TypeScript

## Instalação

clone o projeto
    
```bash
git clone https://github.com/candidosouza/django-react-user.git
```

entre na pasta do projeto

```bash
cd django-react-user
```

suba o container

```bash
docker-compose up -d
```

### Acessando a API
acesse o container da api 

```bash
docker compose exec api bash
```

ative o ambiente virtual

```bash
poetry shell
```

rode as migrations

```bash
python manage.py migrate
```

rode as fixtures

```bash
python manage.py seeds
```

suba o servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

acesse o servidor local

```bash
http://localhost:8000/
```

### Acessando o Frontend
acesse o container do frontend 

```bash
docker compose exec frontend bash
```

instale as dependências

```bash
npm install
```

suba o servidor

```bash
npm start
```

acesse o servidor local

```bash
http://localhost:3000/
```

## Documentação da API

A documentação da API está disponível em:

- `/swagger/`
- `/schema.json/`
- `/redoc/`

## Endpoints de Autenticação

- `POST /api/token/` - Solicitação de token JWT
- `POST /api/token/refresh/` - Atualização de token JWT
- `POST /api/token/verify/` - Verificação de token JWT

## Endpoints da API

- `GET /api/` - API Root
- `GET /api/users/` - Lista de usuários
- `POST /api/users/` - Criação de um usuário
- `GET /api/users/<int:pk>/` - Detalhes de um usuário
- `PUT /api/users/<int:pk>/` - Atualização de um usuário
- `PATCH /api/users/<int:pk>/` - Atualização parcial de um usuário
- `DELETE /api/users/<int:pk>/` - Exclusão de um usuário

## Endpoints da Administração

- `/user-platform-admin/` - Página de login do admin

usuário: admin

password: admin


## Endpoints do Frontend

- `/` - Página inicial
- `/` - Login via Modal
- `/` - Cadatro via Modal
- `/` - Págian de perfil do usuário logado
- `/update/<int:id>/` - Página de atualização de usuário
- `/delete/<int:id>/` - Página de exclusão de usuário
- `/logout/` - Página de logout	

## Testes

Para rodar os testes, acesse o container da api 

```bash
docker compose exec api bash
```

ative o ambiente virtual

```bash
poetry shell
```

rode os testes

```bash
python manage.py test
```

## Licença
Este projeto NÃO possui licença.

## Conclusão

Este projeto oferece uma solução para gerenciamento de usuários, com um backend que fornece endpoints para manipulação de dados de usuário e um frontend interativo que permite aos usuários acessarem e atualizarem suas informações.
