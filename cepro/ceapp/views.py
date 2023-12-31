from django.shortcuts import render,redirect, get_list_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from .models import Member
from .models import Crop
from .models import Blog
from .models import ApplyCrop
from .models import CustomUser
from .models import FarmerProfile
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
    
def index(request):
    return render(request,'index.html')

# def home1(request):
#     return render(request,'home1.html')
# def service(request):
    # return render(request,'service.html')
# def about(request):
    # return render(request,'about.html')
# def testimonail(request):
    # return render(request,'testimonail.html')

# def blog(request):
    # return render(request,'blog.html')

# def contact(request):
    # return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

# def shop(request):
#     return render(request,'shop.html')

# def cart(request):
#     return render(request,'cart.html')

# def checkout(request):
#     return render(request,'checkout.html')

# def wishlist(request):
#     return render(request,'wishlist.html')
# def gallery(request):
#     return render(request,'gallery.html')
def homepage(request):
    user = request.user
    profile = FarmerProfile.objects.get(user=user)
    return render(request,'homepage.html',{'profile':profile})

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
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return render(request,'product.html')
def apply(request):
    return render(request,'apply.html')
# def crop(request):
#     return render(request,'crop.html')



# def index2(request):
#     return render(request,'Atemp/index2.html')
# def aindex2(request):
#     return render(request,'Atemp/aindex2.html')

def adindex(request):
    me = Member.objects.all()
    me_count = me.count()
    c=Crop.objects.all()
    c_count=c.count()
    crops = Crop.objects.all()
    approval = ApplyCrop.objects.all()
    approval_count = approval.count()
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
# def mcrop(request):
#     return render(request,'membertemp/mcrop.html')
def mappointment(request):
    return render(request,'membertemp/mappointment.html')
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
    blogs = Blog.objects.all()
    context={
        'blogs' : blogs,
    }
    return render(request, 'admintemp/adblog.html',context)
def adaddblog(request):
    if request.method == 'POST':
        blogname = request.POST.get('blogname')
        blogcategory = request.POST.get('blogcategory')
        blogdes = request.POST.get('blogdes')
        blogimage  = request.POST.get('blogimage')

        obj = Blog()
        obj.blogname = blogname
        obj.blogcategory = blogcategory
        obj.blogdes = blogdes
        obj.blogimage = blogimage
        obj.save()


        # You can use messages and redirection if needed
        # messages.success(request, 'Asha Worker created successfully!')
        return redirect('adblog')

    return render(request, 'admintemp/adaddblog.html')

 # Import a form for editing member details if you have one


from django.shortcuts import render, redirect
from .models import Crop  # Import your Crop model
def admember(request):
    members = Member.objects.filter(is_active=True)
    return render(request, 'admintemp/admember.html', {'members': members})
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

def fmyprofile(request):
    profile = FarmerProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'fmyprofile.html', context)

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



# def adeditprofile(request):
    
#     user = request.user
#     adprofile = FarmerProfile.objects.get(user=user)
    
#     if request.method == "POST":
#         print ('POST')
#         # user.first_name=request.POST.get('first_name')
#         # user.last_name=request.POST.get('last_name')
#         # Process the form data and save/update the profile

#         adprofile.first_name = request.POST.get('first_name')
#         print("first name :",adprofile.first_name)
#         adprofile.last_name = request.POST.get('last_name')
#         print("last name :",adprofile.last_name)
        
#         # profile.birth_date = request.POST.get('birth_date')
#         # print("Date of Birth :",profile.birth_date)
     
#         adprofile.email = request.POST.get('email')
#         print("email name :",adprofile.email)

        
#         adprofile.gender = request.POST.get('gender')
#         print("gender :",adprofile.gender)

#         # profile.house_name = request.POST.get('house_name')
#         # print("house name :",profile.house_name)

#         adprofile.house_no = request.POST.get('house_no')
#         print("house no :",adprofile.house_no)

#         adprofile.address = request.POST.get('address')
#         print("adsress :",adprofile.address)

