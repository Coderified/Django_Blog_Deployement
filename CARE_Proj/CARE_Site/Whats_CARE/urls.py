from django.urls import path
from . import views

urlpatterns=[
    path('',views.Carebasic,name='CARE'),
    path('titlelinks',views.basicview,name='titlelinks'),
    path("<int:pk>/",views.detailview,name='detaillink'),
    
]