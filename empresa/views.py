from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Empresa
from django.db.models import Q
from .forms import  NewEmpresaForm
# Create your views here



class Company(View):
    def get (self, request):
        query=Empresa.objects.all().filter(avalible=True)
        template_name="empresa/listaempresa.html"
        search = request.GET.get('search')
        if search:
            query = query.filter(
                Q(nombre_empresa__icontains=search) |
                Q(direccion__icontains=search)
            ).distinct()
        context={
            'empresas':query
        }
        return render(request, template_name, context)


class CompanyDetail(View):
    def get(self, request, id):
        queryset = Empresa.objects.get(id=id)
        template_name = "empresa/empresa_detail.html"
        context = {
           'object': queryset
         }

        return render(request, template_name, context)


class EmpresaCreate(View):
    def get(self, request):
        template_name="empresa/empresa_create.html"
        form=  NewEmpresaForm
        context={
            'form':form
        }
        return render(request,template_name,context)

    def post(self,request):
        print(request.POST)
        form= NewEmpresaForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('company:empresas')