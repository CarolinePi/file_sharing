from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_new, name='index'),
    path('my_uploading/', views.show_files, name='my_uploading'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.new_page, name='new_page')
]

handler404 = views.handler404

