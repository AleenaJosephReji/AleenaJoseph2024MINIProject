from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from .CustomUser import CustomUser  # Assuming CustomUser is in the same app

# from ceapp.CustomUser import CustomUser  # Replace "myapp" with the actual app name

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
   
    def create_user(self, email, password=None, role=None):
        if not email:
         raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
              # Set the role here
    )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):
        
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
             # Set the role here

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.role=3
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    FARMER = 1
    MEMBER = 2
    ADMIN = 3

    ROLE_CHOICE = (
        (FARMER, 'FARMER'),
        (MEMBER, 'MEMBER'),
        (ADMIN,'ADMIN'),
    
    )

    username=models.CharField(null=True,max_length=120)
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')


    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = []

    objects = UserManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# Create your models here.
class Member(models.Model): 
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    admin_set_password = models.CharField(max_length=128, blank=True, null=True)

    def set_password(self, password):
        # Hash and set the password
        self.admin_set_password = make_password(password)



    date_of_birth = models.CharField(max_length=100,null=True, blank=True)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    district= models.CharField(max_length=100,null=True, blank=True)
    taluk = models.CharField(max_length=255, null=True, blank=True)
    Panchayat = models.CharField(max_length=100,null=True, blank=True)
    ward = models.CharField(max_length=100,null=True, blank=True)
    postal = models.IntegerField()
    phone = models.IntegerField()
    bio=models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    def __str__(self):
        return self.email
# class Crop(models.Model):
#     Namec = models.CharField(max_length=100)
#     des = models.TextField()
#     available = models.BooleanField(default=False)
#     not_available = models.BooleanField(default=False)

class Crop(models.Model):
    Namec = models.CharField(max_length=100)
    des = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    count = models.CharField(max_length=100,null=True, blank=True)


    # available = models.BooleanField(default=False)
    # not_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=False)




class Blog(models.Model):
    blogname = models.CharField(max_length=100)
    blogcategory = models.CharField(max_length=100)
    blogdes = models.TextField()
    blogimage =  models.ImageField(upload_to='blog/', null=True, blank=True)

# models.py


# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)


class ApplyCrop(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'
    
    APPROVAL_CHOICES = [
    (APPROVED, 'Approved'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,default=1)
    cname = models.CharField(max_length=100,null=True, blank=True)
    farmerName = models.CharField(max_length=100,null=True, blank=True)
    address = models .CharField(max_length=100,null=True,blank=True)
    contactNo = models .CharField(max_length=100,null=True,blank=True)
    wardNo = models .CharField(max_length=100,null=True,blank=True)
    AnnualIncome = models .IntegerField(null=True,blank=True)
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )

    # approved = models.BooleanField(default=False)







class FarmerProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    # birth_date = models.DateField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    house_name = models.CharField(max_length=100, null=True,blank=True)
    house_no = models.IntegerField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    ward = models.CharField(max_length=100)
    pin_code = models.IntegerField(max_length=6,null=True,blank=True)
    phone_number = models.IntegerField(max_length=12,null=True,blank=True)
    
    # current_diagnosis = models.CharField(max_length=100, null=True,blank=True)
    # past_med_condition = models.CharField(max_length=100, null=True,blank=True)
    # surgical_history = models.CharField(max_length=100, null=True,blank=True)
    
    # allergies = models.CharField(max_length=100, null=True,blank=True)
    # height = models.IntegerField(max_length=100, null=True,blank=True)
    # weight = models.IntegerField(max_length=100, null=True,blank=True)
    # bmi = models.IntegerField(max_length=100, null=True,blank=True)
    # medication_names = models.CharField(max_length=100, null=True,blank=True)
    # dosage = models.CharField(max_length=12,null=True,blank=True)
    # frequency = models.CharField(max_length=12,null=True,blank=True)
    
    def _str_(self):
        return self.first_name


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     # mobile = models.CharField(max_length=15)
#     # profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     # address = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name






