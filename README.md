# Charity Organization Event Website

## INTRO
A membership website for charities written in Django and Wagtail CMS.

Charity owners can create an account and add a profile for their charity. 

The site admin has to approve all charity organization profiles.

Once approved, the charity owner can login and create 'event' objects to tell the world about upcoming fundraising events.

## FEATURES
- Approved charities listed in paginated pages.
- Approved events listed in paginated pages.
- Users can create a charity profile
- Users can create events
- Admin has to approve all users and events before they appear on the website.

## TOOLS 
- Django
- Wagtail
- Bootstrap
- python-decouple
- django-countries
- Pillow
- CustomUser model - extends AbstractUser
- UserCreationForm
- UserChangeForm
- Django registration, login and password reset system

### To Do
- [ ] Add custom user settings to the wagtail admin dashboard
- [ ] Add a news blog app
- [y] Add a search events page - add to the menu
- [ ] Add a link to the main blog page to the menu

## SCREENSHOTS

### 1. Homepage

![homepage](https://github.com/richardgourley/charity-organization-event-website/blob/main/sreenshots/homepage.png)

### 2. SignUp Page
- Extends the standard Django user model using AbstractUser

![signuppage](https://github.com/richardgourley/charity-organization-event-website/blob/main/sreenshots/signuppage.png)

### 3. Profile Page 

![profilepage](https://github.com/richardgourley/charity-organization-event-website/blob/main/sreenshots/profilepage.png)

### 4. Events Page

![eventspage](https://github.com/richardgourley/charity-organization-event-website/blob/main/sreenshots/events.png)

## GETTING STARTED

New to Django and/ or Wagtail? To setup Django and Wagtail with Bootstrap and a bespoke database see my other repo for a step by step guide: https://github.com/richardgourley/django-wagtail-stepbystep

```
virtualenv charityeventwebsite -p python3`
cd charityeventwebsite
source bin/activate
pip install wagtail
wagtail start charityorganizationeventwebsite
cd charityorganizationeventwebsite
pip install -r requirements.txt
```

Set up a database table and assign priveliges.
Create a file called '.env' and add:
```
SECRET_KEY=12345etc.
DEBUG=True
DB_NAME=mysite
DB_USER=newusername
DB_PASSWORD=password
DB_HOST=127.0.0.1
PORT=3306
```

Install python decouple, any database client you require (MySQL example used here) 
```
pip install python-decouple
pip install mysqlclient
```

Install django-countries

`pip install django-countries`

See files in '/settings' dir to see how to set up python-decouple 'config', django-countries, abstract user and bespoke database.

```
python manage.py startapp accounts
python manage.py startapp events
```

NOTE: Setup custom user code from the app 'accounts' **before** the first migration:

See https://learndjango.com/tutorials/django-custom-user-model for more on custom user models.

Usual python web application creation
```
python manage.py makemigrations accounts
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## RELATED
There is some debate over whether to use a Custom User model or to create a one-to-one field for a model called 'Profile' linked to a user.  Here are some links that discuss the topic further: 

https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html

https://github.com/guettli/django-tips