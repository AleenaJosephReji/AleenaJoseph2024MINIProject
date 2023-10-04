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


    path('delete_crop/<int:crop_id>/', views.delete_crop, name='delete_crop'),
    path('edit_crop/<int:crop_id>/', views.edit_crop, name='edit_crop'),

    path('search_crop', views.search_crop, name='search_crop'),
    # path('reduce_crop_count/<int:crop_id>/', views.reduce_crop_count, name='reduce_crop_count'),
    # path('reduce_crop_count/<int:crop_id>/', views.reduce_crop_count, name='reduce_crop_count'),
    path('combined_details/', views.combined_details, name='combined_details'),

    path('reduce_crop_count/', views.reduce_crop_count, name='reduce_crop_count'),

    path('mindex',views.mindex,name="mindex"),
    path('mblog',views.mblog,name="mblog"),
    path('mappointment',views.mappointment,name="mappointment"),
    path('mcrop',views.mcrop,name="mcrop"),
    path('mcalendar',views.mcalendar,name="mcalendar"),
    path('mlogin',views.mlogin,name="mlogin"),
    path('meditprofile',views.meditprofile,name='meditprofile'),
    path('mfregistered',views.mfregistered,name='mfregistered'),
    path("mapprove", views.mapprove, name="mapprove"),
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

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
