from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_admin_panel, name='custom_admin_panel'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]