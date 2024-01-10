"""
URL configuration for cepro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ceapp import views 
from ceapp.views import index,loginn,loggout,register,about,service,product,contact,adindex,admember,adaddmember,adappointment,adcrop,adinbox,admailview,adcompose,adaddappointment,adaddcrop,adblog,adaddblog,adeditblog,adblogdetails,adcalendar,adeditprofile,adapproval,mindex,mblog,mcalendar,mcrop,mappointment,mlogin
from django.conf import settings
from django.conf.urls.static import static
from ceapp.views import ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("allauth.urls")),
    # path('home/', include('ceapp.urls')),
    path('',views.index, name='index'),
    path('loginn',loginn,name='loginn'),
    path('signup',register,name='signup'),
    path('homepage',views.homepage,name='homepage'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('product',views.product,name='product'),
    path('contact',views.contact,name='contact'),
    path('crop',views.crop,name='crop'),
    path('apply/<int:crop_id>/',views.apply,name='apply'),
    path('applyerror',views.applyerror,name='applyerror'),
    path('fmyprofile',views.fmyprofile,name='fmyprofile'),

    path('disapply',views.disapply,name='disapply'),
    path('ceditprofile',views.ceditprofile, name='ceditprofile'),
    path('application', views.application, name='application'),

    # path('fnotifications',views.notifications,name='fnotifications'),

    # path('notifications',views.notifications,name='notifications'),


    # path('index2',views.index2,name='index2'),
    # path('aindex2',views.aindex2,name='aindex2'),
    path('adindex',views.adindex,name='adindex'),
    path('admember',views.admember,name='admember'),
    # path('alogin',views.alogin,name='alogin'),
    # path('aprofile',views.aprofile,name='aprofile'),
    # path('aeditprofile',views.aeditprofile,name='aeditprofile'),
    # path('asettings',views.asettings,name='asettings'),
    path('adaddmember',adaddmember,name='adaddmember'),
    # path('aeditmember',views.aeditmember,name='aeditmember'),
    # path('afarmers',views.afarmers,name='afarmers'),
    path('adappointment',views.adappointment,name='adappointment'),
    path('adaddappointment',views.adaddappointment,name='adaddappointment'),
    path('adcrop',views.adcrop,name='adcrop'),
    path('adaddcrop',adaddcrop,name='adaddcrop'),
    path('adcompose',views.adcompose,name='adcompose'),
    path('adinbox',views.adinbox,name='adinbox'),
    path('admailview',views.admailview,name='admailview'),
    path('adblog',views.adblog,name='adblog'),
    path('adaddblog',adaddblog,name='adaddblog'),
    path('adeditblog',views.adeditblog,name='adeditblog'),
    path('adblogdetails',views.adblogdetails,name='adblogdetails'),
    path('adcalendar',views.adcalendar,name='adcalendar'),
    path('adeditprofile',views.adeditprofile,name='adeditprofile'),
    path('adapproval', views.adapproval, name='adapproval'),
    # path('adapproval',views.adapproval,name='adapproval'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adsettings',views.adsettings,name='adsettings'),
    path('adpendinglist',views.adpendinglist,name='adpendinglist'),
    path('adpendingapproval',views.adpendingapproval,name='adpendingapproval'),
    path('adreport',views.adreport,name='adreport'),
    path('admeeting',views.admeeting,name='admeeting'),
    path('adaddmeeting',views.adaddmeeting,name='adaddmeeting'),
    path('edit_meeting/<int:meeting_id>/', views.edit_meeting, name='edit_meeting'),
    path('delete_meeting/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),

    path('delete_crop/<int:crop_id>/', views.delete_crop, name='delete_crop'),
    path('edit_crop/<int:crop_id>/', views.edit_crop, name='edit_crop'),
    path('search_crop', views.search_crop, name='search_crop'),
    
    path('search_member', views.search_member, name='search_member'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    # path('reduce_crop_count/<int:crop_id>/', views.reduce_crop_count, name='reduce_crop_count'),
    # path('reduce_crop_count/<int:crop_id>/', views.reduce_crop_count, name='reduce_crop_count'),
    path('combined_details/', views.combined_details, name='combined_details'),
    path('generate_pdfreport/', views.generate_pdfreport, name='generate_pdfreport'),
    # path('crop_graph/', views.crop_graph, name='crop_graph'),
    # path('update_attendance/<int:meeting_id>/', views.update_attendance, name='update_attendance'),
    path('adaddattendance', views.adaddattendance, name='adaddattendance'),
    path('adattendance/', views.adattendance, name='adattendance'),
    path('submit_attendance/', views.submit_attendance, name='submit_attendance'),
    path('display_attendance/', views.display_attendance, name='display_attendance'),
    path('approve_attcertification/<int:attendance_id>/', views.approve_attcertification, name='approve_attcertification'),
    path('reject_attcertification/<int:attendance_id>/', views.reject_attcertification, name='reject_attcertification'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    # path('store_attendance/', views.store_attendance, name='store_attendance'),



    path('reduce_crop_count/<int:crop_id>/', views.reduce_crop_count, name='reduce_crop_count'),

    path('mindex',views.mindex,name="mindex"),
    path('mblog',views.mblog,name="mblog"),
    path('mappointment',views.mappointment,name="mappointment"),
    path('mcrop',views.mcrop,name="mcrop"),
    path('mcalendar',views.mcalendar,name="mcalendar"),
    path('mlogin',views.mlogin,name="mlogin"),
    path('meditprofile',views.meditprofile,name='meditprofile'),
    path('mfregistered',views.mfregistered,name='mfregistered'),
    path("mapprove", views.mapprove, name="mapprove"),
    path('mmeeting', views.mmeeting, name='mmeeting'),





    path('approve_certification/<int:certification_id>/', views.approve_certification, name='approve_certification'),
    path('reject_certification/<int:certification_id>/', views.reject_certification, name='reject_certification'),
    # path('pending_certification/<int:certification_id>/', views.pending_certification, name='pending_certification'),
    path('wait_certification/<int:application_id>/', views.wait_certification, name='wait_certification'),
    path('approve_acertification/<int:certification_id>/', views.approve_acertification, name='approve_acertification'),
    # path('reject_acertification/<int:certification_id>/', views.reject_acertification, name='reject_acertification'),
    path('set_status_waiting/<int:application_id>/', views.set_status_waiting, name='set_status_waiting'),
   
    # path('waiting_acertification/<int:certification_id>/', views.waiting_acertification, name='waiting_acertification'),
    path('mpending', views.mpending, name='mpending'),
    # path('membereditprofile', views.membereditprofile, name='membereditprofile'),


    path('loggout',loggout,name='loggout'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),




    path('edit_attendance/<int:meeting_id>/', views.edit_attendance, name='edit_attendance'),
    path('addriver', views.addriver, name='addriver'),
    path('adadddriver', views.adadddriver, name='adadddriver'),






    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
