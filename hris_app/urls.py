from django.contrib import admin
from django.urls import path
from . import views 



urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('userdashboard/<str:pk>', views.userdashboard, name='userdashboard'),
    path('admindashboard/<str:pk>', views.admindashboard, name='admindashboard'),
    path('personalinfo/<str:pk>', views.personalinfo, name='personalinfo'),
    path('familybackground/<str:pk>', views.familybackground, name='familybackground'),
    path('educationalbackground/<str:pk>', views.educationalbackground, name='educationalbackground'),
    path('civilservice/<str:pk>', views.civilservice, name='civilservice'),
    path('delete_civilservice/<str:pk>', views.delete_civilservice, name='delete_civilservice'),
    path('workexperience/<str:pk>', views.workexperience, name='workexperience'),
    path('delete_workexperience/<str:pk>', views.delete_workexperience, name='delete_workexperience'),
    path('voluntarywork/<str:pk>', views.voluntarywork, name='voluntarywork'),
    path('delete_voluntarywork/<str:pk>', views.delete_voluntarywork, name='delete_voluntarywork'),
    path('learning/<str:pk>', views.learning, name='learning'),
    path('delete_learning/<str:pk>', views.delete_learning, name='delete_learning'),
    path('otherinfo/<str:pk>', views.otherinfo, name='otherinfo'),
    path('miscellaneousinfo/<str:pk>', views.miscellaneous_info, name='miscellaneousinfo'),
    path('delete_otherinfo/<str:pk>', views.delete_otherinfo, name='delete_otherinfo'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('editprofile/<str:pk>', views.editprofile, name='editprofile'),
    path('admindashboard_activate/<str:pk>', views.admindashboard_activate, name='admindashboard_activate'),
    path('admindashboard_deactivate/<str:pk>', views.admindashboard_deactivate, name='admindashboard_deactivate'),
    path('page1', views.generate_pdf, name='page1'),
    path('page2', views.generate_pdf2, name = 'page2'),
    path('page3', views.generate_pdf3, name = 'page3'),
    path('page4', views.generate_pdf4, name = 'page4'),
    path('report/<str:pk>', views.report, name='report'),
    path('viewuser/<str:pk>', views.viewuser, name='viewuser'),
    path('admin_page1/<str:pk>', views.admin_generate_pdf, name='admin_page1'),
    path('admin_page2/<str:pk>', views.admin_generate_pdf2, name='admin_page2'),
    path('admin_page3/<str:pk>', views.admin_generate_pdf3, name='admin_page3'),
    path('admin_page4/<str:pk>', views.admin_generate_pdf4, name='admin_page4'),

    path('accounts/inactive/', views.inactive, name='inactive'),
]
