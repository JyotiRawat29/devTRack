### Brief(h3)

**What you are building** 
A backend API for tracking engineering issues. Engineers report bugs, assign priorities, and track status similar to a stripped-down GitHub Issues.

**Context**
Every engineering team tracks work bugs filed, priorities set, statuses updated. DevTrack is a minimal backend for this. You will build the Django project, model the data using OOP, wire up URL routing, and expose endpoints testable in Postman.

**Data model**
Two entities. Keep it simple.

**Reporter**
A person who files issues-

    1.id - unique integer
    2.name - full name
    3.email - contact email
    4.team - e.g. backend, frontend, devops

**Issue**
A bug report or task filed by a Reporter-

id - unique integer
title - short summary
description - full details
status - one of: open, in_progress, resolved, closed
priority - one of: low, medium, high, critical
reporter_id - ID of the Reporter who filed this
created_at - optional, use str(datetime.now())

*Create two classes named issue and reporter i.e. issue.py and reporter.py*
*Since we are using django, we will not create these classes from scratch at any location instead, we inititalise the Django configs, to give us a structure. following are the commands to use-*
    *1. django-admin startproject config. It creates [settings.py,urls.py--inside config] and manage.py--at root folder*
    *2. In settings.py, INSTALLED_APPS, add issues, rest_framework---installing a package is not always enough in Django, you usually need to register them via INSTALLED_APPS when needed.*
    *3. These are called Django apps, and if we are adding more features that are not similiar to each other, we create separate apps and those are added inside INSTALLED_APPS*
    *4. python manage.py startapp issues---Creates tasks folder with admin.py, apps.py, models.py,tests.py and views.py file. since our entity name is issues, we use here issues instead of tasks*
**Relationship**
One Reporter can file many Issues. 
This is a 1:many relationship - store reporter_id inside the Issue, not the other way around.


**OOP design**
Model both entities as Python classes before writing any Django code.

*Here we know, 2 classes issues and reporter needs tobe created having one(reporter) to many(issues) property (inheritence or polymorphism: not sure)*
#######################################################################################################33**Part A - BaseEntity, validate(), and to_dict()**
Create an abstract base class BaseEntity. Reporter and Issue must both inherit from it.
issues/models.py
# In views.py:
# from issues.models import Reporter, Issue

*inside issues/models create abstract class Basentity having function def validate to be overriden in child classes. Create 2 child classes-- 1.Reporter 2. Issue, define their attributes as given above and override function validate as per given instructions*
*in views.py import Reporter and Issue*

**Part B - Priority subclasses using inheritance**
Create two subclasses of Issue that override a describe() method. This is the same method overriding pattern from the add_two_numbers example in class.
In your POST /api/issues/ view, instantiate the correct subclass based on priority and include describe() in the response. For medium and high priority, use the base Issue class.

*1. Django endpoints are built by connecting view to a URL route.*
*2. A view is a function that takes request and return response. View is like a controller in Django's request flow.*
*3. views.py is where API logic starts.*
*4. Add the endpoint functions inside urls.py(at app level-issues), in the list urlpatterns*
*5. Add the path in urls.py at root level(config-->urls.py)*

In screenshot folder, pictures from postman are there for both reporter and issues endpoints
**Flow**
*1.In views.py create as view class for reporter and issue for their corresponding endpoints; ReporterView, IssueView both child class of APIView*
*2.In URLS.py (issues) add the endpoint issues/ and reporters/ for respective views*
*3.Add get and post function in both classes according to the given condition in the assignment*
