from django.shortcuts import render,redirect
from django.views import View
from .forms import TaskForm,LogForm,RegForm
from django.http import HttpResponse
from .models import Task
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# this is def based view:
# def landingView(request):
#     return render(request,"landing.html")
class LoginView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        formdata=LogForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('landing')
            else:
                return redirect('log')
        return render(request,'login.html',{"form":formdata})

            
       

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():

            formdata.save()
            return redirect('log')
        return render(request,"reg.html",{"form":formdata})

# class based view for above landing.html:
class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")

# def dashboardView(request):
#     return render(request,"dashboard.html")

# class based view for above dashboard.html:
class DashboardView(View):
    def get(self,request):
        data=Task.objects.all()
        return render(request,"dashboard.html",{"data":data})

class AddTaskView(View):
    def get(self,request):
        form=TaskForm()

        return render(request,"add.html",{"form":form})
    def post(self,request):
        formdata=TaskForm(data=request.POST)
        if formdata.is_valid():
            title=formdata.cleaned_data.get("title")
            descp=formdata.cleaned_data.get("description")
            dt=formdata.cleaned_data.get("date")
            tm=formdata.cleaned_data.get("time")
            Task.objects.create(title=title,description=descp,date=dt,time=tm)
            return redirect("dashboard")

            
    
        return render(request,"add.html",{"form":formdata})

class DeleteTaskView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        task=Task.objects.get(id=tid)
        task.delete()
        return redirect('dashboard')

class EditTaskView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        task=Task.objects.get(id=tid)
        form=TaskForm(initial={"title":task.title,"description":task.description,"date":task.date,"time":task.time})
        return render(request,"edit.html",{"form":form})
    def post(self,request,**kwargs):
        formdata=TaskForm(data=request.POST)
        tid=kwargs.get('id')

        task=Task.objects.get(id=tid)
        if formdata.is_valid():
            title=formdata.cleaned_data.get("title")
            descp=formdata.cleaned_data.get("description")
            dt=formdata.cleaned_data.get("date")
            tm=formdata.cleaned_data.get("time")
            task.title=title
            task.description=descp
            task.date=dt
            task.time=tm
            task.save()
            
            return redirect("dashboard")
        return render(request,"edit.html",{"form":formdata})
