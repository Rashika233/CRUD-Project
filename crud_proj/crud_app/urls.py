from django.urls import path
from . import views
urlpatterns=[
    #path('', views.CreateView, name='CreateView'),
    path('data/', views.Retrieve_ListView),
    path('data/<int:_id>',views.Retrieve_DetailView),
]