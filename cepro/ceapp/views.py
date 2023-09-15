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
from django.core.files.storage import FileSystemStorage
from datetime import date



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
        # name = request.POST['name']
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
                user = CustomUser.objects.create_user(email=email, password=password, role=role)
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
    return render(request,'homepage.html')

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
    return render(request,'admintemp/adindex.html')
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



def mindex(request):
    return render(request,'membertemp/mindex.html')
def mblog(request):
    return render(request,'membertemp/mblog.html')
# def mcrop(request):
#     return render(request,'membertemp/mcrop.html')
def mappointment(request):
    return render(request,'membertemp/mappointment.html')
def mcalendar(request):
    return render(request,'membertemp/mcalendar.html')
def meditprofile(request):
    return render(request,'membertemp/meditprofile.html')


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
    members = Member.objects.all()
    return render(request, 'admintemp/admember.html', {'members': members})
def adaddmember(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dis = request.POST.get('dis', 'Default District')  # Set a default value for District
        taluk = request.POST.get('taluk', 'Default Taluk')   # Set a default value for Taluk
        panchayat = request.POST.get('panchayat', 'Default Panchayat')  # Set a default value for Panchayat
        ward = request.POST.get('ward')
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        
        role=CustomUser.MEMBER

        profile_photo = request.FILES.get('profile_photo')

        member=Member()
        user = CustomUser()
        member.Name = name
        member.email = email
        member.set_password(password)
        member.date_of_birth = date_of_birth
        # member.gender = gender
        member.address = address
        member.district = dis
        member.taluk = taluk
        member.Panchayat = panchayat
        member.ward = ward
        member.postal = pin
        member.phone = phone
        member.bio = bio


        user.email=email
        user.set_password(password)
        user.role=role
        if profile_photo:
            # Save the profile photo to a specific directory
            fs = FileSystemStorage()
            filename = fs.save(f"profile_photos/{profile_photo.name}", profile_photo)
            member.profile_photo = filename  # Associate profile photo if uploaded

        # if profile_photo:
        #     # Save the profile photo to a specific directory
        #     fs = FileSystemStorage()
        #     filename = fs.save(f"profile_photos/{profile_photo.name}", profile_photo)
        #     member.profile_photo = filename 
        #     # Associate profile photo if uploaded
        #     # Save the updated member object
        member.save()
        user.save()
        return redirect('admember')

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

        # Update the member's attributes with the new data
        member.Name = name
        member.email = email
        member.date_of_birth = dob
        # member.gender = gender
        member.address = address
        member.district = district
        member.taluk = taluk
        member.Panchayat = panchayat
        member.ward = ward
        member.postal = postal
        member.phone = phone
        member.bio = bio

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
        member.delete()
        
        # Redirect to a page after deleting the member (e.g., member list)
        return redirect('admember')

    return render(request, 'admintemp/delete_member.html', {'member': member})

# def cprofile(request):
#     return render(request, 'cprofile.html')
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
        profile.email = request.POST.get('email')
        print("email name :",profile.email)

        profile.gender = request.POST.get('gender')
        print("gender :",profile.gender)

        profile.house_name = request.POST.get('house_name')
        print("house name :",profile.house_name)

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

       
        profile.save()
        
            

        # messages.success(request, 'Profile updated successfully.')
        return redirect('ceditprofile')  # Redirect to the profile page
    context = {
        'user': user,
        'profile': profile
    }

    return render(request, 'ceditprofile.html',context)





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
        new_crop = Crop(Namec=cname, des=cdescription, start_date = start_date ,end_date = end_date, count=count ,current=True)
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

        # Check the value of 'availability' to determine the selected option
        availability = request.POST.get('availability')
        if availability == '1':
            avail = True
            notavail = False
        else:
            avail = False
            notavail = True

        # Update the member's attributes with the new data
        crop.Namec = cname
        crop.des = details
        crop.available = avail
        crop.notavailable = notavail

        # Save the updated member object
        crop.save()

        # Redirect to the member list page after editing
        return redirect('adcrop')

    return render(request, 'admintemp/edit_crop.html', {'crop': crop})

def mcrop(request):
    crops = Crop.objects.all()  # Retrieve all crops from the database
    return render(request, 'membertemp/mcrop.html', {'crops': crops})



def crop(request):
    today = date.today()
    # Retrieve the currently added crop
    # current_crop = Crop.objects.filter(current=True).first()
    crops = Crop.objects.all() 
    # for crop in crops:
    #     print(f"Today: {today}, Start Date: {crop.start_date}, End Date: {crop.end_date}")
    return render(request, 'crop.html', {'crops': crops , 'today': today})
#application for crops 


    
  





# def crop(request):
#     crops = Crop.objects.all()  # Retrieve all crops from the database
#     return render(request, 'crop.html', {'crops': crops})

def disapply(request):
    applys = ApplyCrop.objects.all()
    return render(request, 'disapply.html', {'applys': applys})
from django.contrib.auth.decorators import login_required

@login_required
def apply(request):
    existing_certification = ApplyCrop.objects.filter(user=request.user).first()
    if existing_certification:
        return render(request, 'apply.html', {'existing_certification': existing_certification})
    
    crop_name = request.GET.get('crop_name')
    
    if request.method == 'POST':
        
    #    cname = request.POST.get('cname')
        farmerName = request.POST.get('farmerName')
        address = request.POST.get('address')
        contactNo = request.POST.get('contactNo')
        wardNo  = request.POST.get('wardNo')
        annualIncome  = request.POST.get('annualIncome')

        

        obj = ApplyCrop()
        obj.user = request.user
        obj.cname = crop_name
        obj.farmerName = farmerName
        obj.address = address
        obj.contactNo= contactNo
        obj.wardNo = wardNo
        obj.AnnualIncome = annualIncome
        obj.save()

        
        return redirect('apply')

    return render(request, 'apply.html', {
    'crop_name': crop_name,
    'existing_certification': existing_certification,
     
    })
    

        
 


    

# def disapply(request):
#     # Retrieve details from the database
#     details = ApplyCrop.objects.all()  # You might need to filter this based on your requirements

#     # Pass the details to the template
#     return render(request, 'crop.html', {'details': details})


# views.py
from django.shortcuts import render
from .models import ApplyCrop  # Import your model

def mfregistered(request):
    pending_details = ApplyCrop.objects.all()
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


def approve_acertification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = ApplyCrop.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('adpendingapproval')

def reject_acertification(request, certification_id):
    certification = get_object_or_404(ApplyCrop, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = ApplyCrop.REJECTED  # Set it to 'rejected'
        certification.save()
    return redirect('adpendingapproval')

def mapprove(request):
    pending_details = ApplyCrop.objects.filter(is_approved='approved')  # Adjust the filter condition as needed

    # Pass the data to the template
    context = {'pending_details': pending_details}

    return render(request, 'membertemp/mapprove.html', context)
    
# user.role == CustomUser.MEMBER:
# def mapprove(request):
#     pending_details = ApplyCrop.objects.filter(approved=False)
#     return render(request, 'membertemp/mapprove.html', {'details': pending_details})

def adpendingapproval(request):
    pending_details = ApplyCrop.objects.filter(is_approved='approved')  # Adjust the filter condition as needed
    user_roles = {}
    for application in pending_details:
        # Ensure the user associated with the Certification exists
        user = get_object_or_404(CustomUser, id=application.user_id)

        # Retrieve user roles
        user_roles[application.id] = {
            'is_admin': user.is_superuser,
            # 'is_member': user.role == CustomUser.MEMBER,
            'is_farmer': user.role == CustomUser.FARMER,
            # 'is_seller': user.is_staff
        }

    context = {
        'pending_details': pending_details,
        'user_roles': user_roles,  # Include user roles in the context
    }
    return render(request, 'admintemp/adpendingapproval.html', context)


def adapproval(request):
    pending_details = ApplyCrop.objects.filter(is_approved='approved')  # Adjust the filter condition as needed

    # Pass the data to the template
    context = {'pending_details': pending_details}

    return render(request, 'admintemp/adapproval.html', context)
    

    # details = ApplyCrop.objects.all()
    # return render(request, 'admintemp/adpendingapproval.html', {'details': details})



# def mfregistered(request):
#     details = ApplyCrop.objects.all()
#     return render(request,'membertemp/mfregistered.html',{details : details})