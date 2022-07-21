from django.urls import path
from . import views

urlpatterns = [
    path('users_management/', views.users_management),
    path('api/', views.apiOverview, name='api-overview'),
    
    path('roles-list/', views.rolesList, name='roles-list'),
    path('roles-details/<str:pk>/', views.rolesDetail, name='roles-details'),
    path('roles-create/', views.rolesCreate, name='roles-create'),
    path('roles-update/<str:pk>/', views.rolesUpdate, name='roles-update'),
    path('roles-delete/<str:pk>/', views.rolesDelete, name='roles-delete'),
]