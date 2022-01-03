# Hacker News

Hackernews clone that sync with the hackernews website

[![cookiecutter-django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Technologies

- [Python 3.9](https://python.org): Base programming language for development
- [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
- [PostgreSQL](https://www.postgresql.org/): Application relational databases for development, staging and production environments
- [Django Framework](https://www.djangoproject.com/): Development framework used for the application
- [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
- [Celery](https://github.com/celery/celery): A simple, flexible, and reliable distributed system to process vast amounts of tasks
- [Django Celery Beat](https://github.com/celery/django-celery-beat): A Database Period task scheduler
- [Flower](https://github.com/mher/flower): A web based tool for monitoring and administrating Celery clusters.
- [Redis](https://github.com/redis/redis-py): A NoSQL Database that serves as a Celery Broker and Result Backend
- [Aiohttp](https://docs.aiohttp.org/en/stable/): An Asynchronous HTTP Client/Server for asyncio and Python.
- [MailHog](https://github.com/mailhog/MailHog): MailHog is an email testing tool for developers
- [Sphinx](https://github.com/sphinx-doc/sphinx): Sphinx is a tool that makes it easy to create intelligent and beautiful documentation for Python projects
- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## How To Start App

- Clone the Repository
- Run `docker-compose -f local.yml build`

  - Running the above command for the first time will download all docker-images and third party packages needed for the app.
  - **NB: This will take several minutes for the first built, others will be in a blink of an eye**

- Run `docker-compose -f local.yml up`

  - Running the above command will Start up the following Servers:
    - Postgres Server --> http://localhost:5432
    - Django Development Server --> http://localhost:8000
    - Redis Server --> http://localhost:6379
    - Flower --> http://localhost:5555
    - MailHog --> http://localhost:8025
    - Sphinx Docs --> http://localhost:7000

- Run Migrations `docker-compose -f local.yml exec django python3 manage.py makemigrations`
- Run Migrate `docker-compose exec django python3 manage.py migrate`

## Exploring The App

Make sure that all the above servers are running before you start exploring the project. If those servers are up and running, have fun with the app!!!

### HackerNews App

You can explore the Hackernews App by going to `http://localhost:8000` on your browser. You will be able to see the following features

1. View list of paginated latest hackersnews
2. Filter hackernews by type: `story`, `job` and `poll`
3. Search hackernews by text
4. View News Details page with Comments
5. Sign up
6. Login
7. Forgot and Reset password
8. Login to Django Admin on `http://localhost:8000/admin`

### API

You can explore the Hackernews App by going to `http://localhost:8000/api` on your browser. The following endpoints are accessible

1. GET News --> `http://localhost:8000/api/news/`
2. GET Paginated news --> `http://localhost:8000/api/news/?limit=10&offset=10`
3. GET Filtered news by type
   1. For story --> http://localhost:8000/api/news/?type=story
   2. For poll --> http://localhost:8000/api/news/?type=poll
   3. For job --> http://localhost:8000/api/news/?type=job
4. POST News --> `http://localhost:8000/api`
5. PUT News --> `http://localhost:8000/api` if only created by user
6. DELETE News --> `http://localhost:8000/api` if only created by user

### Flower

You can also monitor and administer Hackernews Background Job with flower. Go to `http://localhost:5555` on your browser.

Login with `username: debug` and `password: debug`

### Sphinx

You can visit `http://localhost:7000` to read the Sphinx auto generated documentation
