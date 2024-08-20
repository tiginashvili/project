from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_note, name='add'),
    path('delete_note/<str:id>/', views.delete_note, name='delete_note'),
    path('update-user/', views.update_user, name='update-user'),
    path('python/', views.python, name='python'),
    path('cpp/', views.cpp, name='cpp'),
]
