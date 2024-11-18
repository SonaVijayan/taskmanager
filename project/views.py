from django.shortcuts import render,redirect
from django.views import View
from .forms import ProjectModelForm
from . models import Projects
from django.contrib import messages


# Create your views here.
class ProjectDashboardView(View):
    def get(self,request):
        data=Projects.objects.all()
        return render(request,"pdashboard.html",{"projects":data})
    
class AddProjectView(View):
    def get(self,request):
        form=ProjectModelForm()
        return render(request,"addproject.html",{"form":form})
    def post(self,request):
        formdata=ProjectModelForm(data=request.POST,files=request.FILES)
        
        
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Project Added Successfully ")
            messages.error(request,'Checking!!!')
            return redirect('pdash')
        messages.error(request,'invalid data')
        return render(request,'padd.html',{'form':formdata})

           

class DeleteTaskView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        project=Projects.objects.get(id=tid)
        project.delete()
        return redirect('pdash')

class EditProjectView(View):
    def get(self,request,**kwargs):
        pid=kwargs.get('id')
        
        project=Projects.objects.get(id=pid)
        form=ProjectModelForm(instance=project)
        return render(request,"pedit.html",{"form":form})
    def post(self,request,**kwargs):
        
        pid=kwargs.get('id')

        project=Projects.objects.get(id=pid)
        formdata=ProjectModelForm(data=request.POST,files=request.FILES,instance=project)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,'project edited successfully')
            return redirect('pdash')
            
            
        return render(request,"pedit.html",{"form":formdata})

 