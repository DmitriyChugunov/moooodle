from django.urls import path

from .views import home, errors_task, user_task

urlpatterns = [
    path('user/<str:login>/<str:name_post>/<int:id_post>', user_task, name='user'),
    path('user/<str:login>/<str:name_post>', user_task, name='user'),
    path('user/<str:login>', user_task, name='user'),
    path('error/', errors_task, name='error'),
    path('user', user_task, name='user'),
    path('', home, name='home'),

]