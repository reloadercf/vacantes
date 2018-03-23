from django.urls import path
from .views import Trabajo,JobDetail,JobCreate,JobEdit,JobDelete

app_name='job'

urlpatterns=[
    path('',Trabajo.as_view(),name="job"),
    path('<int:id>/',JobDetail.as_view(),name='detail'),
    path('new/', JobCreate.as_view(),name='new'),
    path('edit/<int:id>', JobEdit.as_view(), name="editar"),
    path('delete/<int:id>',JobDelete.as_view(),name="delete"),
]