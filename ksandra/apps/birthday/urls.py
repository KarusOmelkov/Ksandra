from django.urls import path

from . import views

app_name = 'birthday'
urlpatterns = [
    path('', views.code),
    path('code/', views.code, name='code'),
    path('activated/', views.activated, name='activated'),
    path('instruction/', views.instruction, name='instruction'),
    path('prize/', views.prize, name='prize'),
    path('prize/<str:code>', views.prize_code, name='prize_code'),
    path('poem/', views.prize_poem, name='prize_poem'),
    path('poem_two/', views.prize_poem_two, name='prize_poem_two')
]

