from django.urls import path
from websites.views import *

urlpatterns=[
    path('',home ,name='home'),
    path('home/',home ,name='home'),

    path('about/', about, name='about'),
    path('contact/', contact , name='contact'),
    path('projects/', projects, name='projects'),
    path('skills/', skills, name='skills'),
]