from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.Index.as_view(),name='index'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('addstudent/',views.Addstudent.as_view(),name='addstudent'),
    path('showstudents/',views.Showstudents.as_view(),name='showstudents'),
    path('editstudent/',views.Editstudent.as_view(),name='editstudent'),
    path('deletestudent/',views.Deletestudent.as_view(),name='deletestudent'),
    path('showstaffs/',views.Showstaffs.as_view(),name='showstaffs'),
    path('profile/',views.Profile.as_view(),name='profile'),

]