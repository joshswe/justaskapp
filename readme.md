# AskMe App

This single page application is a Quora-like website that is built with Django and VueJS. Once registered, users will be able to post questions on any topic and answer any question(s) on the site. In addition, they will be able to vote for the best answers added to each question using a Like button; they will also be able to edit or delete their questions or answers at anytime.

The backend of the application was built first, followed by the frontend interface.


# Main Technologies
- Django
- Django Rest Framework
- VueJS

## Libraries
- [django-registration](https://django-registration.readthedocs.io/en/3.0.1/): An extensible application providing user registration functionality for Django-powered Web sites


# Requirements

## Authentication Page
- Login Fields
    - Username
    - Password
- Option to create a new account

## Account Creation Page 
- Account Fields
    - Username
    - Email address
    - Password
    - Password confirmation

## Main Page
- Options/ Buttons
    - Home 
    - Ask a question
    - Logout
- List of questions
    - Title
    - Author
    - Number of answers
- Load more button 
    - At the bottom of the page

## Question Page
- Question title
- Author
- Published date
- List of replies
    - Author
    - Published date
    - Number of likes
- Has the user answered the question?
    - Yes
        - Option to answer the question
        - Answer field
        - Submit button
    - No
        - Message that indicates the user has already answered the question
        - Option to edit the answer
        - Option to delete the answer

## Ask a question page
- Text field area for the question
- Publish button


# Configuration

## Create a virtual environment in the directory
In Windows environment:
`python -m venv ./venv`
`source ./venv/Scripts/activate`

## Install packages
- Django and Django Rest Framework:
`pip install django djangorestframework`
- View installed packages:
`pip freeze`
- Export the list of installed packages to requirements.txt:
`pip freeze > requirements.txt`
- Django Rest Auth:
`pip install django-rest-auth`

## Django
- Initialize the project:
`django-admin startproject JustAsk .`
- Create *users* application:
`python manage.py startapp users`


# Additional Resources
- [Using a custom user model](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)
- [django-registration Documentation](https://buildmedia.readthedocs.org/media/pdf/django-registration/3.0/django-registration.pdf)
