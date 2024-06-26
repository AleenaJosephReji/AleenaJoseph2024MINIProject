from django.shortcuts import render,redirect, get_list_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from .models import Member
from .models import Crop
from .models import Product
from .models import ApplyCrop
from .models import CustomUser
from .models import FarmerProfile,Sellapply,Notification,Mleave
from .models import Driver
from .models import SecretaryProfile
from .models import *
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.utils import timezone


# Create your views here.

def loginn(request):
    # if request.user.is_authenticated:
    #     # User is authenticated, redirect to another page
    #     return render(request, 'appointment.html')


    if request.method == "POST":
        # username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']
        print(email)
        print(password)
        user = authenticate(email=email,password=password)
        print(user)
        if user is not None:
            
            if user.role == CustomUser.MEMBER:
               login(request, user) 
               return redirect('mindex')
            elif user.role == CustomUser.FARMER:
                login(request, user)
                return redirect('homepage')
            elif user.role == CustomUser.ADMIN:
                login(request, user)
                return redirect('adindex')
            elif user.role == CustomUser.DRIVER:
                login(request,user)
                return redirect('dindex')
            else:
                messages.info(request, "Invalid Role for Login")
        else:
            messages.info(request, "Invalid Login")
        return redirect('loginn')
    else:
        return render(request, 'loginn.html')



# def loginn(request):
#     if request.method == "POST":
#         username=request.POST['email']
#         password=request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('homepage')
#         else:
#             messages.info(request, "Invalid login")
#         return redirect('loginn')
#     else:
#         return render(request, 'loginn.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        # email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        role = CustomUser.FARMER

        if password == confirm_password:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
                # return render(request, 'signup.html', {'username_exists': True})
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'Email already exists') 
            #     return redirect('register')
            else:
                user = CustomUser.objects.create_user(email=email, password=password,name=name, role=role)
                profile=FarmerProfile(user = user ,email = email)
                profile.save()
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('register')
    else:
     return render(request, 'signup.html')
    
# def index(request):
#     return render(request,'index.html')
def about(request):
    return render(request,'about.html')
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
def applyerror(request):
    message = "This crop is unavailable."
    return render(request,'applyerror.html', { 'message': message})
def blog(request):
    return render(request,'blog.html')
def detail(request):
    return render(request,'detail.html')
def feature(request):
    return render(request,'feature.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def apply(request):
    return render(request,'apply.html')
@never_cache
@login_required
def adindex(request):
    me = Member.objects.all()
    me_count = me.count()
    c=Crop.objects.all()
    c_count=c.count()
    crops = Crop.objects.all()
    approval = ApplyCrop.objects.all()
    approval_count = approval.count()
    # message = "A user has reviewed your store"
    #     Notification.objects.create(
    #         user=seller.user, title="Review Added", message=message, is_read=False
    #     )
    context = {'me': me, 'me_count': me_count,'c':c, 'c_count':c_count,'crops': crops ,'approval':approval,'approval_count':approval_count}
    return render(request, 'admintemp/adindex.html', context)

# def amembers(request):
#     return render(request,'Atemp/amembers.html')
def alogin(request):
    return render(request,'Atemp/alogin.html')
def aprofile(request):
    return render(request,'Atemp/aprofile.html')
def aeditprofile(request):
    return render(request,'Atemp/aeditprofile.html')
def asettings(request):
    return render(request,'Atemp/asettings.html')
def afarmers(request):
    return render(request,'Atemp/afarmers.html')
# def aaddmember(request):
#     return render(request,'Atemp/aaddmember.html')
def aeditmember(request):
    return render(request,'Atemp/aeditmember.html')
def adappointment(request):
    return render(request,'admintemp/adappointment.html')
def adaddappointment(request):
    return render(request,'admintemp/adaddappointment.html')
# def adcrop(request):
#     return render(request,'admintemp/adcrop.html')
# def adaddcrop(request):
#     return render(request,'admintemp/adaddcrop.html')
def adcompose(request):
    return render(request,'admintemp/adcompose.html')
def adinbox(request):
    return render(request,'admintemp/adinbox.html')
def admailview(request):
    return render(request,'admintemp/admailview.html')
# def adblog(request):
#     return render(request,'admintemp/adblog.html')
# def adaddblog(request):
#     return render(request,'admintemp/adaddblog.html')
def adeditblog(request):
    return render(request,'admintemp/adeditblog.html')
def adblogdetails(request):
    return render(request,'admintemp/adblogdetails.html')
@never_cache
@login_required
def adcalendar(request):
    return render(request,'admintemp/adcalendar.html')
def adeditprofile(request):
    return render(request,'admintemp/adeditprofile.html')
# def adapproval(request):
#     return render(request,'admintemp/adapproval.html')
def adminlogin(request):
    return render(request,'admintemp/adminlogin.html')
# def adeditmember(request):
#     return render(request,'admintemp/adeditmember.html')
def adsettings(request):
    return render(request,'admintemp/adsettings.html')
def adapprovalpending(request):
    return render(request,'admintemp/adapprovalpending.html')
def application(request):
    return render(request,'application.html')
@never_cache
@login_required
def mindex(request):
    user = request.user
    profile = Member.objects.get(user=user)
    print(profile.wardno)
    fe=ApplyCrop.objects.filter(wardNo=profile.wardno)
    fe_count=fe.count()
    approve = ApplyCrop.objects.filter(is_approved='approved', wardNo=profile.wardno)
    approve_count = approve.count()
    pendings = ApplyCrop.objects.filter(is_approved='waiting', wardNo=profile.wardno)
    pendings_count = pendings.count()
    context={'fe':fe,'fe_count':fe_count ,'approve':approve ,'approve_count': approve_count, 'pendings':pendings ,'pendings_count':pendings_count}

    return render(request,'membertemp/mindex.html',context)
def mblog(request):
    return render(request,'membertemp/mblog.html')
def mappointment(request):
    return render(request,'membertemp/mappointment.html')
@never_cache
@login_required
def mcalendar(request):
    return render(request,'membertemp/mcalendar.html')

def mlogin(request):
    # if request.method == "POST":
    #     username=request.POST['email']
    #     password=request.POST['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('membertemp/mindex')
    #     else:
    #         messages.info(request, "Invalid login")
    #     return redirect('mlogin')
    # else:
        return render(request, 'membertemp/mlogin.html')


def adblog(request):
    products = Product.objects.all()

    # blogs = Blog.objects.all()
    # context={
    #     'blogs' : blogs,
    # }
    return render(request, 'admintemp/adblog.html',{'products': products})
# views.py


 # Import a form for editing member details if you have one


from django.shortcuts import render, redirect
from .models import Crop  
@never_cache
@login_required
def admember(request):
    members = Member.objects.filter(is_active=True)
    return render(request, 'admintemp/admember.html', {'members': members})
@never_cache
@login_required
def adaddmember(request):
    # user=None
    # profile1 = MemberProfile(user=user)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # date_of_birth = request.POST.get('date_of_birth')
        # gender = request.POST.get('gender')
        address = request.POST.get('address')
        dis = request.POST.get('dis', 'Default District')  # Set a default value for District
        taluk = request.POST.get('taluk', 'Default Taluk')   # Set a default value for Taluk
        panchayat = request.POST.get('panchayat', 'Default Panchayat')  # Set a default value for Panchayat
        wardno = request.POST.get('wardno')
        wardname = request.POST.get('wardname')
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        profile_photo = request.FILES.get('profile_photo')
        
        role=CustomUser.MEMBER
        print(role)

        if CustomUser.objects.filter(email=email,role=CustomUser.MEMBER).exists():
                messages.info(request, 'Email already exists') 
                return redirect('adaddmember')
        else:
                user = CustomUser.objects.create_user(email=email, password=password ,name=name)
                user.role = CustomUser.MEMBER
                user.save()
                mem = Member(user=user,Name=name,email=email,address=address,district=dis,taluk=taluk,Panchayat=panchayat,wardname=wardname,wardno=wardno,postal=pin,phone=phone,bio=bio,profile_photo=profile_photo)
                mem.save()
                return redirect('admember')
    else:
         
        return render(request, 'admintemp/adaddmember.html')


def loggout(request):
    print('Logged Out')
    logout(request)
    return redirect('/')



# editmember
from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
@never_cache
@login_required
def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        # gender = request.POST.get('gender')
        address = request.POST.get('address')
        district = request.POST.get('district')
        taluk = request.POST.get('taluk')
        panchayat = request.POST.get('panchayat')
        ward = request.POST.get('ward')
        postal = request.POST.get('postal')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        profile_photo = request.FILES.get('profile_photo')


        # Update the member's attributes with the new data
        member.Name = name
        member.email = email
        member.date_of_birth = dob
        # member.gender = gender
        member.address = address
        member.district = district
        member.taluk = taluk
        member.Panchayat = panchayat
        member.wardno = ward
        member.postal = postal
        member.phone = phone
        member.bio = bio
        member.profile_photo = profile_photo
        # Save the updated member object
        member.save()

        # Redirect to the member list page after editing
        return redirect('admember')

    return render(request, 'admintemp/edit_member.html', {'member': member})


# from django.shortcuts import render, get_object_or_404, redirect
from .models import Member

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        # Delete the member object
        member.is_active = False
        member.save()
        request.session['delete mem'] = True
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('admember')

    return render(request, 'admintemp/delete_member.html', {'member': member})




# def cprofile(request):
#     return render(request, 'cprofile.html')
@never_cache
@login_required
def fmyprofile(request):
    profile = FarmerProfile.objects.get(user=request.user)
    context = {'profile': profile}
    
    return render(request, 'fmyprofile.html', context)
@never_cache
@login_required
def ceditprofile(request):
    
    user = request.user
    profile = FarmerProfile.objects.get(user=user)
    
    if request.method == "POST":
        print ('POST')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        # Process the form data and save/update the profile

        profile.first_name = request.POST.get('first_name')
        print("first name :",profile.first_name)
        
        
       
        
        profile.last_name = request.POST.get('last_name')
        print("last name :",profile.last_name)
        
        # profile.birth_date = request.POST.get('birth_date')
        # print("Date of Birth :",profile.birth_date)
     
        profile.email = request.POST.get('email')
        print("email name :",profile.email)

        
        profile.gender = request.POST.get('gender')
        print("gender :",profile.gender)

        profile.annual_income = request.POST.get('annual_income')
        print("annual income  :",profile.annual_income)
        profile.land = request.POST.get('land')
        print("land :",profile.land)

        # profile.house_name = request.POST.get('house_name')
        # print("house name :",profile.house_name)

        profile.house_no = request.POST.get('house_no')
        print("house no :",profile.house_no)

        profile.address = request.POST.get('address')
        print("adsress :",profile.address)

        profile.ward = request.POST.get('ward')
        print("ward :",profile.ward)

        profile.pin_code = request.POST.get('pin_code')
        print("pin code :",profile.pin_code)

        profile.phone_number = request.POST.get('phone_number')
        print("phone :",profile.phone_number)

        # profile.phone_number = request.POST.get('phone_number')
        profile.fprofile_photo = request.FILES.get('fprofile_photo')
        print("phone :",profile.fprofile_photo)

        profile.save()
        
            

        # messages.success(request, 'Profile updated successfully.')
        return redirect('ceditprofile')  # Redirect to the profile page
    context = {
        'user': user,
        'profile': profile
    }

    return render(request, 'ceditprofile.html',context)

from django.contrib.auth import update_session_auth_hash
# @login_required(login_url='login_page')
@never_cache
@login_required
def meditprofile(request):
    
    # user = request.user
    # profile = PatientProfile.objects.get(user=user)
    user = request.user
    mem = get_object_or_404(Member, user=user)
    
    if request.method == "POST":
        print ('POST')
        # user.first_name=request.POST.get('first_name')
        # user.last_name=request.POST.get('last_name')
        # Process the form data and save/update the profile
        mem.Name = request.POST.get('name')
        mem.email = request.POST.get('email')
        # mem.gender = request.POST.get('gender')
        # mem.date_of_birth = request.POST.get('dob')
        # mem.date_of_join = request.POST.get('doj')        
        mem.address = request.POST.get('address')
        mem.district = request.POST.get('dis')
        mem.wardno = request.POST.get('ward')
        mem.postal = request.POST.get('pin')
        mem.phone = request.POST.get('phone')
        mem.Panchayat = request.POST.get('panchayat')
        mem.phone = request.POST.get('phone')
        profile_photo = request.FILES.get('profile_photo')
        mem.profile_photo = profile_photo
        
        mem.amob = request.POST.get('amob')
        mem.aemail = request.POST.get('aemail')
        mem.dob = request.POST.get('dob')
        mem.degree = request.POST.get('degree')
        mem.institution = request.POST.get('institution')
        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')


        if old_password and reset_password and request.POST.get('cpass') == reset_password:
            if user.check_password(old_password):
                # The old password is correct, set the new password
                user.set_password(reset_password)
                user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
            else:
                messages.error(request, "Incorrect old password. Password not updated.")
        else:
            print("Please fill all three password fields correctly.")
        
        mem.reset_password = reset_password
        mem.save()
        return redirect('meditprofile') 
    context = {
        'user': user,
        'mem': mem
    }

    return render(request, 'membertemp/meditprofle.html',context)

# @login_required(login_url='login_page')
# def pro_ashaworker(request):
#     asha = Ashaworker.objects.filter(user=request.user).first() 
#     return render(request, 'asha_temp/pro_ashaworker.html', {'asha': [asha]})



@never_cache
@login_required   
def meditprofile(request):
   
    user = request.user
    # profile1 = FarmerProfile.objects.get(user=user)
    member, created = Member.objects.get_or_create(user=user)
    
    if request.method == "POST":
        print ('POST')
        user.name=request.POST.get('name')
        # user.last_name=request.POST.get('last_name')
        # Process the form data and save/update the profile

        member.name = request.POST.get('name')
        print("name :",member.name)
        # profile1.last_name = request.POST.get('last_name')
        # print("last name :",profile1.last_name)
        member.email = request.POST.get('email')
        print("email name :",member.email)
        member.gender = request.POST.get('gender')
        print("gender :",member.gender)
        # profile1.annual_income = request.POST.get('annual_income')
        # print("annual income  :",profile1.annual_income)
        # profile1.land = request.POST.get('land')
        # print("land :",profile1.land)
        # profile.house_name = request.POST.get('house_name')
        # print("house name :",profile.house_name)
        # profile1.house_no = request.POST.get('house_no')
        # print("house no :",profile1.house_no)
        member.address = request.POST.get('address')
        print("adsress :",member.address)
        member.ward = request.POST.get('ward')
        print("ward :",member.ward)
        member.postal = request.POST.get('postal')
        print("pin code :",member.postal)
        member.phone = request.POST.get('phone')
        print("phone :",member.phone)


        member.dob = request.POST.get('dob')
        print("Date of Birth :",member.dob)
        member.amob = request.POST.get('amob')
        print("amob :",member.amob)
        member.aemail = request.POST.get('aemail')
        print("aemail :",member.aemail)
        member.degree = request.POST.get('degree')
        print("degree :",member.degree)
        member.institution = request.POST.get('institution')
        print("institution :",member.institution)
        # profile.phone_number = request.POST.get('phone_number')
        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')


        if old_password and reset_password and request.POST.get('cpass') == reset_password:
            if user.check_password(old_password):
                # The old password is correct, set the new password
                user.set_password(reset_password)
                user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
            else:
                messages.error(request, "Incorrect old password. Password not updated.")
        else:
            print("Please fill all three password fields correctly.")
        
        member.reset_password = reset_password
        member.save()
        return redirect('meditprofile') 
    context = {
        'user': user,
        'member': member
    }

    return render(request, 'membertemp/meditprofile.html',context)

from django.shortcuts import render, redirect
from .models import Crop 

@never_cache
@login_required
def adcrop(request):
    crops = Crop.objects.all()
    return render(request, 'admintemp/adcrop.html', {'crops': crops})

from django.db.models import Max
@never_cache
@login_required
def adaddcrop(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cdescription = request.POST.get('cdescription')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        count = request.POST.get('count')
        crop_photo = request.FILES.get('crop_photo')

        existing_crop = Crop.objects.filter(Namec=cname).first()
        if existing_crop:
            messages.error(request, f'A crop with the name "{cname}" already exists.')
            return redirect('adaddcrop')

        new_crop = Crop(Namec=cname, des=cdescription, start_date=start_date, end_date=end_date, count=count,
                        crop_photo=crop_photo, current=True)
        new_crop.save()

        # Set current to False for all other crops
        Crop.objects.exclude(id=new_crop.id).update(current=False)

        if request.user.is_authenticated:
            # Create a notification for the authenticated user
            message = f'A new crop "{cname}" has been added.'
            Notification.objects.create(user=request.user, title="New Crop Added", message=message, is_read=False)

        return redirect('adcrop')

    return render(request, 'admintemp/adaddcrop.html')



# from .models import Crop, Notification

# def adaddcrop(request):
#     if request.method == 'POST':
#         cname = request.POST.get('cname')
#         cdescription = request.POST.get('cdescription')
#         avail = request.POST.get('available') == 'on'
#         notavail = request.POST.get('notavailable') == 'on'

#         crop = Crop(Namec=cname, des=cdescription, available=avail, not_available=notavail)
#         crop.save()

#         # Notify farmers about the new crop
#         if avail:
#             farmers = User.objects.filter(userprofile__is_admin=False)
#             for farmer in farmers:
#                 Notification.objects.create(user=farmer, crop=crop)

#         return redirect('adcrop')  # Redirect to a success page or URL

#     return render(request, 'admintemp/adaddcrop.html')

def delete_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)

    if request.method == 'POST':
        # Delete the member object
        crop.delete()
        
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('adcrop')

    return render(request, 'admintemp/delete_crop.html', {'crop': crop})
@never_cache
@login_required
def edit_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)

    if request.method == 'POST':
        cname = request.POST.get('cname')
        details = request.POST.get('details')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        count = request.POST.get('count')
        crop_photo = request.FILES.get('crop_photo')

        # Check the value of 'availability' to determine the selected option
        # availability = request.POST.get('availability')
        # if availability == '1':
        #     avail = True
        #     notavail = False
        # else:
        #     avail = False
        #     notavail = True

        # Update the member's attributes with the new data
        crop.Namec = cname
        crop.des = details
        crop.start_date = start_date
        crop.end_date = end_date
        crop.count = count
        crop.crop_photo = crop_photo
        # Save the updated member object
        crop.save()

        # Redirect to the member list page after editing
        return redirect('adcrop')

    return render(request, 'admintemp/edit_crop.html', {'crop': crop})