#         adprofile.ward = request.POST.get('ward')
#         print("ward :",adprofile.ward)

#         adprofile.pin_code = request.POST.get('pin_code')
#         print("pin code :",adprofile.pin_code)

#         adprofile.phone_number = request.POST.get('phone_number')
#         print("phone :",adprofile.phone_number)

#         # profile.phone_number = request.POST.get('phone_number')
#         profile.fprofile_photo = request.FILES.get('fprofile_photo')
#         print("phone :",profile.fprofile_photo)

#         profile.save()
        
            

#         # messages.success(request, 'Profile updated successfully.')
#         return redirect('adeditprofile')  # Redirect to the profile page
#     context = {
#         'user': user,
#         'profile': profile
#     }

#     return render(request, 'ceditprofile.html',context)


from django.contrib.auth import update_session_auth_hash
# @login_required(login_url='login_page')
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

# add_crop

from django.shortcuts import render, redirect
from .models import Crop 
# from .models import Notification 

 # Import your Crop model

def adcrop(request):
    crops = Crop.objects.all()
    return render(request, 'admintemp/adcrop.html', {'crops': crops})


# def adaddcrop(request):
#     if request.method == 'POST':
#         cname = request.POST.get('cname')
#         cdescription = request.POST.get('cdescription')
        
#         # Check if the "available" form field was submitted and set it to True or False accordingly
#         available = request.POST.get('cavailability')
#         if available == 'Available':
#             avail = True
#         else:
#             avail = False

#         # Create a new Crop instance with the provided data
#         new_crop = Crop(Namec=cname, des=cdescription, available=avail)
#         new_crop.save()

#         # Redirect to the appropriate page after adding the new crop
#         return redirect('adcrop')

#     return render(request, 'admintemp/adaddcrop.html')



from django.db.models import Max
def adaddcrop(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cdescription = request.POST.get('cdescription')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        count = request.POST.get('count')
        crop_photo = request.FILES.get('crop_photo')


        # available = request.POST.get('available')
        # notavail = request.POST.get('notavailable')
        
        # Determine the availability based on user input
        # if available == 'Available':
        #     avail = True
        #     notavail = False
        # else:
        #     avail = False
        #     notavail = True

        # Create a new Crop instance with the provided data
        existing_crop = Crop.objects.filter(Namec=cname).first()
        if existing_crop:
            messages.error(request, f'A crop with the name "{cname}" already exists.')
            return redirect('adaddcrop')
        new_crop = Crop(Namec=cname, des=cdescription, start_date = start_date ,end_date = end_date, count=count, crop_photo=crop_photo ,current=True)
        new_crop.save()

        # Set current to False for all other crops
        Crop.objects.exclude(id=new_crop.id).update(current=False)

        # Redirect to the appropriate page after adding the new crop
        return redirect('adcrop')

    return render(request, 'admintemp/adaddcrop.html')


# def adaddcrop(request):
#     if request.method == 'POST':
#         cname = request.POST.get('cname')
#         cdescription = request.POST.get('cdescription')
#         avail = request.POST.get('available') == 'on'  
#         notavail = request.POST.get('notavailable') == 'on'  

#         obj = Crop(Namec=cname, des=cdescription, available=avail, not_available=notavail)
#         obj.save()
#         return redirect('adcrop') 

#     return render(request,'admintemp/adaddcrop.html')  





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







#crop

def delete_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)

    if request.method == 'POST':
        # Delete the member object
        crop.delete()
        
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('adcrop')

    return render(request, 'admintemp/delete_crop.html', {'crop': crop})
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

def mcrop(request):
    crops = Crop.objects.all()  # Retrieve all crops from the database
    return render(request, 'membertemp/mcrop.html', {'crops': crops})



def crop(request):
    user = request.user
    profile = FarmerProfile.objects.get(user=user)
    today = date.today()
    # Retrieve the currently added crop
    # current_crop = Crop.objects.filter(current=True).first()
    crops = Crop.objects.all() 
    # for crop in crops:
    #     print(f"Today: {today}, Start Date: {crop.start_date}, End Date: {crop.end_date}")
    return render(request, 'crop.html', {'crops': crops , 'today': today ,'profile' : profile})
