from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainhome,name='mainhome'),
    path('courses/',views.courses,name='courses'),
    path('trainers/',views.trainers,name='trainers'),
    path('contact/',views.contact,name='contact'),
path('login/',views.login,name='login'),
path('signup/',views.signup,name='signup'),
path('forgpass/',views.forgpass,name='forgpass'),
path('logout/',views.logout,name='logout')
]