@never_cache
@login_required
def mcrop(request):
    crops = Crop.objects.all()  # Retrieve all crops from the database
    return render(request, 'membertemp/mcrop.html', {'crops': crops})



# def crop(request):
#     user = request.user
#     profile = FarmerProfile.objects.get(user=user)
#     today = date.today()
#     # Retrieve the currently added crop
#     # current_crop = Crop.objects.filter(current=True).first()
#     crops = Crop.objects.all() 
#     # for crop in crops:
#     #     print(f"Today: {today}, Start Date: {crop.start_date}, End Date: {crop.end_date}")
#     return render(request, 'crop.html', {'crops': crops , 'today': today ,'profile' : profile})
@never_cache
@login_required
def crop(request):
    user = request.user
    profile = FarmerProfile.objects.get(user=user)
    today = date.today()
    crops = Crop.objects.all()
    
    existing_certifications = ApplyCrop.objects.filter(user=user)
    
    return render(request, 'crop.html', {
        'crops': crops,
        'today': today,
        'profile': profile,
        'existing_certifications': existing_certifications
    })
# def crop(request):
#     crops = Crop.objects.all()  # Retrieve all crops from the database
#     return render(request, 'crop.html', {'crops': crops})

def disapply(request):
    applys = ApplyCrop.objects.all()
    return render(request, 'disapply.html', {'applys': applys})

from django.contrib.auth.decorators import login_required
@never_cache
@login_required
def apply(request,crop_id):
    existing_certification = ApplyCrop.objects.filter(user=request.user,crop_id=crop_id).first()
    print(existing_certification)
    if existing_certification:
        return render(request, 'apply.html', {'existing_certification': existing_certification})
    
    crop_name = request.GET.get('crop_name')

    farmer_profile = FarmerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        
    #    cname = request.POST.get('cname')
        farmerName = request.POST.get('farmerName')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        wardNo  = request.POST.get('wardno')
        annualIncome  = request.POST.get('annualIncome')
        land = request.POST.get('land')
        file_upload = request.FILES.get('file_upload')
        
        crop=Crop.objects.filter(id=crop_id)
        obj = ApplyCrop()
        obj.user = request.user
        obj.cname = crop_name
        obj.farmerName = farmerName
        obj.address = address
        obj.contactNo= phone_number
        obj.wardNo = wardNo
        obj.crop_id=crop[0]
        obj.land = land
        obj.AnnualIncome = annualIncome
        obj .file_upload = file_upload
        obj.save()

        
        return redirect('apply',crop_id=crop_id)

    return render(request, 'apply.html', {
    'crop_name': crop_name,
    'existing_certification': existing_certification,'farmer_name': farmer_profile.first_name,'farmer_lname': farmer_profile.last_name, # Add these fields to the context
        'farmer_address': farmer_profile.address,
        'farmer_phone_number': farmer_profile.phone_number,
        'farmer_ward': farmer_profile.ward, 
        'farmer_annual_income': farmer_profile.annual_income,
        'farmer_land' : farmer_profile.land,
        'farmer_file_upload' : farmer_profile.file_upload
     
    })
@never_cache
@login_required
def applied_crops(request):
    user = request.user
    today = date.today()
    
    # Filter applied crops for the current user
    applied_crops_ids = ApplyCrop.objects.filter(user=user).values_list('crop_id', flat=True)
    applied_crops = Crop.objects.filter(id__in=applied_crops_ids)
    
    existing_certifications = ApplyCrop.objects.filter(user=user)
    
    return render(request, 'applied_crops.html', {
        'applied_crops': applied_crops,
        'today': today,
        'existing_certifications': existing_certifications
    })
# @login_required
# def apply(request):
#     existing_certification = ApplyCrop.objects.filter(user=request.user).first()
#     if existing_certification:
#         return render(request, 'apply.html', {'existing_certification': existing_certification})
    
#     crop_name = request.GET.get('crop_name')

#     farmer_profile = FarmerProfile.objects.get(user=request.user)
#     if request.method == 'POST':
        
#     #    cname = request.POST.get('cname')
#         farmerName = request.POST.get('farmerName')
#         address = request.POST.get('address')
#         contactNo = request.POST.get('contactNo')
#         wardNo  = request.POST.get('wardNo')
#         annualIncome  = request.POST.get('annualIncome')

        

#         obj = ApplyCrop()
#         obj.user = request.user
#         obj.cname = crop_name
#         obj.farmerName = farmerName
#         obj.address = address
#         obj.contactNo= contactNo
#         obj.wardNo = wardNo
#         obj.AnnualIncome = annualIncome
#         obj.save()

        
#         return redirect('apply')

#     return render(request, 'apply.html', {
#     'crop_name': crop_name,
#     'existing_certification': existing_certification,'farmer_name': farmer_profile.first_name,  # Add these fields to the context
#         'farmer_address': farmer_profile.address,
#         'farmer_contact': farmer_profile.phone_number,
#         # 'farmer_phone_number': farmer_profile.contactNo,
#         'farmer_ward': farmer_profile.ward,
#         'farmer_annual_income': farmer_profile.annual_income,
     
#     })
# def disapply(request):
#     # Retrieve details from the database
#     details = ApplyCrop.objects.all()  # You might need to filter this based on your requirements

#     # Pass the details to the template
#     return render(request, 'crop.html', {'details': details})


# views.py
from django.shortcuts import render
from .models import ApplyCrop  # Import your model
@never_cache
@login_required
def mfregistered(request):
    user = request.user
    profile = Member.objects.get(user=user)
    print(profile.wardno)
    pending_details = ApplyCrop.objects.filter(wardNo=profile.wardno)
    user_roles = {}
    for application in pending_details:
        # Ensure the user associated with the Certification exists
        user = get_object_or_404(CustomUser, id=application.user_id)

        # Retrieve user roles
        user_roles[application.id] = {
            'is_member': user.role == CustomUser.MEMBER,
            'is_farmer': user.role == CustomUser.FARMER,
            # 'is_seller': user.is_staff
        }

    context = {
        'pending_details': pending_details,
        'user_roles': user_roles,  # Include user roles in the context
    }
    return render(request, 'membertemp/mfregistered.html', context)

def approve_certification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = ApplyCrop.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('mfregistered')

def reject_certification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = ApplyCrop.REJECTED  # Set it to 'rejected'
        certification.save()
    return redirect('mfregistered')

def set_status_waiting(request, application_id):
    # Handle the logic to set the status to 'waiting'
    certification = get_object_or_404(ApplyCrop, id=application_id)
    if request.method == 'POST':
        certification.is_approved = ApplyCrop.WAITING  # Set it to 'approved'
        certification.save()
    return redirect('mfregistered')

# def waiting_list_certification(request, certification_id):
#     certification = get_object_or_404(ApplyCrop, id=certification_id)
    
#     if request.method == 'POST':
#         if certification.is_approved == ApplyCrop.PENDING and certification.AnnualIncome > 30000:
#             certification.is_approved = ApplyCrop.WAITING
#             certification.save()
    
#     return redirect('mfregistered')  # Replace 'mfregistered' with the appropriate URL name




# def approve_acertification(request, certification_id):
#     certification = get_object_or_404(ApplyCrop, id=certification_id)
#     if request.method == 'POST':
#         certification.is_approved = ApplyCrop.APPROVED  # Set it to 'approved'
#         certification.save()
    
#     # Get the pending details for adpendingapproval
#     pending_details = ApplyCrop.objects.filter(is_approved=ApplyCrop.PENDING)
    
#     return render(request, 'admintemp/adapproval.html', {'pending_details': pending_details})


def approve_acertification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approvedd = ApplyCrop.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('adpendingapproval')


# def approve_acertification(request, certification_id):
#     certification = get_object_or_404(ApplyCrop, id=certification_id)
#     if request.method == 'POST':
#         certification.is_approved = ApplyCrop.APPROVED  # Set it to 'approved'
#         certification.save()

#         # Store the approved details in a session variable
#         approved_details = {
#             'cname': certification.cname,
#             'farmerName': certification.farmerName,
#             'address': certification.address,
#             'contactNo': certification.contactNo,
#             'wardNo': certification.wardNo,
#             'AnnualIncome': certification.AnnualIncome,
#         }
#         request.session['approved_details'] = approved_details

#     return redirect('adpendingapproval')

def reject_acertification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approvedd = ApplyCrop.REJECTED  # Set it to 'rejected'
        certification.save()
    return redirect('adpendingapproval')

def wait_certification(request, application_id):
    # Handle the logic to set the status to 'waiting'
    certification = get_object_or_404(ApplyCrop, id=application_id)
    if request.method == 'POST':
        certification.is_approvedd = ApplyCrop.WAITING  # Set it to 'approved'
        certification.save()
    return redirect('adpendingapproval')
@never_cache
@login_required
def mapprove(request):
    user = request.user
    profile = Member.objects.get(user=user)
    pending_details = ApplyCrop.objects.filter(is_approved='approved',wardNo=profile.wardno)  # Adjust the filter condition as needed
    # Pass the data to the template
    context = {'pending_details': pending_details}
    return render(request, 'membertemp/mapprove.html', context)
    
# user.role == CustomUser.MEMBER:
# def mapprove(request):
#     pending_details = ApplyCrop.objects.filter(approved=False)
#     return render(request, 'membertemp/mapprove.html', {'details': pending_details})

