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
from ceapp.views import index,loginn,loggout,register,about,service,product,contact,adindex,admember,adaddmember,adappointment,adcrop,adinbox,admailview,adcompose,adaddappointment,adaddcrop,adblog,adaddproduct,adeditblog,adblogdetails,adcalendar,adeditprofile,adapproval,mindex,mblog,mcalendar,mcrop,mappointment,mlogin
from django.conf import settings
from django.conf.urls.static import static
from ceapp.views import ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


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
    path('adaddproduct',adaddproduct,name='adaddproduct'),
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
    path('adaddattendance/<int:meeting_id>/', views.adaddattendance, name='adaddattendance'),
    path('adattendance/', views.adattendance, name='adattendance'),
    path('submit_attendance/', views.submit_attendance, name='submit_attendance'),
    path('display_attendance/', views.display_attendance, name='display_attendance'),
    path('approve_attcertification/<int:attendance_id>/', views.approve_attcertification, name='approve_attcertification'),
    path('reject_attcertification/<int:attendance_id>/', views.reject_attcertification, name='reject_attcertification'),
    path('mark_attendance/<int:meeting_id>/', views.mark_attendance, name='mark_attendance'),
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
   
    path('adproduct', views.adproduct, name='adproduct'),
    path('sellcrop', views.sellcrop, name='sellcrop'),
    # path('addriver', views.addriver, name='addriver'),
    # path('adadddriver', views.adadddriver, name='adadddriver'),
    path('edit_product/<product_id>', views.edit_product, name='edit_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
    path('adservice', views.adservice, name='adservice'),
    path('adaddservice', views.adaddservice, name='adaddservice'),
    path('edit_service/<service_id>', views.edit_service, name='edit_service'),
    path('delete_service/<service_id>', views.delete_service, name='delete_service'),
    path('dindex', views.dindex, name='dindex'),
    path('deditprofile',views.deditprofile,name='deditprofile'),
    path('dcalender',views.dcalender,name='dcalender'),
    path('dapplied',views.dapplied,name='dapplied'),
    path('msell',views.msell,name='msell'),
    path('accept_certification/<int:certification_id>/', views.accept_certification, name='accept_certification'),
    path('remove_certification/<int:certification_id>/', views.remove_certification, name='remove_certification'),
    path('msellapprove',views.msellapprove,name='msellapprove'),
    path('remove_scertification/<int:certification_id>/', views.remove_scertification, name='remove_scertification'),
    path('dleave',views.dleave,name='dleave'),
    path('edit_driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('driverapply',views.driverapply,name='driverapply'),
    path('apply_certification/<int:certification_id>/', views.apply_certification, name='apply_certification'),
    path('mdriverapplied',views.mdriverapplied,name='mdriverapplied'),
    path('confirmation/<int:apply_id>/', views.confirmation, name='confirmation'),
    # path('dispro', views.dispro, name='dispro'),
    path('search_driver', views.search_driver, name='search_driver'),
    path('adproductcost', views.adproductcost, name='adproductcost'),
    path('adaddproductcost', views.adaddproductcost, name='adaddproductcost'),
    path('edit_product_cost/<product_cost_id>', views.edit_product_cost, name='edit_product_cost'),
    path('delete_product_cost/<product_cost_id>', views.delete_product_cost, name='delete_product_cost'),
    path('pricelist1', views.pricelist1, name='pricelist1'),
    path('pricelist2', views.pricelist2, name='pricelist2'),
    path('accounts/', include('allauth.urls')),
    path('sellcrop2', views.sellcrop2, name='sellcrop2'),
    path('dconfirmed', views.dconfirmed, name='dconfirmed'),
    # path('mconfirmed', views.mconfirmed, name='mconfirmed'),
    path('selldetails', views.selldetails, name='selldetails'),
    path('adselldetails',views.adselldetails,name='adselldetails'),
    path('update_total_cost/<int:entry_id>/', views.update_total_cost, name='update_total_cost'),
    path('generate_pdf_bill/<int:sell_id>/', views.generate_pdf_bill, name='generate_pdf_bill'),
    path('collected/<int:collection_id>/', views.collected, name='collected'),
    # path('adaccount', views.adaccount, name='adaccount'),
    path('account', views.account, name='account'),
    # path('update_payment_status/<int:entry_id>/', views.update_payment_status, name='update_payment_status'),
    path('pay_entry/<int:entry_id>/', views.pay_entry, name='pay_entry'),
    path('adgenerate_pdf_bill/<int:sell_id>/', views.adgenerate_pdf_bill, name='adgenerate_pdf_bill'),
    path('all_accounts', views.all_accounts, name='all_accounts'),
    path('driver', views.driver, name='driver'),
    path('adddriver', views.adddriver, name='adddriver'),
    path('mleave', views.mleave, name='mleave'),
    path('apply_leave/<int:absent_member_id>/', views.apply_leave, name='apply_leave'),
    path('process_leave_application/', views.process_leave_application, name='process_leave_application'),
    path('admleaveapply', views.admleaveapply, name='admleaveapply'),
    path('grant_certification/<int:absent_member_id>/', views.grant_certification, name='grant_certification'),
    path('adaddmachinery', views.adaddmachinery, name='adaddmachinery'),
    path('admachinery', views.admachinery, name='admachinery'),
    path('edit_machinery/<int:machineries_id>/', views.edit_machinery, name='edit_machinery'),
    path('delete_machinery/<machineries_id>', views.delete_machinery, name='delete_machinery'),
    path('machinery', views.machinery, name='machinery'),
    # path('submit_machinery_date', views.submit_machinery_date, name='submit_machinery_date'),
    path('mapply/<int:machinery_id>/', views.mapply, name='mapply'),
    path('mmachinery', views.mmachinery, name='mmachinery'),
    path('mapplications', views.mapplications, name='mapplications'),
    path('applied_machineries', views.applied_machineries, name='applied_machineries'),

    # path('success_page', views.success_page, name='success_page'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('notifications', views.notifications, name='notifications'),
    path('mark_notification_as_read', views.mark_notification_as_read, name='mark_notification_as_read'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
