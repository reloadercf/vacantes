from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Job
from django.db.models import Q
from .forms import NewJobForm
# Create your views here

class Trabajo(View):
    def get (self, request):
        queryset=Job.objects.all().filter(avalible=True)
        search=request.GET.get('search')
        if search:
            queryset=queryset.filter(
                Q(name__icontains=search)

            ).distinct()
        template_name="job/bolsa.html"
        context={
            'jobs':queryset
        }
        return render(request, template_name, context)

class JobDetail(View):
    def get(self, request, id):
        queryset=Job.objects.get(id=id)
        template_name="job/job_detail.html"
        context={
            'object':queryset
        }

        return render(request,template_name,context)

class JobCreate(View):
    def get(self, request):
        template_name="job/job_create.html"
        form= NewJobForm
        context={
            'form':form
        }
        return render(request,template_name,context)

    def post(self,request):
        print(request.POST)
        form= NewJobForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('bolsadechamba:job')

class JobEdit(View):
    def get(self, request, id):
        template_name="job/job_create.html"
        queryset=Job.objects.get(id=id)
        form = NewJobForm(instance=queryset)
        context={
            'form':form
        }
        return render(request, template_name, context)
    def post(self,request,id):
        queryset=Job.objects.get(id=id)
        form=NewJobForm(request.POST, instance=queryset)
        if form.is_valid:
            form.save()
        return redirect('bolsadechamba:detail',id)

class JobDelete(View):
    def get(self, request,id):
        queruset=Job.objects.get(id=id)
        queruset.delete()
        return redirect('bolsadechamba:job')