from django.shortcuts import render, get_object_or_404, redirect
from .models import ApplyCrop, Crop
@never_cache
@login_required
def adpendingapproval(request):
    # Retrieve the approved details from your model or database

    approved_details= ApplyCrop.objects.filter(is_approved='approved',is_given='notgiven')
    # approved_details = ApplyCrop.objects.filter(is_approved='approved')

    if request.method == 'POST':
        # Handle the approve request
        certification_id = request.POST.get('certification_id')
        certification = get_object_or_404(ApplyCrop, id=certification_id)
        
        # Reduce the count of the associated Crop by 1
        if certification.crop:
            certification.crop.count -= 1
            certification.crop.save()
        
        certification.is_approvedd = ApplyCrop.WAITING  # Set it to 'waiting' or the appropriate status
        certification.save()

        # Now, update the approved details queryset to exclude the approved item
        approved_details = approved_details.exclude(id=certification_id)

    context = {
        'approved_details': approved_details,
    }
    return render(request, 'admintemp/adpendingapproval.html', context)



    # approved_details = ApplyCrop.objects.filter(is_approved='approved')
    # user_roles = {}
    # for application in approved_details:
    #     # Ensure the user associated with the Certification exists
    #     user = get_object_or_404(CustomUser, id=application.user_id)

    #     # Retrieve user roles
    #     user_roles[application.id] = {
    #         'is_member': user.role == CustomUser.MEMBER,
    #         'is_farmer': user.role == CustomUser.FARMER,
    #         # 'is_seller': user.is_staff
    #     }
    # # Pass the approved details to the template
    # context = { 'user_roles': user_roles,'approved_details': approved_details}
    # return render(request, 'admintemp/adpendingapproval.html', context)
    # pending_details = ApplyCrop.objects.filter(is_approved='approved')  # Adjust the filter condition as needed
    # user_roles = {}
    # for application in pending_details:
    #     # Ensure the user associated with the Certification exists
    #     user = get_object_or_404(CustomUser, id=application.user_id)

    #     # Retrieve user roles
    #     user_roles[application.id] = {
    #         'is_admin': user.is_superuser,
    #         # 'is_member': user.role == CustomUser.MEMBER,
    #         'is_farmer': user.role == CustomUser.FARMER,
    #         # 'is_seller': user.is_staff
    #     }

    # context = {
    #     'pending_details': pending_details,
    #     'user_roles': user_roles,  # Include user roles in the context
    # }
    # return render(request, 'admintemp/adpendingapproval.html', context)

@never_cache
@login_required
def adapproval(request):
    approved_details = ApplyCrop.objects.filter(is_approvedd='approved')
    # crops = Crop.objects.all()
    # existing_review = ApplyCrop.objects.filter(user=approved_details.user, crop=approved_details.crop_id).first()

    # if existing_review:
    #         # You can handle the case where the user has already reviewed this seller
    #         # For example, you can display an error message or redirect them to a different page.
    #         review_status = 'reviewed'
    # else:
    #         review_status = 'pending'

    # combined_data = zip(approved_details, crops)
    return render(request, 'admintemp/adapproval.html', {'approved_applications': approved_details})
    # combined_data = zip(approved_details, crops)
    # return render(request, 'admintemp/adapproval.html', {'approved_applications': approved_details ,'combined_data' : combined_data})
    # pending_details = ApplyCrop.objects.filter(is_approved='approved')  # Adjust the filter condition as needed
    # # Pass the data to the template
    # context = {'pending_details': pending_details}
    # return render(request, 'admintemp/adapproval.html', context)
    # Retrieve the approved details from the session variable
    # approved_details = request.session.get('approved_details', [])

    # # Pass the approved details to the template
    # return render(request, 'admintemp/adapproval.html', {'approved_details': approved_details})
    # details = ApplyCrop.objects.all()
    # return render(request, 'admintemp/adpendingapproval.html', {'details': details})



# def mfregistered(request):
#     details = ApplyCrop.objects.all()
#     return render(request,'membertemp/mfregistered.html',{details : details})


#hh
from django.shortcuts import render
from .models import Crop

def search_crop(request):
    cropname = request.GET.get('cropname', '')
    # crops = Crop.objects.filter(Namec__icontains=cropname)

    if cropname:
        crops = Crop.objects.filter(Namec__icontains=cropname)
    else:
        crops = Crop.objects.all()
    
    return render(request, 'admintemp/adcrop.html', {'crops': crops, 'cropname': cropname})

def search_member(request):
    membername = request.GET.get('membername', '')
    # crops = Crop.objects.filter(Namec__icontains=cropname)

    if membername:
        members = Member.objects.filter(Name__icontains=membername)
    else:
        members = Member.objects.all()
    
    return render(request, 'admintemp/admember.html', {'members': members, 'membername': membername})


from django.http import JsonResponse
@never_cache
@login_required
def mpending(request):
    user = request.user
    profile = Member.objects.get(user=user)
    pending_details = ApplyCrop.objects.filter(is_approved='waiting',wardNo=profile.wardno)  # Adjust the filter condition as needed
    # Pass the data to the template
    context = {'pending_details': pending_details}
    return render(request, 'membertemp/mpending.html', context)


# def adpendinglist(request):
#     # Retrieve the pending details from your model or database
#     pending_details = ApplyCrop.objects.filter(is_approved='waiting')
#     application_waiting = ApplyCrop.objects.filter(is_approvedd='waiting')

#     if request.method == 'POST':
#         # Handle the approve request
#         certification_id = request.POST.get('certification_id')
#         certification = get_object_or_404(ApplyCrop, id=certification_id)
#         certification.is_approvedd = ApplyCrop.APPROVED  # Set it to 'approved'
#         certification.save()

#         # Now, update the pending details queryset to exclude the approved item
#         pending_details = pending_details.exclude(id=certification_id)
#         application_waiting = application_waiting.exclude(id=certification_id)

#     context = {
#         'pending_details': pending_details,'application_waiting' : application_waiting,
#     }
#     return render(request, 'admintemp/adpendinglist.html', context)





@never_cache
@login_required
def adpendinglist(request):
    pending_details = ApplyCrop.objects.filter(is_approved='waiting')
    application_waiting = ApplyCrop.objects.filter(is_approvedd='waiting').first()
    details = list(pending_details)
    if application_waiting:
        details.append(application_waiting)
    if request.method == 'POST':
        certification_id = request.POST.get('certification_id')
        certification = get_object_or_404(ApplyCrop, id=certification_id)
        certification.is_approvedd = ApplyCrop.APPROVED  # Set it to 'approved'
        certification.save()
        details = [item for item in details if item.id != int(certification_id)]
    context = {
        'details': details,
    }
    return render(request, 'admintemp/adpendinglist.html', context)

# def adpendinglist(request):
#     # Retrieve the pending details from your model or database
#     pending_details = ApplyCrop.objects.filter(is_approved='waiting')
#     context = {
#         'pending_details': pending_details,
#     }
#     return render(request, 'admintemp/adpendinglist.html', context)
from django.db import transaction

# def reduce_crop_count(request, crop_id):
#     try:
#         crop = Crop.objects.get(id=crop_id)
#         # Reduce the crop count by 1 (or by your desired amount)
#         crop.count -= 1
#         crop.given = True  # Mark the crop as given
#         crop.save()
#     except Crop.DoesNotExist:
#         pass  # Handle the case where the crop doesn't exist

#     return redirect('adapproval')

from django.shortcuts import render, redirect
from .models import Crop, ApplyCrop

def reduce_crop_count(request, crop_id):
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        try:
            # Use filter instead of get to retrieve a queryset
            queryset = ApplyCrop.objects.filter(cname=crop_name)
            land_value = None

            if queryset.exists():
                # If there are multiple matching objects, choose one (you can specify the logic)
                # For example, you can choose the first one in the queryset
                land_value_str = queryset.first().land

                # Convert land_value to an integer
                land_value = int(land_value_str)

            reduction_amount = 0

            if land_value is not None:
                if land_value <= 50:
                    reduction_amount = 20
                elif 50 < land_value <= 100:
                    reduction_amount = 40
                elif 100 < land_value <= 150:
                    reduction_amount = 60

            if reduction_amount > 0:
                crop = Crop.objects.get(Namec=crop_name)
                applygive = ApplyCrop.objects.get(id=crop_id)

                if crop.count >= reduction_amount:
                    crop.count -= reduction_amount
                    applygive.is_given = ApplyCrop.GIVEN
                    applygive.crop_giventime = timezone.now()
                    crop.save()
                    applygive.save()

        except (Crop.DoesNotExist, ApplyCrop.DoesNotExist, ValueError):
            pass

    return redirect('adapproval')




def combined_details(request):
    approved_details = ApplyCrop.objects.filter(is_approvedd='approved')
    all_crops = Crop.objects.all()

    return render(request, 'admintemp/adapproval2.html', {
        'approved_applications': approved_details,
        'crops': all_crops,
    })
from django.shortcuts import render
from .models import ApplyCrop, Crop

# def adreport(request):
#     # Fetch approved details and all crops
#     approved_details = ApplyCrop.objects.filter(is_approvedd='approved')
#     crops = Crop.objects.all()

#     # Create a dictionary to store data by crop name
#     data_by_crop = {}

#     # Group approved details by crop name
#     for application in approved_details:
#         crop_name = application.cname
#         if crop_name not in data_by_crop:
#             data_by_crop[crop_name] = []

#         data_by_crop[crop_name].append(application)

#     return render(request, 'admintemp/adreport.html', {'data_by_crop': data_by_crop, 'crops': crops})



from django.shortcuts import render
from .models import ApplyCrop, Crop, Meeting
from django.shortcuts import render
from .models import ApplyCrop, Crop, Meeting
from datetime import date  # Import the date module
@never_cache
@login_required
def adreport(request):
    approved_details = ApplyCrop.objects.filter(is_approvedd='approved')
    crops = Crop.objects.all()
    current_date = date.today()
    meetings = Meeting.objects.filter(meeting_date__lt=current_date)
    data_by_crop = {}
    for application in approved_details:
        crop_name = application.cname
        if crop_name not in data_by_crop:
            data_by_crop[crop_name] = []
        data_by_crop[crop_name].append(application)
    return render(request, 'admintemp/adreport.html', {'data_by_crop': data_by_crop, 'crops': crops, 'meetings': meetings})


#meeting
from django.shortcuts import render, redirect
from .models import Meeting
from .models import Attendance
from django.contrib import messages  
from django.shortcuts import render
from django.utils import timezone

def approve_attcertification(request, attendance_id):
    if request.method == "POST":
        member_id = request.POST.get('member_id')
        attendance = WardAttendance.objects.get(member_id=member_id)
        if(attendance):
            attendance.is_present = WardAttendance.PRESENT
            attendance.save()
        else:
            attendance = WardAttendance(member_id=member_id,is_present=WardAttendance.PRESENT)
            attendance = WardAttendance.objects.get(id=attendance_id)
            attendance.save()
    # attendance.is_present = WardAttendance.PRESENT
    # attendance.save()
    return redirect('adaddattendance')

def reject_attcertification(request, attendance_id):
    attendance = WardAttendance.objects.get(id=attendance_id)
    attendance.is_present = WardAttendance.ABSENT
    attendance.save()
    return redirect('adaddattendance')
@never_cache
@login_required
def adattendance(request):
    if request.method == 'POST':
        selected_wards = request.POST.getlist('ward')
        meeting_id = request.POST.get('meeting_id')
        meeting_day = Meeting.objects.get(id=meeting_id)

        # Iterate through selected wards and update attendance records
        for ward in selected_wards:
            # Check if an attendance record for the person and meeting already exists
            attendance, created = WardAttendance.objects.get_or_create(
                meeting_id=meeting_id,
                person_id=ward,
                meeting_date=meeting_day.meeting_date
            )
            
            # Update the 'attended' field to True
            attendance.attended = True
            attendance.save()

        # Redirect to the attendance page or another appropriate URL
        return redirect('adattendance')  # Replace 'attendance-success' with the actual URL

    # If the request method is not POST, render the page with all meetings.
    meetings = Meeting.objects.all()
    return render(request, 'admintemp/adattendance.html', {'meetings': meetings})

@never_cache
@login_required
def adaddattendance(request, meeting_id):
    # Retrieve the meeting details based on meeting_id
    meeting = Meeting.objects.get(id=meeting_id)

    # Fetch members and attendance records
    members = Member.objects.filter(is_active=True)
    attendance_records = WardAttendance.objects.all()  # Retrieve attendance records

    # Prepare data for rendering in the template
    member_data = {}
    for member in members:
        attendance_record = attendance_records.filter(member=member, meeting=meeting).first()
        if attendance_record:
            member_data[member.id] = {
                'is_present': attendance_record.is_present,
                'Name': member.Name,
                # Add other fields as needed
            }
        else:
            member_data[member.id] = {
                'is_present': 'pending',
                'Name': member.Name,
                # Add other fields as needed
            }

    return render(request, 'admintemp/adaddattendance.html', {'members': member_data, 'meeting': meeting})

# def adaddattendance(request):
#     members = Member.objects.filter(is_active=True)
#     attendance_records = WardAttendance.objects.all()  
#     for application in attendance_records:
#         # Ensure the user associated with the Certification exists
#         user = get_object_or_404(CustomUser, id=application.user_id)
#     context = {
#         'pending_details': attendance_records,
#             # Include user roles in the context
#     }
# # Retrieve attendance records
#     return render(request, 'admintemp/adaddattendance.html', {'members': members, 'attendance_records': attendance_records,'context' : context})


def submit_attendance(request):
    if request.method == 'POST':
        for ward_attendance in WardAttendance.objects.all():
            attendance_value = request.POST.get(f'attendance_{ward_attendance.user.id}', 'off')
            ward_attendance.is_present = attendance_value == 'on'
            ward_attendance.save()
        messages.success(request, "Attendance marked")
    return redirect('adaddattendance')
from django.shortcuts import redirect

def mark_attendance(request, meeting_id):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        attendance_status = request.POST.get('attendance_status')

        print(f"Member ID: {member_id}, Attendance Status: {attendance_status}")

        # Get or create the WardAttendance record based on member_id and meeting_id
        obj, created = WardAttendance.objects.get_or_create(member_id=member_id, meeting_id=meeting_id, defaults={'is_present': attendance_status})
        
        # If the record already exists, update the is_present field
        if not created:
            obj.is_present = attendance_status
            obj.save()

    return redirect('adaddattendance', meeting_id)
