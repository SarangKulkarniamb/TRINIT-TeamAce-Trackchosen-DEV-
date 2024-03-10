from django.shortcuts import render,redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login , logout
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user,allowed_users
# Create your views here.
@unauthenticated_user
def loginpage(request):
    page='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            dj_login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or password does not exist')
            
    context={'page': page}
    return render(request,'login_register.html',context)


def logoutuser(request):
    logout(request)
    return redirect('home')

@unauthenticated_user
def registerpage(request):
    form=UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            username=form.cleaned_data.get('username')
            username=str(username)
            if username.endswith('@student'):

                group=Group.objects.get(name='Students')
                user.groups.add(group)
            elif username.endswith('@teacher'):
                group=Group.objects.get(name='Teachers')
                user.groups.add(group)
            dj_login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occurred during registration')
    return render(request,'login_register.html',{'form':form})

def home(request):
    return render(request,'home.html',{})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def data(request):
    all_members=member.objects.all
    return render(request,'data.html',{'all':all_members})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def student(request):
    
    return render(request,'student.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teachers'])
def teacher(request):
    
    return render(request,'teacher.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def create_customer(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create_customer.html',{'form':form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def create_order(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create_order.html',{'form':form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Teachers'])
def create_course(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create_course.html',{'form':form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def filter(request):
    qs=product.objects.all()
    
    course_name_query=request.GET.get('name')
    host_query=request.GET.get('host')
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('host')
    min_experience=request.GET.get('min_experience')
    
    if course_name_query!='' and course_name_query is not None:
        qs=qs.filter(name__icontains=course_name_query)
    if host_query!='' and host_query is not None:
        qs=qs.filter(host__icontains=host_query)
    if min_price!='' and min_price is not None:
        qs=qs.filter(price__gte=min_price)
    if max_price!='' and max_price is not None:
        qs=qs.filter(price__lte=max_price)
    if min_experience!='' and min_experience is not None:
        qs=qs.filter(experience__gte=min_experience)
    context={'queryset':qs}
    return render(request,'filter.html',context)



