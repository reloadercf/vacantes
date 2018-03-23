from django.urls import path
from .views import Company,CompanyDetail,EmpresaCreate

app_name='empresa'

urlpatterns=[
    path('',Company.as_view(),name="empresas"),
    path('<int:id>/',CompanyDetail.as_view(),name='detail'),
    path('new/', EmpresaCreate.as_view(), name='new'),
]