from django.shortcuts import render
from .models import WardAttendance, Meeting
from django.shortcuts import render
from .models import Meeting, Member, WardAttendance
@never_cache
@login_required
def view_attendance(request, meeting_id):
    # Retrieve the meeting details based on meeting_id
    meeting = Meeting.objects.get(id=meeting_id)

    # Fetch members and attendance records
    members = Member.objects.filter(is_active=True)
    attendance_records = WardAttendance.objects.all()  # Retrieve attendance records

    # Prepare data for rendering in the template
    member_data = {}
    for member in members:
        attendance_record = attendance_records.filter(member=member, meeting=meeting).first()
        if attendance_record:
            member_data[member.id] = {
                'is_present': attendance_record.is_present,
                'Name': member.Name,
                # Add other fields as needed
            }
        else:
            member_data[member.id] = {
                'is_present': 'pending',
                'Name': member.Name,
                # Add other fields as needed
            }

    return render(request, 'admintemp/view_attendance.html', {'members': member_data, 'meeting': meeting})


def display_attendance(request):
    # Fetch all members
    members = CustomUser.objects.filter(role=CustomUser.MEMBER)

    # Create a dictionary to store attendance information for each member
    attendance_info = {}

    for member in members:
        # Check if there is a WardAttendance record for the member
        ward_attendance = WardAttendance.objects.filter(user=member).all()
        
        if ward_attendance:
            attendance_info[member.name] = ward_attendance.is_present
        else:
            attendance_info[member.name] = False

    return render(request, 'admintemp/attendance_display.html', {'members': members, 'attendance_info': attendance_info})

# def adattendence(request):
#     meetings = Meeting.objects.filter(is_active=True)
#     from django.utils import timezone
#     current_date = timezone.now().date()
#     return render(request, 'admintemp/adattendance.html', {'meetings': meetings, 'current_date': current_date})

from django.shortcuts import render, redirect
from .models import Meeting
# from .models import Attendee
@never_cache
@login_required
def admeeting(request):
    meetings = Meeting.objects.filter(is_active=True)
    from django.utils import timezone
    current_date = timezone.now().date()
    return render(request, 'admintemp/admeeting.html', {'meetings': meetings, 'current_date': current_date})

    # ward_members = Attendee.objects.all()
    # if request.method == 'POST':
    #     form = Attendee(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('adattendence')
    # else:
    #     form = Attendee()
    # return render(request, 'admintemp/adattendence.html', {'ward_members': ward_members, 'form': form})
# def update_attendance(request, meeting_id):
#     if request.method == "POST":
#         meeting = Meeting.objects.get(id=meeting_id)
#         for attendee in meeting.attendees.all():
#             annu_attendance = request.POST.get(f"annu_attendance_{meeting_id}_{attendee.id}")
#             anna_attendance = request.POST.get(f"anna_attendance_{meeting_id}_{attendee.id}")
#             arya_attendance = request.POST.get(f"arya_attendance_{meeting_id}_{attendee.id}")

#             # Update the attendee's attendance status
#             attendee.annu_attendance = annu_attendance == "on"
#             attendee.anna_attendance = anna_attendance == "on"
#             attendee.arya_attendance = arya_attendance == "on"

#             # Save the changes to the database
#             attendee.save()

#     return redirect("admeeting")
@never_cache
@login_required
def adaddmeeting(request):
    if request.method == 'POST':
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        # desmeeting = request.POST.get('desmeeting')
        meeting_venue = request.POST.get('meeting_venue')
        meeting_mode = request.POST.get('meeting_mode')
        meeting_agenda = request.POST.get('meeting_agenda')
        meeting = Meeting(
            meeting_date=meeting_date,
            meeting_time=meeting_time,
            # desmeeting=desmeeting,
            meeting_venue = meeting_venue,
            meeting_mode = meeting_mode,
            meeting_agenda = meeting_agenda
        )
        meeting.save()
        return redirect('admeeting')
    return render(request,'admintemp/adaddmeeting.html')
@never_cache
@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        meeting_venue = request.POST.get('meeting_venue')
        meeting_agenda = request.POST.get('meeting_agenda')
        # desmeeting = request.POST.get('desmeeting')
        report = request.POST.get('report')
        meeting.meeting_date = meeting_date
        meeting.meeting_time = meeting_time
        meeting.meeting_venue = meeting_venue
        meeting.meeting_agenda = meeting_agenda
        # meeting.desmeeting = desmeeting
        meeting.report = report
        meeting.save()
        return redirect('admeeting')
    return render(request, 'admintemp/edit_meeting.html', {'meeting': meeting})

def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting.is_active = False
        meeting.save()
        request.session['delete meet'] = True
        return redirect('admeeting')
    return render(request, 'admintemp/delete_meeting.html', {'meeting': meeting})

@never_cache
@login_required
def mmeeting(request):
    meetings = Meeting.objects.filter(is_active=True)
    from django.utils import timezone
    current_date = timezone.now().date()
    return render(request, 'membertemp/mmeeting.html', {'meetings': meetings, 'current_date': current_date})

from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.shortcuts import render

