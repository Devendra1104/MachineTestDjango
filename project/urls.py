from django.urls import path
from . import  views

urlpatterns = [
    path('GET/clients/',views.ClientList.as_view(),name = 'clients'), # List of all clients
    path('POST/clients/',views.ClientCreateView.as_view(),name = 'createclient'), # Create new client
    path('UPDATE/clients/<int:pk>/',views.ClientUpdateView.as_view(),name = 'clientsdetail'), # Update existing client info
    path('DELETE/clients/<int:pk>/',views.ClientDeleteView.as_view(),name='clientdelete'), # Delete existing client
    path('GET/clients/<int:pk>/',views.ClientProjectView.as_view(),name = 'clientProjects'),
    path('GET/projects/',views.UserProjectView.as_view(),name = 'userProject'),
    path('clients/<int:pk>/projects/',views.CreateProjectView.as_view(),name = 'createProject'),
]