#application for crops 


    
  





# def crop(request):
#     crops = Crop.objects.all()  # Retrieve all crops from the database
#     return render(request, 'crop.html', {'crops': crops})

def disapply(request):
    applys = ApplyCrop.objects.all()
    return render(request, 'disapply.html', {'applys': applys})

from django.contrib.auth.decorators import login_required
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

def adpendingapproval(request):
    # Retrieve the approved details from your model or database
    approved_details = ApplyCrop.objects.filter(is_approved='approved')

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


#search
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


def adattendance(request):
    if request.method == 'POST':
        selected_wards = request.POST.getlist('ward')
        meeting_id = request.POST.get('meeting_id')

        # Iterate through selected wards and update attendance records
        for ward in selected_wards:
            # Check if an attendance record for the person and meeting already exists
            attendance, created = WardAttendance.objects.get_or_create(
                meeting_id=meeting_id,
                person_id=ward,
            )
            
            # Update the 'attended' field to True
            attendance.attended = True
            attendance.save()

        # Redirect to the attendance page or another appropriate URL
        return redirect('adattendance')  # Replace 'attendance-success' with the actual URL

    # If the request method is not POST, render the page with all meetings.
    meetings = Meeting.objects.all()
    return render(request, 'admintemp/adattendance.html', {'meetings': meetings})


def adaddattendance(request):
    members = Member.objects.filter(is_active=True)
    attendance_records = WardAttendance.objects.all()  # Retrieve attendance records
    member_data = {}

    for member in members:
        attendance_record = attendance_records.filter(member=member).first()
        
        if attendance_record:
            # If the member is in attendance records, set the value to is_present
            member_data[member.id] = {
            'is_present': attendance_record.is_present,  # Replace with the actual field name
            'Name': member.Name,  # Replace with actual field names
            # Add other fields as needed
            }  # Replace with the actual field name
        else:
            # Member is not in attendance records, set the value to 'pending'
            member_data[member.id] = {
            'is_present': 'pending',  # Replace with the actual field name
            'Name': member.Name,  # Replace with actual field names
            # Add other fields as needed
            }
    print(member_data.items())
    return render(request, 'admintemp/adaddattendance.html', {'members': member_data, 'attendance_records': attendance_records})


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

def mark_attendance(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        attendance_status = request.POST.get('attendance_status')
        
        print(f"Member ID: {member_id}, Attendance Status: {attendance_status}")
        obj,created = WardAttendance.objects.update_or_create(member_id=member_id,is_present=attendance_status)
        print(obj)
        # ... (update the model)
    return redirect('adaddattendance')


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

def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        meeting_venue = request.POST.get('meeting_venue')
        meeting_agenda = request.POST.get('meeting_agenda')
        desmeeting = request.POST.get('desmeeting')
        report = request.POST.get('report')
        meeting.meeting_date = meeting_date
        meeting.meeting_time = meeting_time
        meeting.meeting_venue = meeting_venue
        meeting.meeting_agenda = meeting_agenda
        meeting.desmeeting = desmeeting
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

#graph

# views.py
# from django.shortcuts import render
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64

# from .models import Crop

# def crop_graph(request):
#     crops = Crop.objects.all()
#     crop_names = [crop.Namec for crop in crops]
#     crop_counts = [crop.count for crop in crops]

#     plt.figure(figsize=(10, 6))
#     plt.bar(crop_names, crop_counts)
#     plt.xlabel('Crop Name')
#     plt.ylabel('Crop Count')
#     plt.title('Crop Count Distribution')

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     plt.close()
#     buffer.seek(0)

#     image_png = buffer.getvalue()
#     buffer.close()
#     graph = base64.b64encode(image_png).decode()

#     return render(request, 'admintemp/adindex.html', {'graph': graph})
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