def generate_pdf(request):
    template = get_template('admintemp/generate_pdfmeeting.html')  # Use the new template

    context = {
        'meetings': Meeting.objects.filter(is_active=True),
        'current_date': timezone.now().date(),
    }

    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="meeting_table.pdf"'

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdfreport(request):
    template = get_template('admintemp/generate_pdfreport.html')  # Use the new template

    context = {
        'applications': ApplyCrop.objects.filter(is_approvedd='approved'),
        'crops': Crop.objects.all(),
        'current_date': timezone.now().date(),
    }

    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="meeting_table.pdf"'

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('loginn')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('loginn')

    
    
    
#new
    
    
@never_cache
@login_required    
def edit_attendance(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        report = request.POST.get('report')
        meeting.report = report
        meeting.save()
        return redirect('adattendance')
    return render(request, 'admintemp/edit_attendance.html', {'meeting': meeting})


def index(request):
    blogs = Product.objects.all()
    services = Service.objects.filter(is_active=True)

    # blogs = Blog.objects.all()
    # context={
    #     'blogs' : blogs,
    # }
    return render(request, 'index.html',{'blogs': blogs , 'services': services})


def product(request):
    blogs = Product.objects.all()
    return render(request, 'product.html',{'blogs': blogs})
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        blogname = request.POST.get('blogname')
        blogimage = request.FILES.get('blogimage')
        product.blogname = blogname
        product.blogimage = blogimage
        product.save()
        return redirect('adproduct')
    return render(request, 'admintemp/edit_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        request.session['delete product'] = True
        return redirect('adproduct')
    return render(request, 'admintemp/delete_product.html', {'product': product})
def adproduct(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'admintemp/adproduct.html',{'products': products})
def adaddproduct(request):
    if request.method == 'POST':
        blogname = request.POST.get('blogname')
        # blogcategory = request.POST.get('blogcategory')
        # blogdes = request.POST.get('blogdes')
        blogimage = request.FILES.get('blogimage')  # Assuming 'blogimage' is the name attribute in your HTML form

        obj = Product()
        obj.blogname = blogname
        # obj.blogcategory = blogcategory
        # obj.blogdes = blogdes
        obj.blogimage = blogimage
        obj.save()

        return redirect('adproduct')  # Redirect to the 'adblog' view after successful creation

    return render(request, 'admintemp/adaddproduct.html')
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Driver

# def adadddriver(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         dage = request.POST.get('dage')
#         dgender = request.POST.get('dgender', 'Default Gender')
#         daddress = request.POST.get('daddress')
#         ddis = request.POST.get('ddis', 'Default District')
#         dtaluk = request.POST.get('dtaluk', 'Default Taluk')
#         dpanchayat = request.POST.get('dpanchayat', 'Default Panchayat')
#         dwardno = request.POST.get('dwardno')
#         dpin = request.POST.get('dpin')
#         dphone = request.POST.get('dphone')
#         dlisence = request.POST.get('dlisence')
#         dvehicle = request.POST.get('dvehicle')
#         dvehicletype = request.POST.get('dvehicletype')
#         ddate = request.POST.get('ddate')
#         dbio = request.POST.get('dbio')
#         profile_photo = request.FILES.get('profile_photo')

#         role = CustomUser.DRIVER
#         print(role)

#         if CustomUser.objects.filter(email=email, role=CustomUser.DRIVER).exists():
#             messages.info(request, 'Email already exists')
#             return redirect('adadddriver')
#         else:
#             user = CustomUser.objects.create_user(email=email, password=password, name=name)
#             user.role = CustomUser.DRIVER
#             user.save()

#             dri = Driver.objects.create(
#                 user=user, name=name, email=email, dgender=dgender, daddress=daddress, dage=dage, ddis=ddis,
#                 dtaluk=dtaluk, dPanchayat=dpanchayat, dwardno=dwardno, dpin=dpin, dphone=dphone,
#                 dbio=dbio,dvehicle=dvehicle,dvehicletype=dvehicletype, dlisence=dlisence, ddate=ddate, profile_photo=profile_photo
#             )

#             return redirect('addriver')
#     else:
#         return render(request, 'admintemp/adadddriver.html')

# def addriver(request):
#     drivers = Driver.objects.filter(is_active=True)
#     return render(request, 'admintemp/addriver.html', {'drivers': drivers})

@never_cache
@login_required    
def dapplied(request):
    products = Sell.objects.all()  # Retrieve all products from the Sell model
    return render(request, 'drivertemp/dapplied.html', {'products': products})
@never_cache
@login_required
def homepage(request):
    user = request.user
    blogs = Product.objects.all()
    services = Service.objects.filter(is_active=True)

    profile = FarmerProfile.objects.get(user=user)

    # Check if there are new crops added and create a notification only once
    if Crop.objects.filter(current=True).exists() and not Notification.objects.filter(user=user, title="New Crop Added").exists():
        message = "A new crop has been added."
        Notification.objects.create(
            user=user, title="New Crop Added", message=message, is_read=False
        )

    # Get success message from Django messages framework
    success_message = messages.get_messages(request)
    messages_to_display = [message.message for message in success_message if message.level == messages.SUCCESS]

    return render(request, 'homepage.html', {'profile': profile, 'blogs': blogs, 'services': services,'success_message':messages_to_display})
#service

def service(request):
   services = Service.objects.filter(is_active=True)
   return render(request, 'service.html',{'services': services})
def adaddservice(request):
    if request.method == 'POST':
        servicename = request.POST.get('servicename')
        serviceimage = request.FILES.get('serviceimage')  
        servicedes = request.POST.get('servicedes')
        obj = Service()
        obj.servicename = servicename
        obj.serviceimage = serviceimage
        obj.servicedes = servicedes
        obj.save()
        return redirect('adservice') 
    return render(request, 'admintemp/adaddservice.html')
def adservice(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'admintemp/adservice.html',{'services': services})

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        servicename = request.POST.get('servicename')
        serviceimage = request.FILES.get('serviceimage')
        servicedes = request.POST.get('servicedes')
        service.servicename = servicename
        service.serviceimage = serviceimage
        service.servicedes = servicedes
        service.save()
        return redirect('adservice')
    return render(request, 'admintemp/edit_service.html', {'service': service})
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.is_active = False
        service.save()
        request.session['delete service'] = True
        # service.delete()
        return redirect('adservice')
    return render(request, 'admintemp/delete_service.html', {'service': service})

@never_cache
@login_required
def dindex(request):
    user = request.user
    profile = Driver.objects.get(user=user)
    confirmed = Sellapply.objects.filter(is_confirmed=True,user_id=profile.user_id)
    confirmed_count = confirmed.count()
    collected = Sellapply.objects.filter(is_collected=True,user_id=profile.user_id)
    collected_count = collected.count()
    applied = Sellapply.objects.filter(is_apply='apply',user_id=profile.user_id)
    applied_count = applied.count()
    return render(request,'drivertemp/dindex.html',{'confirmed':confirmed,'confirmed_count':confirmed_count,'collected':collected,'collected_count':collected_count,'applied':applied,'applied_count':applied_count})
def dleave(request):
    return render(request,'drivertemp/dleave.html')
@never_cache
@login_required
def deditprofile(request):
    
    # user = request.user
    # profile = PatientProfile.objects.get(user=user)
    user = request.user
    driver = get_object_or_404(Driver, user=user)
    
    if request.method == "POST":
        print ('POST')
        driver.name = request.POST.get('name')
        driver.email = request.POST.get('email')
        # mem.gender = request.POST.get('gender')
        # mem.date_of_birth = request.POST.get('dob')
        # mem.date_of_join = request.POST.get('doj')        
        driver.daddress = request.POST.get('daddress')
        driver.ddis = request.POST.get('ddis')
        driver.dwardno = request.POST.get('dwardno')
        driver.dpin = request.POST.get('dpin')
        driver.dphone = request.POST.get('dphone')
        driver.dPanchayat = request.POST.get('dpanchayat')
        driver.dphone = request.POST.get('dphone')
        profile_photo = request.FILES.get('profile_photo')
        driver.profile_photo = profile_photo
        
        driver.damob = request.POST.get('damob')
        driver.daemail = request.POST.get('daemail')
        # mem.dob = request.POST.get('dob')
        driver.dlisence = request.POST.get('dlisence')
        driver.ddate = request.POST.get('ddate')
        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')


        if old_password and reset_password and request.POST.get('cpass') == reset_password:
            if user.check_password(old_password):
                # The old password is correct, set the new password
                user.set_password(reset_password)
                user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
            else:
                messages.error(request, "Incorrect old password. Password not updated.")
        else:
            print("Please fill all three password fields correctly.")
        
        driver.reset_password = reset_password
        driver.save()
        return redirect('deditprofile') 
    context = {
        'user': user,
        'driver': driver
    }
    return render(request, 'drivertemp/deditprofile.html',context)
@never_cache
@login_required
def dcalender(request):
    return render(request,'drivertemp/dcalender.html')
# def msell(request):
#     profile = Member.objects.get(user=request.user)
#     products = Sell.objects.filter(member=profile)
#     current_date = date.today()

#       # Retrieve all products from the Sell model
#     return render(request, 'membertemp/msell.html', {'products': products})

def accept_certification(request, certification_id):
    certification = get_object_or_404(Sell, id=certification_id)
    if request.method == 'POST':
        certification.is_accept = Sell.ACCEPT  # Set it to 'approved'
        certification.save()
    return redirect('msell')
def remove_certification(request, certification_id):
    certification = get_object_or_404(Sell, id=certification_id)
    if request.method == 'POST':
        certification.is_accept = Sell.REMOVE  # Set it to 'rejected'
        certification.save()
    return redirect('msell')
def remove_scertification(request, certification_id):
    certification = get_object_or_404(Sell, id=certification_id)
    if request.method == 'POST':
        certification.is_accept = Sell.REMOVE  # Set it to 'rejected'
        certification.save()
    return redirect('msellapprove')
@never_cache
@login_required
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        dname = request.POST.get('dname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dage = request.POST.get('dage')
        dgender = request.POST.get('dgender', 'Default Gender')
        daddress = request.POST.get('daddress')
        ddis = request.POST.get('ddis', 'Default District')  # Set a default value for District
        dtaluk = request.POST.get('dtaluk', 'Default Taluk')   # Set a default value for Taluk
        dpanchayat = request.POST.get('dpanchayat', 'Default Panchayat')  # Set a default value for Panchayat
        dwardno = request.POST.get('dwardno')
        dpin = request.POST.get('dpin')
        dphone = request.POST.get('dphone')
        dlisence = request.POST.get('dlisence')
        ddate = request.POST.get('ddate')
        dbio = request.POST.get('dbio')
        # profile_photo = request.FILES.get('profile_photo')
        # Update the member's attributes with the new data
        driver.name = dname
        driver.email = email
        driver.password = password
        # member.gender = gender
        driver.dage = dage
        driver.daddress = daddress
        driver.ddis = ddis
        driver.dtaluk = dtaluk
        driver.dPanchayat = dpanchayat
        driver.dwardno = dwardno
        driver.dpin = dpin
        driver.dphone = dphone
        driver.dbio = dbio
        driver.dlisence = dlisence
        driver.ddate = ddate
        # driver.profile_photo = profile_photo
        # Save the updated member object
        driver.save()

        # Redirect to the member list page after editing
        return redirect('driver')

    return render(request, 'admintemp/edit_driver.html', {'driver': driver})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        # Delete the member object
        driver.is_active = False
        driver.save()
        request.session['delete driver'] = True
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('driver')

    return render(request, 'admintemp/delete_driver.html', {'driver': driver})


# def dispro(request):
#     approved_products = Sell.objects.filter(is_accept='accept')
#     return render(request, 'membertemp/msellapprove.html', {'approved_products': approved_products})
def search_driver(request):
    drivername = request.GET.get('drivername', '')
    # crops = Crop.objects.filter(Namec__icontains=cropname)

    if drivername:
        drivers = Driver.objects.filter(name__icontains=drivername)
    else:
        drivers = Driver.objects.all()
    
    return render(request, 'admintemp/addriver.html', {'drivers': drivers, 'drivername': drivername})

#ProductCost
@never_cache
@login_required
def adproductcost(request):
    product_costs = Productcost.objects.filter(is_active=True)
    return render(request, 'admintemp/adproductcost.html', {'product_costs': product_costs})
@never_cache
@login_required
def adaddproductcost(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        # quantity = request.POST.get('quantity')  # Change this line
        price = request.POST.get('price')

        obj = Productcost()
        obj.pname = pname
        # obj.quantity = quantity
        obj.price = price
        obj.save()
        return redirect('adproductcost') 
    return render(request, 'admintemp/adaddproductcost.html')
@never_cache
@login_required
def edit_product_cost(request, product_cost_id):
    productcost = get_object_or_404(Productcost, id=product_cost_id)
    if request.method == 'POST':
        pname = request.POST.get('pname')
        # quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        productcost.pname = pname
        # productcost.quantity = quantity
        productcost.price = price
        productcost.save()
        return redirect('adproductcost')
    return render(request, 'admintemp/edit_product_cost.html', {'productcost': productcost})

def delete_product_cost(request, product_cost_id):
    productcost = get_object_or_404(Productcost, id=product_cost_id)
    if request.method == 'POST':
        productcost.is_active = False
        productcost.save()
        request.session['delete pro'] = True
        return redirect('adproductcost')
    return render(request, 'admintemp/delete_product_cost.html', {'productcost': productcost})

def pricelist1(request):
    product_costs = Productcost.objects.all()
    return render(request,'pricelist1.html', {'product_costs':product_costs })
@never_cache
@login_required
def pricelist2(request):
    product_costs = Productcost.objects.all()
    return render(request, 'pricelist2.html', {'product_costs': product_costs})

from django.http import HttpResponseForbidden

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseForbidden
from .models import FarmerProfile, Member, Sell
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FarmerProfile, Member, Sell
from datetime import datetime
@never_cache
@login_required
def sellcrop(request):
    farmer_profile = FarmerProfile.objects.get(user=request.user)
    product_name = request.GET.get('product_name', '')
    sell_date = None
    error_message = None

    if request.method == 'POST':
        farmerName = request.POST.get('farmerName')
        address = request.POST.get('address')
        wardNo = request.POST.get('wardno')
        name = request.POST.get('pname')
        quantity = request.POST.get('quantity')
        member = Member.objects.get(wardno=wardNo)
        sell_date_str = request.POST.get('sell_date')

        if sell_date_str:
            sell_date = datetime.strptime(sell_date_str, '%Y-%m-%d').date()

            existing_sell = Sell.objects.filter(
                farmerName=farmerName,
                name=name,
                quantity=quantity,
                sell_date=sell_date
            ).exists()

            if existing_sell:
                error_message = "You have already applied for the same product and quantity on the same day."
            else:
                sell_instance = Sell(
                    farmerName=farmerName,
                    address=address,
                    wardNo=wardNo,
                    name=name,
                    quantity=quantity,
                    member=member,
                    sell_date=sell_date
                )
                sell_instance.save()

                # Add success message
                messages.success(request, "You have successfully applied to sell the Product.")

                # Redirect to homepage
                return redirect('homepage')

    return render(request, 'sellcrop.html', {
        'farmer_name': farmer_profile.first_name,
        'farmer_lname': farmer_profile.last_name,
        'address': farmer_profile.address,
        'wardNo': farmer_profile.ward,
        'product_name': product_name,
        'sell_date': sell_date,
        'error_message': error_message
    })


from django.shortcuts import render
from .models import Sell


from django.shortcuts import render
from .models import Sell

# def selldetails(request, sell_id):
#     sell_instance = Sell.objects.get(id=sell_id)

#     return render(request, 'selldetails.html', {
#         'sell_instance': sell_instance,
#     })


from django.http import HttpResponseForbidden
@never_cache
@login_required
def sellcrop2(request):
    farmer_profile = FarmerProfile.objects.get(user=request.user)
    product_name = request.GET.get('product_name', '')
    sell_date = None  # Initialize sell_date variable outside the if block
    error_message = None  # Initialize error_message variable

    if request.method == 'POST':
        farmerName = request.POST.get('farmerName')
        address = request.POST.get('address')
        wardNo = request.POST.get('wardno')
        name = request.POST.get('pname')
        quantity = request.POST.get('quantity')
        member = Member.objects.get(wardno=wardNo)
        sell_date_str = request.POST.get('sell_date')

        if sell_date_str:  # Check if sell_date_str is not empty
            sell_date = datetime.strptime(sell_date_str, '%Y-%m-%d').date()

            # Check if the farmer has already applied for the same product and quantity on the same day
            existing_sell = Sell.objects.filter(
                farmerName=farmerName,
                name=name,
                quantity=quantity,
                sell_date=sell_date
            ).exists()

            if existing_sell:
                error_message = "You have already applied for the same product and quantity on the same day."
            else:
                sell_instance = Sell(
                    farmerName=farmerName,
                    address=address,
                    wardNo=wardNo,
                    name=name,
                    quantity=quantity,
                    member=member,
                    sell_date=sell_date  # Assign sell_date directly
                )
                sell_instance.save()

                # Add success message
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('homepage')  # Redirect to the homepage after successful submission

    return render(request, 'sellcrop2.html', {
        'farmer_name': farmer_profile.first_name,
        'farmer_lname': farmer_profile.last_name,
        'address': farmer_profile.address,
        'wardNo': farmer_profile.ward,
        'product_name': product_name,
        'sell_date': sell_date,  # Pass sell_date to the template
        'error_message': error_message  # Pass error_message to the template
    })
@never_cache
@login_required
def msell(request):
    profile = Member.objects.get(user=request.user)
    today_date = timezone.now().date()
    products = Sell.objects.filter(member=profile, is_accept='pending', sell_date__gte=today_date)
    return render(request, 'membertemp/msell.html', {'products': products, 'today_date': today_date})
@never_cache
@login_required
def msellapprove(request):
    profile = Member.objects.get(user=request.user)

    today_date = timezone.now().date()

    approved_products = Sell.objects.filter(member=profile,is_accept='accept')
    return render(request, 'membertemp/msellapprove.html', {'approved_products': approved_products ,'today_date':today_date})
@never_cache
@login_required
def driverapply(request):
    approved_products = Sell.objects.filter(is_accept='accept')
    data = []  # List to store dictionaries containing product, is_apply status, and confirmation status
    today_date = timezone.now().date()

    for product in approved_products:
        is_apply = 'pending'
        is_confirmed = False

        # Check if the driver has applied
        if Sellapply.objects.filter(sell=product, user=request.user).exists():
            is_apply = 'apply'

            # Check if the driver's application is confirmed
            sell_apply = Sellapply.objects.get(sell=product, user=request.user)
            is_confirmed = sell_apply.is_confirmed

        data.append({'product': product, 'is_apply': is_apply, 'is_confirmed': is_confirmed})

    return render(request, 'drivertemp/driverapply.html', {'data': data, 'today_date': today_date})

def apply_certification(request, certification_id):
    print("something452")
    certification = get_object_or_404(Sell, id=certification_id)
    print(certification)
    driver = Driver.objects.get(user=request.user)

    if request.method == 'POST':
  
        Sellapply.objects.create(
            user=request.user,
            driver=driver,
            sell=certification,
            is_apply=Sellapply.APPLY,
        )
    return redirect('driverapply')
@never_cache
@login_required
def mdriverapplied(request):
    profile = Member.objects.get(user=request.user)
    sells = Sell.objects.filter(member=profile)
    # Get all Sellapply instances related to the sells, including the driver information
    applies = Sellapply.objects.filter(sell__in=sells, is_apply='apply')

    for sellapply in applies:
        if Sellapply.objects.filter(
            sell__farmerName=sellapply.sell.farmerName,
            sell__sell_date=sellapply.sell.sell_date,
            sell__name=sellapply.sell.name,
            is_confirmed=True
        ).exists():
            sellapply.is_confirm = Sellapply.CONFIRM

    drivers = Driver.objects.filter(is_active=True)
    return render(request, 'membertemp/mdriverapplied.html', {'applies': applies, 'drivers': drivers})

def confirmation(request, apply_id):
    sell_apply = get_object_or_404(Sellapply, id=apply_id)
    
    if request.method == 'POST':
        sell_apply.is_confirmed = True
        sell_apply.save()

    return redirect('mdriverapplied')  # Replace with your actual view name

# def dconfirmed(request):
#     user = request.user
#     profile = Driver.objects.get(user=user)
#     confirmed_data = Sellapply.objects.filter(is_confirmed=True,driver_id=profile.id)
#     return render(request, 'drivertemp/dconfirmed.html', {'confirmed_data': confirmed_data})
@never_cache
@login_required
def dconfirmed(request):
    user = request.user
    profile = Driver.objects.get(user=user)
    confirmed_data = Sellapply.objects.filter(is_confirmed=True, driver_id=profile.id)

    for entry in confirmed_data:
        try:
            product_cost = Productcost.objects.get(pname=entry.sell.name)
            entry.total_cost = float(entry.sell.quantity) * product_cost.price
        except Productcost.DoesNotExist:
            entry.total_cost = 0  # Set a default value when the product is not found

        # Save the updated entry to persist changes in the database
        entry.save()

    return render(request, 'drivertemp/dconfirmed.html', {'confirmed_data': confirmed_data})
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Driver, Sellapply, Productcost
def dconfirmed_report(request):
    return render(request,'drivertemp/dconfirmed_report.html')
def generate_pdf_dconfirmed(request):
    user = request.user
    profile = Driver.objects.get(user=user)
    confirmed_data = Sellapply.objects.filter(is_confirmed=True, driver_id=profile.id)

    for entry in confirmed_data:
        try:
            product_cost = Productcost.objects.get(pname=entry.sell.name)
            entry.total_cost = float(entry.sell.quantity) * product_cost.price
        except Productcost.DoesNotExist:
            entry.total_cost = 0  # Set a default value when the product is not found

        # Save the updated entry to persist changes in the database
        entry.save()

    template_path = 'drivertemp/generate_pdf_dconfirmed.html'
    context = {'confirmed_data': confirmed_data}

    # Render the template
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="generate_pdf_dconfirmed.pdf"'

    # Generate PDF using PISA
    pisa_status = pisa.CreatePDF(
        html,
        dest=response,
        encoding='UTF-8',
    )

    if pisa_status.err:
        return HttpResponse('Failed to generate PDF: {}'.format(pisa_status.err))

    return response


def collected(request, collection_id):
    collection = get_object_or_404(Sellapply, id=collection_id)
    
    if request.method == 'POST':
        collection.is_collected = True
        collection.save()

    return redirect('dconfirmed')  # Replace with your actual view name

# def mconfirmed(request):
#     confirmed_apply = get_object_or_404(Sellapply, is_confirmed=True)
#     return render(request, 'membertemp/mconfirmed.html', {'confirmed_apply': confirmed_apply})
# def selldetails(request):
#     current_farmer_profile = request.user.farmerprofile
#     sells = Sell.objects.filter(farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}").select_related('member', 'driver').prefetch_related('sellapply_set__driver')
#     return render(request, 'selldetails.html', {'sells': sells})
from django.db.models import F, ExpressionWrapper, FloatField

# def selldetails(request):
#     current_farmer_profile = request.user.farmerprofile
#     sells = Sell.objects.filter(farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}") \
#                         .select_related('member', 'driver')

#     for sell in sells:
#         try:
#             product_cost = Productcost.objects.get(pname=sell.name)
#             sell.total_cost = float(sell.quantity) * product_cost.price
#         except Productcost.DoesNotExist:
#             sell.total_cost = "Add Amount"  # Set a message when the product is not found
#         sell_applies = Sellapply.objects.filter(sell=sell)
#         if sell_applies.exists():
#             sell.total_cost = sell_applies.first().total_cost
#     return render(request, 'selldetails.html', {'sells': sells})

def update_total_amount(user):
    sells = Sell.objects.filter(farmerName=f"{user.farmerprofile.first_name} {user.farmerprofile.last_name}")
    total_amount = 0

    for sell in sells:
        try:
            product_cost = Productcost.objects.get(pname=sell.name)
            sell.total_cost = float(sell.quantity) * product_cost.price
            sell.save()

            sell_applies = Sellapply.objects.filter(sell=sell)
            if sell_applies.exists():
                for apply in sell_applies:
                    total_cost = apply.total_cost if apply.total_cost is not None else 0
                    total_amount += total_cost
        except Productcost.DoesNotExist:
            sell.total_cost = 0

    user.farmerprofile.total_amount = total_amount
    user.farmerprofile.save()

    # Create or update Total model entry for the user
    total_entry, created = Total.objects.get_or_create(user=user)
    total_entry.farmerName = f"{user.farmerprofile.first_name} {user.farmerprofile.last_name}"
    total_entry.total_amount = total_amount
    total_entry.save()
@never_cache
@login_required
def selldetails(request):
    current_farmer_profile = request.user.farmerprofile
    sells = Sell.objects.filter(farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}") \
                        .select_related('member', 'driver')

    total_amount = 0  # Initialize total_amount variable

    for sell in sells:
        try:
            product_cost = Productcost.objects.get(pname=sell.name)
            sell.total_cost = float(sell.quantity) * product_cost.price
            sell.save()

            sell_applies = Sellapply.objects.filter(sell=sell)
            if sell_applies.exists():
                sell.total_cost = sell_applies.first().total_cost
                sell.save()

            total_amount += sell.total_cost  # Add to total_amount
        except Productcost.DoesNotExist:
            sell.total_cost = 0

    # Update the total_amount for the current user
    update_total_amount(request.user)

    return render(request, 'selldetails.html', {'sells': sells, 'total_amount': total_amount})

from django.shortcuts import render, redirect
from .models import Sellapply

# def adselldetails(request):
#     confirmed_data = Sellapply.objects.filter(is_confirmed=True)

#     if request.method == 'POST':
#         entry_id = request.POST.get('entry_id')
#         total_cost = request.POST.get('total_cost')

#         entry = Sellapply.objects.get(pk=entry_id)
#         entry.total_cost = total_cost
#         entry.save()

#         # Get the updated entry from the database
#         entry = Sellapply.objects.get(pk=entry_id)

#         return render(request, 'admintemp/adselldetails.html', {'confirmed_data': confirmed_data, 'updated_entry': entry})

#     for entry in confirmed_data:
#         try:
#             product_cost = Productcost.objects.get(pname=entry.sell.name)
#             entry.total_cost = float(entry.sell.quantity) * product_cost.price
#         except Productcost.DoesNotExist:
#             entry.total_cost = "Add Amount"

#     return render(request, 'admintemp/adselldetails.html', {'confirmed_data': confirmed_data})

def update_total_cost(request, entry_id):
    if request.method == 'POST':
        total_amount_new = request.POST.get('total_amount_new')

        try:
            entry = Sellapply.objects.get(pk=entry_id)
            entry.total_amount_new = total_amount_new
            entry.save()
        except Sellapply.DoesNotExist:
            pass  # Handle the case where the Sellapply entry is not found

    return redirect('adselldetails')


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from xhtml2pdf import pisa  # Ensure you have xhtml2pdf installed

def generate_pdf_bill(request, sell_id):
    sell = get_object_or_404(Sell, id=sell_id)
    sellapply = sell.sellapply_set.first()  # Assuming a related name is set in Sell model

    if not sellapply:
        return HttpResponse('Sellapply not found for this Sell.')

    template_path = 'admintemp/generate_pdf_bill.html'
    context = {'sell': sell, 'sellapply': sellapply}
    
    # Create a Django response object, specifying content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_{sell.id}.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

def adgenerate_pdf_bill(request, sell_id):
    sell = get_object_or_404(Sell, id=sell_id)
    sellapply = sell.sellapply_set.first()

    if not sellapply:
        return HttpResponse('Sellapply not found for this Sell.')

    template_path = 'admintemp/generate_pdf_bill.html'  # Change the template name
    context = {'sell': sell, 'sellapply': sellapply}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_{sell.id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response


from django.db.models import Sum
# def adaccount(request):
#     filtered_data = Sellapply.objects.filter(
#         is_confirmed=True,
#         is_collected=True,
#         is_apply='apply',
#         sell__is_accept='accept'
#     )

#     # Aggregate total cost for each farmer using the related Sell model
#     farmer_totals = Sellapply.objects.filter(is_confirmed=True).values('sell__farmerName').annotate(total_amount=Sum('total_cost'))

#     return render(request, 'admintemp/adaccount.html', {'farmer_totals': farmer_totals, 'filtered_data': filtered_data})

# def adaccount(request):
#     farmers_total_cost = Sellapply.objects.filter(is_confirmed=True).values('sell__farmerName').annotate(total_cost=Sum('total_cost'))

#     return render(request, 'admintemp/adaccount.html', {'farmers_total_cost': farmers_total_cost})



# def account(request):
#     current_farmer_profile = request.user.farmerprofile
#     sells = Sell.objects.filter(farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}") \
#                         .select_related('member', 'driver')

#     total_amount = 0  # Initialize total amount variable

#     for sell in sells:
#         try:
#             product_cost = Productcost.objects.get(pname=sell.name)
#             sell.total_cost = float(sell.quantity) * product_cost.price
#             total_amount += sell.total_cost  # Add each sell's total cost to the total amount
#         except Productcost.DoesNotExist:
#             sell.total_cost = 0  # Set to 0 when the product is not found

#     return render(request, 'account.html', {'total_amount': total_amount})
# from django.shortcuts import render




from django.shortcuts import render
from .models import Sell, Productcost, Sellapply

# def account(request):
#     current_farmer_profile = request.user.farmerprofile

#     # Filter sells based on farmerName
#     sells = Sell.objects.filter(
#         farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#     ).select_related('member', 'driver')

#     accepted_sells = sells.filter(
#         is_accept='accept',
#         sellapply__is_confirmed=True,
#         sellapply__is_collected=True
#     )

#     total_amount = 0  # Initialize total amount variable

#     for sell in accepted_sells:
#         try:
#             product_cost = Productcost.objects.get(pname=sell.name)
#             sell.total_cost = float(sell.quantity) * product_cost.price
#             total_amount += sell.total_cost  # Add each sell's total cost to the total amount

#             # Include total_cost from Sellapply model if it's not None
#             total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else 0
#             total_amount += total_cost_sellapply
#         except Productcost.DoesNotExist:
#             sell.total_cost = 0  # Set to 0 when the product is not found

#     return render(request, 'account.html', {'total_amount': total_amount, 'accepted_sells': accepted_sells})

from django.shortcuts import render

# def account(request):
#     confirmed_data = Sellapply.objects.filter(is_confirmed=True)
#     total_paid_amount_by_user = {}  
#     total_paid_amount = 0  

#     for entry in confirmed_data:
#         try:
#             product_cost = Productcost.objects.get(pname=entry.sell.name)
#             entry.total_cost = float(entry.sell.quantity) * product_cost.price
#         except Productcost.DoesNotExist:
#             entry.total_cost = "Add Amount"

#         if entry.is_amount:
#             user_name = entry.sell.farmerName
#             total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, 0) + entry.total_cost
#             total_paid_amount += entry.total_cost

#     return render(request, 'account.html', {'total_paid_amount_by_user': total_paid_amount_by_user})


from django.shortcuts import render
from .models import Sellapply, Productcost, Sell
from django.shortcuts import get_object_or_404

# def account(request):
#     current_farmer_profile = request.user.farmerprofile

#     confirmed_data = Sellapply.objects.filter(
#         is_confirmed=True,
#         sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#     )
#     total_paid_amount_by_user = {}
#     total_paid_amount = 0

#     for entry in confirmed_data:
#         try:
#             product_cost = Productcost.objects.get(pname=entry.sell.name)
#             entry.total_cost = float(entry.sell.quantity) * product_cost.price
#         except Productcost.DoesNotExist:
#             entry.total_cost = "Add Amount"

#         if entry.is_amount:
#             user_name = entry.sell.farmerName
#             total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, 0) + entry.total_cost
#             total_paid_amount += entry.total_cost

#     sells = Sell.objects.filter(
#         farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#     ).select_related('member', 'driver')

#     accepted_sells = sells.filter(
#         is_accept='accept',
#         sellapply__is_confirmed=True,
#         sellapply__is_collected=True
#     )

#     total_amount = 0

#     for sell in accepted_sells:
#         try:
#             product_cost = Productcost.objects.get(pname=sell.name)
#             sell.total_cost = float(sell.quantity) * product_cost.price
#             total_amount += sell.total_cost

#             total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else 0
#             total_amount += total_cost_sellapply
#         except Productcost.DoesNotExist:
#             sell.total_cost = 0

#     return render(request, 'account.html', {'total_paid_amount_by_user': total_paid_amount_by_user, 'total_amount': total_amount})
from decimal import Decimal
from django.db.models import Sum
@never_cache
@login_required
def account(request):
    current_farmer_profile = request.user.farmerprofile

    # Fetch the Total instance for the current user
    total_instance = Total.objects.filter(user=request.user).first()

    confirmed_data = Sellapply.objects.filter(
        is_confirmed=True,
        sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
    )
    total_paid_amount_by_user = {}
    total_paid_amount = Decimal('0')

    for entry in confirmed_data:
        try:
            product_cost = Productcost.objects.get(pname=entry.sell.name)
            entry.total_cost = Decimal(entry.sell.quantity) * Decimal(product_cost.price)
        except Productcost.DoesNotExist:
            entry.total_cost = Decimal('0')

        if entry.is_amount:
            user_name = entry.sell.farmerName
            total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, Decimal('0')) + entry.total_cost
            total_paid_amount += entry.total_cost

    sells = Sell.objects.filter(
        farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
    ).select_related('member', 'driver')

    accepted_sells = sells.filter(
        is_accept='accept',
        sellapply__is_confirmed=True,
        sellapply__is_collected=True
    )

    total_amount = Decimal('0')

    for sell in accepted_sells:
        try:
            product_cost = Productcost.objects.get(pname=sell.name)
            sell.total_cost = Decimal(sell.quantity) * Decimal(product_cost.price)
            total_amount += sell.total_cost

            total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else Decimal('0')
            total_amount += total_cost_sellapply
        except Productcost.DoesNotExist:
            sell.total_cost = Decimal('0')

    # Calculate balance for each user
    balance_list = [(user_name, total_paid_amount_by_user.get(user_name, Decimal('0')), total_amount - total_paid_amount_by_user.get(user_name, Decimal('0'))) for user_name in total_paid_amount_by_user]

    # Fetch total_amount_per_farmer
    total_amount_per_farmer = Sellapply.objects.filter(
        is_confirmed=True,
        sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
    ).values('sell__farmerName').annotate(total_amount=Sum('total_cost'))

    return render(request, 'account.html', {'balance_list': balance_list, 'total_amount': total_amount, 'total_instance': total_instance, 'total_amount_per_farmer': total_amount_per_farmer})

from django.shortcuts import render
from .models import Sell, Productcost, Sellapply
from django.shortcuts import render
from .models import FarmerProfile, Sell, Productcost, Sellapply
# # views.py
# def adaccount(request):
#     all_farmer_profiles = FarmerProfile.objects.all()

#     total_amounts = {}

#     for farmer_profile in all_farmer_profiles:
#         sells = Sell.objects.filter(
#             farmerName=f"{farmer_profile.first_name} {farmer_profile.last_name}"
#         ).select_related('member', 'driver')

#         accepted_sells = sells.filter(
#             is_accept='accept',
#             sellapply__is_confirmed=True,
#             sellapply__is_collected=True
#         )

#         total_amount = 0

#         for sell in accepted_sells:
#             try:
#                 product_cost = Productcost.objects.get(pname=sell.name)
#                 sell.total_cost = float(sell.quantity) * product_cost.price
#                 total_amount += sell.total_cost

#                 total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else 0
#                 total_amount += total_cost_sellapply
#             except Productcost.DoesNotExist:
#                 sell.total_cost = 0

#         # Check if the farmer has at least one collected sell
#         if accepted_sells.exists():
#             total_amounts[farmer_profile] = total_amount

#     return render(request, 'admintemp/adaccount.html', {'total_amounts': total_amounts})
# def pay_entry(request, entry_id):
#     entry = get_object_or_404(Sellapply, id=entry_id)
    
#     if request.method == 'POST':
#         entry.is_amount = True
#         entry.save()

#     return redirect('adselldetails') 
from .models import Total
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal  # Import Decimal for precise arithmetic
from .models import Sellapply, Total, Productcost  # Import your models as needed
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from collections import defaultdict
from .models import Sellapply, Productcost, Total

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum
from collections import defaultdict
from decimal import Decimal
from .models import Sellapply, Total


from django.shortcuts import render, redirect
from django.db.models import Sum
from decimal import Decimal
from .models import Sellapply
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sellapply, Total
@never_cache
@login_required
def adselldetails(request):
    confirmed_data = Sellapply.objects.filter(is_confirmed=True)
    
    # Calculate total amount per farmer
    total_amount_per_farmer = Sellapply.objects.filter(is_confirmed=True).values('sell__farmerName').annotate(total_amount=Sum('total_cost'))
    
    # Calculate total paid amount per farmer
    paid_amount_per_farmer = Sellapply.objects.filter(is_amount=True).values('sell__farmerName').annotate(total_paid=Sum('total_cost'))

    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        total_cost = request.POST.get('total_cost')

        # Update total_cost in Sellapply model
        entry = Sellapply.objects.get(pk=entry_id)
        entry.total_cost = total_cost
        entry.save()

        # Update paid amount per farmer
        farmer_name = entry.sell.farmerName
        total_obj, created = Total.objects.get_or_create(user=entry.sell.user, farmerName=farmer_name)
        total_obj.paid_amount += Decimal(total_cost)
        total_obj.save()

        return redirect('adselldetails')  # Redirect back to the adselldetails page after updating

    return render(request, 'admintemp/adselldetails.html', {'confirmed_data': confirmed_data, 'total_amount_per_farmer': total_amount_per_farmer, 'paid_amount_per_farmer': paid_amount_per_farmer})

from django.shortcuts import get_object_or_404
from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sellapply, Total
from django.shortcuts import redirect
from .models import Sellapply, Total
from django.shortcuts import redirect
from decimal import Decimal
from .models import Sellapply, Total

from django.shortcuts import redirect
from decimal import Decimal
from .models import Sellapply, Total

def pay_entry(request, entry_id):
    entry = Sellapply.objects.get(pk=entry_id)
    
    # Check if the payment amount exceeds the total cost
    if Decimal(entry.total_cost) > entry.paid_amount:
        # Update the paid amount for the corresponding farmer
        farmer_name = entry.sell.farmerName
        total_obj, created = Total.objects.get_or_create(user=entry.sell.user, farmerName=farmer_name)
        
        # Reduce the paid amount for the specific farmer by the corresponding total_cost
        total_obj.paid_amount -= Decimal(entry.total_cost)
        total_obj.save()
        
        # Update the Sellapply entry's is_amount field to indicate payment has been made
        entry.is_amount = True
        entry.save()
        
        return redirect('adselldetails')  # Redirect back to the adselldetails page after payment
    else:
        # Handle the case where payment amount exceeds total cost
        # You can add your logic here, such as displaying an error message or redirecting to another page
        return HttpResponse("Payment amount exceeds total cost.")

from django.shortcuts import render
from .models import Sellapply, Productcost, Sell


# def all_accounts(request):
#     all_farmers = []

#     for farmer_profile in FarmerProfile.objects.all():  # Assuming FarmerProfile is your model for farmer profiles
#         current_farmer_profile = farmer_profile

#         # Filtering Sellapply data based on specified conditions
#         confirmed_data = Sellapply.objects.filter(
#             is_confirmed=True,
#             is_collected=True,
#             is_apply='apply',
#             sell__is_accept='accept',
#             sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         )

#         # If there are no confirmed_data, skip to the next farmer
#         if not confirmed_data.exists():
#             continue

#         total_paid_amount_by_user = {}
#         total_paid_amount = 0

#         for entry in confirmed_data:
#             try:
#                 product_cost = Productcost.objects.get(pname=entry.sell.name)
#                 entry.total_cost = float(entry.sell.quantity) * product_cost.price
#             except Productcost.DoesNotExist:
#                 entry.total_cost = "Add Amount"

#             if entry.is_amount:
#                 user_name = entry.sell.farmerName
#                 total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, 0) + entry.total_cost
#                 total_paid_amount += entry.total_cost

#         sells = Sell.objects.filter(
#             farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         ).select_related('member', 'driver')

#         accepted_sells = sells.filter(
#             is_accept='accept',
#             sellapply__is_confirmed=True,
#             sellapply__is_collected=True
#         )

#         total_amount = 0

#         for sell in accepted_sells:
#             try:
#                 product_cost = Productcost.objects.get(pname=sell.name)
#                 sell.total_cost = float(sell.quantity) * product_cost.price
#                 total_amount += sell.total_cost

#                 total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else 0
#                 total_amount += total_cost_sellapply
#             except Productcost.DoesNotExist:
#                 sell.total_cost = 0

#         # Calculate balance for each user
#         balance_list = [
#             (user_name, total_paid_amount_by_user.get(user_name, 0), total_amount - total_paid_amount_by_user.get(user_name, 0))
#             for user_name in total_paid_amount_by_user
#         ]

#         all_farmers.append({
#             'farmer_profile': current_farmer_profile,
#             'balance_list': balance_list,
#             'total_amount': total_amount
#         })

#     return render(request, 'admintemp/all_accounts.html', {'all_farmers': all_farmers})


from decimal import Decimal  # Import the Decimal type

from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from .models import FarmerProfile, Sellapply, Productcost, Sell, Total
from django.db.models import Sum
# def all_accounts(request):
#     all_farmers = []

#     for farmer_profile in FarmerProfile.objects.all():
#         current_farmer_profile = farmer_profile
#         confirmed_data = Sellapply.objects.filter(
#             is_confirmed=True,
#             is_collected=True,
#             is_apply='apply',
#             sell__is_accept='accept',
#             sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         )

#         if not confirmed_data.exists():
#             continue

#         total_paid_amount_by_user = {}
#         total_paid_amount = Decimal('0')  # Initialize total_paid_amount as Decimal

#         for entry in confirmed_data:
#             try:
#                 product_cost = Productcost.objects.get(pname=entry.sell.name)
#                 entry.total_cost = Decimal(entry.sell.quantity) * Decimal(product_cost.price)
#             except Productcost.DoesNotExist:
#                 entry.total_cost = Decimal(0)

#             if entry.is_amount:
#                 user_name = entry.sell.farmerName
#                 total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, Decimal('0')) + entry.total_cost
#                 total_paid_amount += entry.total_cost

#         # Fetch total_amount and paid_amount from the Total model
#         total_entry = Total.objects.filter(user=current_farmer_profile.user).first()
#         total_amount_from_total_model = total_entry.total_amount if total_entry else Decimal('0')
#         paid_amount_from_total_model = total_entry.paid_amount if total_entry else Decimal('0')

#         sells = Sell.objects.filter(
#             farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         ).select_related('member', 'driver')

#         accepted_sells = sells.filter(
#             is_accept='accept',
#             sellapply__is_confirmed=True,
#             sellapply__is_collected=True
#         )

#         total_amount = Decimal('0')  # Initialize total_amount as Decimal

#         for sell in accepted_sells:
#             try:
#                 product_cost = Productcost.objects.get(pname=sell.name)
#                 sell.total_cost = Decimal(sell.quantity) * Decimal(product_cost.price)
#                 total_amount += sell.total_cost

#                 total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else Decimal('0')
#                 total_amount += total_cost_sellapply

#                 # Add total_amount_new to total_amount
#                 total_amount += sell.sellapply_set.first().total_amount_new if sell.sellapply_set.exists() and sell.sellapply_set.first().total_amount_new is not None else Decimal('0')
#             except Productcost.DoesNotExist:
#                 sell.total_cost = Decimal('0')

#         balance_list = [
#             (user_name, total_paid_amount_by_user.get(user_name, Decimal('0')), total_amount - total_paid_amount_by_user.get(user_name, Decimal('0')))
#             for user_name in total_paid_amount_by_user
#         ]

#         # Calculate the balance here and include it in the context
#         balance = total_amount_from_total_model - paid_amount_from_total_model

#         all_farmers.append({
#             'farmer_profile': current_farmer_profile,
#             'balance_list': balance_list,
#             'total_amount': total_amount_from_total_model,  # Include total_amount from Total model
#             'paid_amount': paid_amount_from_total_model,  # Include paid_amount from Total model
#             'balance': balance,  # Include the calculated balance
#         })

#     return render(request, 'admintemp/all_accounts.html', {'all_farmers': all_farmers})
from django.shortcuts import render
from django.db.models import Sum
from ceapp.models import CustomUser  # Import your custom user model
from .models import Sellapply, Total

# def all_accounts(request):
#     # Get total paid amount for each user along with their names
#     total_paid_amount_by_user = Total.objects.values('user').annotate(total_paid=Sum('paid_amount'))

#     # Fetch user names based on user IDs from your custom user model
#     for user_data in total_paid_amount_by_user:
#         user_id = user_data['user']
#         user_obj = CustomUser.objects.get(id=user_id)
#         user_data['user'] = user_obj.username  # Replace user ID with user name

#     return render(request, 'admintemp/all_accounts.html', {'total_paid_amount_by_user': total_paid_amount_by_user})
from django.shortcuts import render
from django.db.models import Sum
from .models import Total





# def all_accounts(request):
#     # Retrieve total paid amounts for each user along with their farmer names
#     users_total_paid = Total.objects.all().values('user__username', 'farmerName').annotate(total_paid=Sum('paid_amount'))

#     # Calculate total paid amount across all users
#     total_paid_amount = Total.objects.aggregate(Sum('paid_amount'))['paid_amount__sum'] or 0

#     return render(request, 'admintemp/all_accounts.html', {'users_total_paid': users_total_paid, 'total_paid_amount': total_paid_amount})

# def generate_pdf_all_accounts(request):
#     all_farmers = []

#     for farmer_profile in FarmerProfile.objects.all():
#         current_farmer_profile = farmer_profile
#         confirmed_data = Sellapply.objects.filter(
#             is_confirmed=True,
#             is_collected=True,
#             is_apply='apply',
#             sell__is_accept='accept',
#             sell__farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         )

#         if not confirmed_data.exists():
#             continue

#         total_paid_amount_by_user = {}
#         total_paid_amount = Decimal('0')  # Initialize total_paid_amount as Decimal

#         for entry in confirmed_data:
#             try:
#                 product_cost = Productcost.objects.get(pname=entry.sell.name)
#                 entry.total_cost = Decimal(entry.sell.quantity) * Decimal(product_cost.price)
#             except Productcost.DoesNotExist:
#                 entry.total_cost = Decimal(0)

#             if entry.is_amount:
#                 user_name = entry.sell.farmerName
#                 total_paid_amount_by_user[user_name] = total_paid_amount_by_user.get(user_name, Decimal('0')) + entry.total_cost
#                 total_paid_amount += entry.total_cost

#         # Fetch total_amount and paid_amount from the Total model
#         total_entry = Total.objects.filter(user=current_farmer_profile.user).first()
#         total_amount_from_total_model = total_entry.total_amount if total_entry else Decimal('0')
#         paid_amount_from_total_model = total_entry.paid_amount if total_entry else Decimal('0')

#         sells = Sell.objects.filter(
#             farmerName=f"{current_farmer_profile.first_name} {current_farmer_profile.last_name}"
#         ).select_related('member', 'driver')

#         accepted_sells = sells.filter(
#             is_accept='accept',
#             sellapply__is_confirmed=True,
#             sellapply__is_collected=True
#         )

#         total_amount = Decimal('0')  # Initialize total_amount as Decimal

#         for sell in accepted_sells:
#             try:
#                 product_cost = Productcost.objects.get(pname=sell.name)
#                 sell.total_cost = Decimal(sell.quantity) * Decimal(product_cost.price)
#                 total_amount += sell.total_cost

#                 total_cost_sellapply = sell.sellapply_set.first().total_cost if sell.sellapply_set.exists() and sell.sellapply_set.first().total_cost is not None else Decimal('0')
#                 total_amount += total_cost_sellapply
#             except Productcost.DoesNotExist:
#                 sell.total_cost = Decimal('0')

#         balance_list = [
#             (user_name, total_paid_amount_by_user.get(user_name, Decimal('0')), total_amount - total_paid_amount_by_user.get(user_name, Decimal('0')))
#             for user_name in total_paid_amount_by_user
#         ]

#         # Calculate the balance here and include it in the context
#         balance = total_amount_from_total_model - paid_amount_from_total_model

#         all_farmers.append({
#             'farmer_profile': current_farmer_profile,
#             'balance_list': balance_list,
#             'total_amount': total_amount_from_total_model,  # Include total_amount from Total model
#             'paid_amount': paid_amount_from_total_model,  # Include paid_amount from Total model
#             'balance': balance,  # Include the calculated balance
#         })

#     context = {'all_farmers': all_farmers}

#     # Render the HTML template to a string
#     template = get_template('admintemp/generate_pdf_all_accounts.html')
#     html = template.render(context)

#     # Create a PDF file
#     result_file = BytesIO()
#     pisa_status = pisa.CreatePDF(html, dest=result_file)

#     # Check if PDF creation was successful
#     if pisa_status.err:
#         return HttpResponse('Error creating PDF: %s' % pisa_status.err)

#     # Get the PDF content from the BytesIO buffer
#     pdf_content = result_file.getvalue()

#     # Set the HTTP response with PDF content
#     response = HttpResponse(pdf_content, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="payment_details.pdf"'

#     return response
@never_cache
@login_required
def adddriver(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dage = request.POST.get('dage')
        dgender = request.POST.get('dgender', 'Default Gender')
        daddress = request.POST.get('daddress')
        ddis = request.POST.get('ddis', 'Default District')
        dtaluk = request.POST.get('dtaluk', 'Default Taluk')
        dpanchayat = request.POST.get('dpanchayat', 'Default Panchayat')
        dwardno = request.POST.get('dwardno')
        dpin = request.POST.get('dpin')
        dphone = request.POST.get('dphone')
        dlisence = request.POST.get('dlisence')
        dvehicletype = request.POST.get('dvehicletype')
        dvehicle = request.POST.get('dvehicle')
        ddate = request.POST.get('ddate')
        dbio = request.POST.get('dbio')
        profile_photo = request.FILES.get('profile_photo')

        role = CustomUser.DRIVER
        print(role)

        if CustomUser.objects.filter(email=email, role=CustomUser.DRIVER).exists():
            messages.info(request, 'Email already exists')
            return redirect('adddriver')
        else:
            user = CustomUser.objects.create_user(email=email, password=password, name=name)
            user.role = CustomUser.DRIVER
            user.save()

            dri = Driver.objects.create(
                user=user, name=name, email=email, dgender=dgender, daddress=daddress, dage=dage, ddis=ddis,
                dtaluk=dtaluk, dPanchayat=dpanchayat, dwardno=dwardno, dpin=dpin, dphone=dphone,
                dbio=dbio, dlisence=dlisence,dvehicle=dvehicle, dvehicletype=dvehicletype,ddate=ddate, profile_photo=profile_photo
            )

            return redirect('driver')
    else:
        return render(request, 'admintemp/adddriver.html')

def driver(request):
    drivers = Driver.objects.filter(is_active=True)
    return render(request, 'admintemp/driver.html', {'drivers': drivers})

@never_cache
@login_required
def mleave(request):
    today = date.today()
    profile = Member.objects.get(user=request.user)
    absent_members = WardAttendance.objects.filter(member=profile, is_present='absent')

    for absent_member in absent_members:
        # Debugging information
        print(f"Member: {absent_member.member.Name}, Leave Applied: {absent_member.leave_applied}")

    return render(request, 'membertemp/mleave.html', {'absent_members': absent_members, 'today': today})
@never_cache
@login_required
def apply_leave(request, absent_member_id):
    absent_member = get_object_or_404(WardAttendance, id=absent_member_id)

    return render(request, 'membertemp/apply_leave.html', {'absent_member': absent_member})

def process_leave_application(request):
    if request.method == 'POST':
        absent_member_id = request.POST.get('absent_member_id')
        reason = request.POST.get('reason')

        # Get the absent_member instance
        absent_member = get_object_or_404(WardAttendance, id=absent_member_id)

        # Update the reason field and set leave_applied to True
        absent_member.reason = reason
        absent_member.leave_applied = True
        absent_member.save()

        # Add more logic based on your application requirements

        return redirect('mleave')  # Redirect back to the main leave page

    return render(request, 'membertemp/mleave.html')  # Redirect to mleave page if the request method is not POST
# views.py
def grant_certification(request, absent_member_id):
    absent_member = get_object_or_404(WardAttendance, id=absent_member_id)
    if request.method == 'POST':
        absent_member.is_grant = WardAttendance.GRANT  # Set it to 'grant'
        absent_member.save()
    return redirect('admleaveapply')
@never_cache
@login_required
def admleaveapply(request):
    absent_members = WardAttendance.objects.filter(leave_applied=True)
    return render(request, 'admintemp/admleaveapply.html', {'absent_members': absent_members})

# def adaddmachinery(request):
    # views.py
from .models import AddMachinery
@never_cache
@login_required
def adaddmachinery(request):
    if request.method == 'POST':
        machinery_photo = request.FILES.get('machinery_photo')
        mname = request.POST.get('mname')
        count = request.POST.get('count')
        price = request.POST.get('price')
        days = request.POST.get('days')

        # Validate and save the data
        if machinery_photo and mname and count and price and days:
            machinery = AddMachinery(
                machinery_photo=machinery_photo,
                mname=mname,
                count=count,
                price=price,
                days=days
            )
            machinery.save()
            return redirect('admachinery')  # Redirect to a success page or wherever you want

    return render(request, 'admintemp/adaddmachinery.html')
@never_cache
@login_required
def admachinery(request):
    machineries = AddMachinery.objects.filter(is_active = True)
    return render(request, 'admintemp/admachinery.html', {'machineries': machineries})
@never_cache
@login_required
def edit_machinery(request, machineries_id):
    machinery = get_object_or_404(AddMachinery, id=machineries_id)

    if request.method == 'POST':
        mname = request.POST.get('mname')
        count = request.POST.get('count')
        price = request.POST.get('price')
        days = request.POST.get('days')
        machinery_photo = request.FILES.get('machinery_photo')

        # Update other fields
        machinery.mname = mname
        machinery.price = price
        machinery.days = days
        machinery.count = count

        # Update machinery_photo only if a new file is provided
        if machinery_photo:
            machinery.machinery_photo = machinery_photo

        machinery.save()
        return redirect('admachinery')

    return render(request, 'admintemp/edit_machinery.html', {'machinery': machinery})

def delete_machinery(request, machineries_id):
    machinery = get_object_or_404(AddMachinery, id=machineries_id)

    if request.method == 'POST':
        # Delete the member object
        machinery.is_active = False
        machinery.save()
        request.session['delete mem'] = True
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('admachinery')

    return render(request, 'admintemp/delete_machinery.html', {'machinery': machinery})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AddMachinery
from .models import FarmerProfile, AddMachinery
from datetime import timedelta

from django.urls import reverse
from .models import AddMachinery, FarmerProfile
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import AddMachinery, MachineryApplication
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from .models import AddMachinery, MachineryApplication
@never_cache
@login_required
def machinery(request):
    machineries = AddMachinery.objects.filter(is_active=True)
    # applications = MachineryApplication.objects.filter(farmer_profile__user=request.user)

    # if request.method == 'POST':
    #     machinery_id = request.POST.get('machinery_id')
    #     machinery = get_object_or_404(AddMachinery, id=machinery_id)

    #     # Assuming the current user is the applying farmer
    #     farmer_profile = FarmerProfile.objects.get(user=request.user)

    #     # Get apply_date and acount from the form data
    #     apply_date = request.POST.get('apply_date')
    #     acount = int(request.POST.get('acount'))

    #     # Convert apply_date to a datetime object
    #     apply_date = datetime.strptime(apply_date, '%Y-%m-%d').date()

    #     # Calculate total_days
    #     total_days = apply_date + timedelta(days=machinery.days)

    #     # Create a new application with apply_date, total_days, and acount
    #     application = MachineryApplication.objects.create(
    #         machinery=machinery,
    #         farmer_profile=farmer_profile,
    #         farmerName=farmer_profile.first_name,
    #         address=farmer_profile.address,
    #         wardNo=farmer_profile.ward,
    #         apply_date=apply_date,
    #         total_days=total_days,
    #         acount=acount,
    #         Tcount=machinery.count - acount  # Subtract acount from the count
    #     )

    #     # Redirect to the same page after applying to prevent form resubmission
    #     return HttpResponseRedirect(reverse('machinery'))

    return render(request, 'machinery.html', {'machineries': machineries})

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from .models import AddMachinery, MachineryApplication

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import AddMachinery, MachineryApplication, FarmerProfile
from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from .models import AddMachinery, MachineryApplication, FarmerProfile
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AddMachinery, FarmerProfile, MachineryApplication
from django.db import transaction
from django.db.models import F
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from django.db import transaction
from .models import AddMachinery, FarmerProfile, MachineryApplication, MachineryTcount
from datetime import datetime, timedelta
@transaction.atomic
def mapply(request, machinery_id):
    machinery = get_object_or_404(AddMachinery, id=machinery_id)
    farmer_profile = FarmerProfile.objects.get(user=request.user)
    
    # Check if the farmer has already applied for this machinery and if the total_days have passed
    previous_application = MachineryApplication.objects.filter(
        farmer_profile=farmer_profile,
        machinery=machinery,
        total_days__gte=timezone.now().date()  # Check if total_days is greater than or equal to today
    ).first()
    
    if previous_application:
        # Redirect or show an error message indicating that the farmer cannot apply again yet
        return render(request, 'error.html', {'message': "You cannot apply for this machinery until the previous application's total_days have passed.", 'total_days': previous_application.total_days})

    if request.method == 'POST':
        apply_date = request.POST.get('apply_date')
        acount = int(request.POST.get('acount'))
        file_upload = request.FILES.get('file_upload')  # Get the uploaded file
        
        apply_date = datetime.strptime(apply_date, '%Y-%m-%d').date()
        total_days = apply_date + timedelta(days=machinery.days)
        
        # Calculate the total price based on the account count
        total_price = machinery.price * acount
        
        # Get or create MachineryTcount instance based on mname
        tcount_instance, created = MachineryTcount.objects.get_or_create(mname=machinery.mname, defaults={'count': machinery.count})
        
        Tcount = tcount_instance.count
        
        # Calculate updated Tcount value
        updated_Tcount = Tcount - acount
        
        # Update the total count in MachineryTcount using F() expression
        tcount_instance.count = F('count') - acount
        tcount_instance.save()
        
        # Create a new MachineryApplication instance with updated Tcount
        application = MachineryApplication.objects.create(
            machinery=machinery,
            farmer_profile=farmer_profile,
            farmerName=farmer_profile.first_name,
            address=farmer_profile.address,
            wardNo=farmer_profile.ward,
            apply_date=apply_date,
            total_days=total_days,
            acount=acount,
            Tcount=updated_Tcount,  # Use updated_Tcount here
            file_upload=file_upload,  # Save the uploaded file
            total_price=total_price  # Save the calculated total price
        )

        # Check if total_days is today's date
        if total_days == timezone.now().date():
            # Increase Tcount based on acount
            tcount_instance.count = F('count') + acount
            tcount_instance.save()
        
        # Redirect to the confirmation page with machinery and application IDs
        return redirect('payment', machinery_id=machinery_id, application_id=application.id)

    return render(request, 'mapply.html', {'machinery': machinery, 'farmer_profile': farmer_profile})
@never_cache
@login_required
def mmachinery(request):
    machineries = AddMachinery.objects.filter(is_active=True)
    return render(request, 'membertemp/mmachinery.html', {'machineries': machineries})
def mapplications(request):
    user = request.user
    profile = Member.objects.get(user=user)
    applications = MachineryApplication.objects.filter(wardNo=profile.wardno)
    return render(request, 'membertemp/mapplications.html', {'applications': applications})
from django.shortcuts import render
from .models import MachineryApplication
@never_cache
@login_required
def applied_machineries(request):
    # Fetch applied machinery details for the logged-in user
    applied_machineries = MachineryApplication.objects.filter(farmer_profile=request.user.farmerprofile)

    return render(request, 'applied_machineries.html', {'applied_machineries': applied_machineries})
def applied_machineries_admin(request):
    # Fetch all applied machinery details
    applied_machineries = MachineryApplication.objects.all()

    return render(request, 'admintemp/applied_machineries_admin.html', {'applied_machineries': applied_machineries})

# def confirm_machinery(request):
#     # Retrieve the latest MachineryApplication instance
#     latest_application = MachineryApplication.objects.latest('id')
    
#     context = {
#         'farmer_profile': latest_application.farmer_profile,
#         'machinery': latest_application.machinery,
#         'acount': latest_application.acount,
#         'total_price': latest_application.total_price,
#     }
    
#     return render(request, 'confirm_machinery.html', context)

# def mapply(request,machinery_id):
#     machinery = get_object_or_404(AddMachinery, id=machinery_id)
#     applications = MachineryApplication.objects.filter(farmer_profile__user=request.user)

#     if request.method == 'POST':
#         machinery_id = request.POST.get('machinery_id')
#         machinery = get_object_or_404(AddMachinery, id=machinery_id)

#         # Assuming the current user is the applying farmer
#         farmer_profile = FarmerProfile.objects.get(user=request.user)

#         # Get apply_date and acount from the form data
#         apply_date = request.POST.get('apply_date')
#         acount = int(request.POST.get('acount'))

#         # Convert apply_date to a datetime object
#         apply_date = datetime.strptime(apply_date, '%Y-%m-%d').date()

#         # Calculate total_days
#         total_days = apply_date + timedelta(days=machinery.days)

#         # Create a new application with apply_date, total_days, and acount
#         application = MachineryApplication.objects.create(
#             machinery=machinery,
#             farmer_profile=farmer_profile,
#             farmerName=farmer_profile.first_name,
#             address=farmer_profile.address,
#             wardNo=farmer_profile.ward,
#             apply_date=apply_date,
#             total_days=total_days,
#             acount=acount,
#             Tcount=machinery.count - acount  # Subtract acount from the count
#         )

#         # Redirect to the same page after applying to prevent form resubmission
#         return HttpResponseRedirect(reverse('mapply'))

#     return render(request, 'mapply.html', {'machinery': machinery, 'applications': applications})

@login_required
def mark_notification_as_read(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        Notification.objects.filter(id=notification_id, user=request.user).update(is_read=True)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user, is_read=False)

    context = {
        'notifications': [{'id': n.id, 'title': n.title, 'message': n.message} for n in notifications],
        'notification_count': notifications.count()
    }

    return JsonResponse(context)


from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .models import Payment, MachineryApplication

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal
from .models import Payment, MachineryApplication
from razorpay.errors import SignatureVerificationError


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def payment(request, machinery_id, application_id):
    # Retrieve machinery and application objects
    machinery = get_object_or_404(AddMachinery, id=machinery_id)
    application = get_object_or_404(MachineryApplication, id=application_id)

    # Create a Razorpay Order
    currency = 'INR'
    amount = float(application.total_price) * 100  # Convert to float and then to paise
    razorpay_order = razorpay_client.order.create(dict(
        amount=amount,
        currency=currency,
        payment_capture='0'
    ))

    # Create a Payment object for tracking
    payment = Payment.objects.create(
        user=request.user,
        razorpay_order_id=razorpay_order['id'],
        payment_id="",
        amount=float(application.total_price),  # Convert to float
        currency=currency,
        payment_status=Payment.PaymentStatusChoices.PENDING,
        MachineryApplication=application
    )

    # Prepare context for rendering the confirmation page
    context = {
        'user': request.user,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'amount': float(application.total_price) / 100,  # Convert to float
        'callback_url': '/paymenthandler/',
        'machinery': machinery,
        'application': application,
    }

    return render(request, 'confirm_machinery.html', context)

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        # Verify the payment signature
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)

        if result:
            amount = int(float(payment.amount) * 100)  # Convert to float and then to paise
            # Capture the payment
            razorpay_client.payment.capture(payment_id, amount)

            # Update the order with payment ID and change status to "Successful"
            payment.payment_id = payment_id
            payment.payment_status = Payment.PaymentStatusChoices.SUCCESSFUL
            payment.save()

            # Render success page on successful capture of payment
            return render(request, 'homepage.html')
        else:
            # If signature verification fails
            payment.payment_status = Payment.PaymentStatusChoices.FAILED
            payment.save()
            return render(request, 'paymentfail.html', {'error': 'Signature verification failed'})
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')

def all_report(request):
    return render(request,'admintemp/all_report.html')


# def see_attendance(request):
#     return render(request,'admintemp/see_attendance.html')
# def see_attendance2(request, meeting_id):
#     meeting = Meeting.objects.get(id=meeting_id)
#     return render(request, 'admintemp/see_attendance2.html', {'meeting': meeting})
def generate_pdf_adselldetails(request):
    template_path = 'admintemp/generate_pdf_adselldetails.html'
    context = {
        'confirmed_data': Sellapply.objects.filter(is_confirmed=True),
    }
    # Render template
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="generate_pdf_adselldetails.pdf"'

    # Enable debugging
    pisa.showLogging()

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')

    return response
