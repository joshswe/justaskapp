## AskMe App

This single page application is a Quora-like website that is built with Django and VueJS. Once registered, users will be able to post questions on any topic and answer any question(s) on the site. In addition, they will be able to vote for the best answers added to each question using a Like button; they will also be able to edit or delete their questions or answers at anytime.

The backend of the application was built first, followed by the frontend interface.


## Table of Contents
- [Main Technologies](#main-technologies)
- [Demo](#demo)
  * [1 - Authentication](#1---authentication)
  * [2 - Account Creation](#2---account-creation)
  * [3 - Question Component](#3---question-component)
  * [4 - Answer Component](#4---answer-component)
  * [5 - 404 Not Found](#5---404-not-found)
- [Configuration](#configuration)
    + [Create a virtual environment in the directory](#create-a-virtual-environment-in-the-directory)
    + [Install packages](#install-packages)
    + [Django](#django)
- [Additional Resources](#additional-resources)
- [Commands](#commands)
    + [Slug Testing](#slug-testing)
    + [Vue CLI](#vue-cli)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Main Technologies
- Django
- Django Rest Framework
- Vue.JS
- Node.JS


## Demo

### 1 - Authentication
- User cannot access “JustAsk!” site until he or she is logged in
- User will be asked to enter the correct username and/ or password if the incorrect credentials were entered
- User will be directed to “JustAsk!” homepage after successful login, he or she can choose to logout anytime

![Authentication Demo](/demo-gif/1.authentication_logout.gif){:height="50%" width="50%"}

### 2 - Account Creation
![Account Creation Demo](/demo-gif/2.accountcreation.gif){:height="50%" width="50%"}

### 3 - Question Component
-	Ask new question
    - User can post a new question by clicking on the “Ask Question” button on the homepage
    - The question cannot be empty and can only have maximum length of 240 characters
-	Edit the question
    - User can only edit his/ her own question
    - The question content will be reflected instantly after the edit
-	Delete the question
    - User can only delete his/her own question, this cannot be undone

![Question Component Demo](/demo-gif/3.question_add-edit-delete.gif){:height="50%" width="50%"}

### 4 - Answer Component
-	Each question has a counter (in the homepage) to count its number of answers
-	Publish an answer
    - User can answer to any question, but only once in each question
    - The answer cannot be empty and can only have maximum length of 240 characters
-	Edit the answer
    - User can only edit his/ her own answer
    - The answer content will be reflected instantly after the edit
-	Delete the answer
    - User can only edit his/ her own answer, this cannot be undone
-	Like or unlike the answer
    - User can only like or unlike the other users’ answers
    - Each answer has its own counter to count how many people like that answer

![Answer Component Demo](/demo-gif/4.answer_add-edit-delete-like.gif){:height="50%" width="50%"}

### 5 - 404 Not Found
![404 Not Found Demo](/demo-gif/5.404NotFound.gif){:height="50%" width="50%"}


## Configuration

#### Create a virtual environment in the directory
In Windows environment:
`python -m venv ./venv`
`source ./venv/Scripts/activate`

#### Install packages
- Django and Django Rest Framework:
`pip install django djangorestframework`
- View installed packages:
`pip freeze`
- Export the list of installed packages to requirements.txt:
`pip freeze > requirements.txt`
- Django Rest Auth:
`pip install django-rest-auth`

#### Django
- Initialize the project:
`django-admin startproject JustAsk .`
- Create *users* application:
`python manage.py startapp users`


## Additional Resources
- [Using a custom user model](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)
- [django-registration Documentation](https://buildmedia.readthedocs.org/media/pdf/django-registration/3.0/django-registration.pdf)
- [DRF - Permissions](https://www.django-rest-framework.org/api-guide/permissions/)


## Commands
#### Slug Testing
```
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> custom_user = get_user_model()
>>> u = custom_user.objects.first()
>>> u
<CustomUser: joshua>
>>> from questions.models import Question
>>> q = Question.objects.create(author=u, content="First Question!")
>>> q.slug
'first-question-8cb6ay'
```
#### Vue CLI
In Node.js Command Prompt:
- Install Vue CLI: `npm i -g @vue/cli`
- Create Vue project: `vue create <project-name>`
- Run Vue project: `npm run serve`