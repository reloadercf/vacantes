from django.urls import path
from .views import Company,CompanyDetail,EmpresaCreate,EmpresaEdit

app_name='empresa'

urlpatterns=[
    path('',Company.as_view(),name="empresas"),
    path('<int:id>/',CompanyDetail.as_view(),name='detail'),
    path('new/', EmpresaCreate.as_view(), name='new'),
    path('edit/<int:id>', EmpresaEdit.as_view(), name="editar"),
]