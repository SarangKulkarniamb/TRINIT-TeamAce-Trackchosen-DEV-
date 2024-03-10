from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns=[
    path('', views.home , name="home"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registerpage,name="register"),
    path('data/',views.data,name="data"),
    path('student/',views.student,name="student"),
    path('teacher/',views.teacher,name="teacher"),
    path('create_customer/',views.create_customer,name="create_customer"),
    path('create_order/',views.create_order,name="create_order"),
    path('create_course/',views.create_course,name="create_course"),
    path('filter/',views.filter,name="filter")

]