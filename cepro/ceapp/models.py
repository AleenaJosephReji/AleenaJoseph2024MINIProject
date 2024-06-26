from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# from .CustomUser import CustomUser  # Assuming CustomUser is in the same app

# from ceapp.CustomUser import CustomUser  # Replace "myapp" with the actual app name

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
   
    def create_user(self, name, email, password=None, role=None):
        if not email:
         raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            role=role,
              # Set the role here
    )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,name, email, password=None):
        
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
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
    DRIVER = 4
    ROLE_CHOICE = (
        (FARMER, 'FARMER'),
        (MEMBER, 'MEMBER'),
        (ADMIN,'ADMIN'),
        (DRIVER,'DRIVER'),
    
    )

    username=models.CharField(null=True,max_length=120)
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    name=models.CharField(max_length=50)
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
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    admin_set_password = models.CharField(max_length=128, blank=True, null=True)

    def set_password(self, password):
        # Hash and set the password
        self.admin_set_password = make_password(password)



    dob = models.CharField(max_length=100,null=True, blank=True)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    district= models.CharField(max_length=100,null=True, blank=True)
    taluk = models.CharField(max_length=255, null=True, blank=True)
    Panchayat = models.CharField(max_length=100,null=True, blank=True)
    wardname = models.CharField(max_length=100,null=True, blank=True)
    wardno = models.IntegerField(max_length=100,null=True, blank=True)
    postal = models.IntegerField()
    phone = models.IntegerField()
    bio=models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)


    amob = models.IntegerField(max_length=100,null=True, blank=True)
    aemail = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    institution = models.CharField(max_length=255, null=True,blank=True)
    reset_password = models.CharField(max_length=128, null=True, blank=True)  # New field for reset password


    is_active = models.BooleanField(default=True)
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
    count = models.PositiveIntegerField(default=0)
    # count = models.CharField(max_length=100,null=True, blank=True)
    crop_photo = models.ImageField(upload_to='crop_photos/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    # available = models.BooleanField(default=False)
    # not_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=False)
   




class Product(models.Model):
    blogname = models.CharField(max_length=100)
    # blogcategory = models.CharField(max_length=100)
    # blogdes = models.TextField()
    blogimage =  models.ImageField(upload_to='blog/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
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
    WAITING = 'waiting'
    
    APPROVAL_CHOICES = [
    (APPROVED, 'Approved'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending'),
    (WAITING, 'waiting'),
    ]

    WAITING = 'waiting'
    NOTWAITING = 'notwaiting'
    
    WAITING_CHOICES = [
    (WAITING,'waiting'),
    (NOTWAITING,'notwaiting'),
    ]

    GIVEN = 'given'
    NOTGIVEN = 'notgiven'
    
    IS_GIVEN = [
    (GIVEN, 'Given'),
    (NOTGIVEN, 'Notgiven'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,default=1)
    cname = models.CharField(max_length=100,null=True, blank=True)
    farmerName = models.CharField(max_length=100,null=True, blank=True)
    address = models .CharField(max_length=100,null=True,blank=True)
    contactNo = models .CharField(max_length=100,null=True,blank=True)
    wardNo = models .CharField(max_length=100,null=True,blank=True)
    AnnualIncome = models .IntegerField(null=True,blank=True)
    land = models .CharField(max_length=100,null=True,blank=True)
    crop_id=models.ForeignKey(Crop, on_delete=models.CASCADE, null=True,default=1)
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    crop_giventime = models.DateTimeField(null=True,blank=True)
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )
    is_approvedd = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )
    is_waiting = models.CharField(
        max_length=10,
        choices=WAITING_CHOICES,
        default=WAITING,
    )
    is_given = models.CharField(
        max_length=10,
        choices=IS_GIVEN,
        default=NOTGIVEN,
    )    
    # approved = models.BooleanField(default=False)

class FarmerProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    # house_name = models.CharField(max_length=100, null=True,blank=True)
    annual_income = models.IntegerField(max_length=100, null=True,blank=True)
    land = models.CharField(max_length=100, null=True,blank=True)
    house_no = models.IntegerField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.IntegerField(max_length=12,null=True,blank=True)
    ward = models.CharField(max_length=100)
    pin_code = models.IntegerField(max_length=6,null=True,blank=True)
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    fprofile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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

class Meeting(models.Model):
    meeting_date = models.DateField(null=True, blank=True)
    meeting_time = models.TimeField(null=True,blank=True)
    desmeeting = models.TextField()
    last_edited_at = models.DateTimeField(auto_now=True) 
    meeting_venue = models.CharField(max_length=100,null=True,blank=True)
    meeting_mode = models.CharField(max_length=100,null=True,blank=True)
    meeting_agenda = models.CharField(max_length=100,null=True,blank=True)
    report = models.TextField(max_length=100,null=True,blank=True)
    # attendees = models.ManyToManyField('Attendee', related_name='meetings')
    # attendance = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    # members_attendance = models.ManyToManyField(Member)
    def __str__(self):
        return f"Meeting on {self.meeting_date} at {self.meeting_time}"


class Attendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    meeting_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)
    # You might need additional fields or relationships to properly link users and meetings.

    def __str__(self):
        return f"{self.user} - {self.meeting}"

class WardAttendance(models.Model):
    ABSENT = 'absent'
    PRESENT = 'present'
   
    APPROVAL_CHOICES = [
    (ABSENT, 'absent'),
    (PRESENT, 'present'),
    
   
    ]
    PENDING = 'pending'
    GRANT = 'grant'
   
    GRANT_CHOICES = [
    (PENDING, 'pending'),
    (GRANT, 'grant'),
    
   
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    # ward_name = models.CharField(max_length=50)
    # is_present = models.BooleanField(default=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE,null=True)
    meeting_date = models.DateField(null=True, blank=True)     
    reason = models.TextField(max_length=100,null=True,blank=True)
    leave_applied = models.BooleanField(default=False)     
    is_present = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PRESENT,
    )
    is_grant = models.CharField(
        max_length=10,
        choices=GRANT_CHOICES,
        default=PENDING,
    )
class Mleave(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE,null=True)
    wardattendance = models.ForeignKey(WardAttendance, on_delete=models.CASCADE,null=True)

    reason = models.TextField(max_length=100,null=True,blank=True)

class SecretaryProfile(models.Model):
    
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,blank=True, null=True )
    name = models.CharField(max_length=100, null=True,blank=True)
    # last_name = models.CharField(max_length=100,null=True,blank=True)
    # age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    # house_name = models.CharField(max_length=100, null=True,blank=True)
    # annual_income = models.IntegerField(max_length=100, null=True,blank=True)
    # land = models.CharField(max_length=100, null=True,blank=True)

    # house_no = models.IntegerField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.IntegerField(max_length=12,null=True,blank=True)
    ward = models.CharField(max_length=100)
    pin_code = models.IntegerField(max_length=6,null=True,blank=True)

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

class Driver(models.Model): 
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    dage = models.IntegerField(null=True, blank=True)

    admin_set_password = models.CharField(max_length=128, blank=True, null=True)

    def set_password(self, password):
        # Hash and set the password
        self.admin_set_password = make_password(password)
    dgender= models.CharField(max_length=100,null=True, blank=True)
    daddress = models.TextField()
    ddis= models.CharField(max_length=100,null=True, blank=True)
    dtaluk = models.CharField(max_length=255, null=True, blank=True)
    dPanchayat = models.CharField(max_length=100,null=True, blank=True)
    dwardno = models.IntegerField(max_length=100,null=True, blank=True)
    dpin = models.IntegerField()
    dphone = models.IntegerField()
    dlisence = models.CharField(max_length=255, null=True, blank=True)
    ddate = models.CharField(max_length=100,null=True, blank=True)
    dbio=models.TextField()
    dvehicle = models.CharField(max_length=255, null=True, blank=True)
    dvehicletype = models.CharField(max_length=255, null=True, blank=True)

    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    damob = models.IntegerField(max_length=100,null=True, blank=True)
    daemail = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.email
# class Crop(models.Model):
#     Namec = models.CharField(max_length=100)
#     des = models.TextField()
#     available = models.BooleanField(default=False)
#     not_available = models.BooleanField(default=False)
class Service(models.Model):
    servicename = models.CharField(max_length=100)
    serviceimage =  models.ImageField(upload_to='blog/', null=True, blank=True)
    servicedes=models.TextField()
    is_active = models.BooleanField(default=True)

class Sell(models.Model):
    ACCEPT = 'accept'
    REMOVE = 'remove'
    PENDING = 'pending'

    APPROVAL_CHOICES = [
    (ACCEPT, 'Accept'),
    (REMOVE, 'Remove'),
    (PENDING, 'Pending'),
    
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    applied_drivers = models.ManyToManyField(Driver, related_name='applied_products', blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    farmerName = models.CharField(max_length=100,null=True, blank=True)
    address = models .CharField(max_length=100,null=True,blank=True)
    wardNo = models .CharField(max_length=100,null=True,blank=True)
    # farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    sell_date = models.DateField(null=True, blank=True)
    applied = models.DateTimeField(null=True,blank=True)
    giventime = models.DateTimeField(null=True,blank=True)

    is_accept = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )
    

class Sellapply(models.Model):
    APPLY = 'apply'
    PENDING = 'pending'

    APPLY_CHOICES = [
    (APPLY ,'Apply'),
    (PENDING, 'Pending'),

    ]

    CONFIRM = 'confirm'
    PENDING = 'pending'

    CONFIRM_CHOICES = [
    (CONFIRM ,'Confirm'),
    (PENDING, 'Pending'),

    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)  # Add this field

    is_apply = models.CharField(
            max_length=10,
            choices=APPLY_CHOICES,
            default=PENDING,
        )
    is_confirm = models.CharField(
            max_length=10,
            choices=CONFIRM_CHOICES,
            default=PENDING,
        )
    is_confirmed = models.BooleanField(default=False)
    # total_cost = models.IntegerField(null=True, blank=True)
    total_cost = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    is_collected = models.BooleanField(default=False)
    # is_paidd = models.BooleanField(default=True)
    is_amount = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    total_amount = models.IntegerField(null=True, blank=True)
    total_amount_new = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
class Total_Amount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    farmerName = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
class Total(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    farmerName = models.CharField(max_length=100, null=True, blank=True)
    sellapply = models.ForeignKey(Sellapply, on_delete=models.CASCADE, blank=True, null=True)

    # total_amount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    balance = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, default=0)
    
class Confirm(models.Model):
    CONFIRM = 'confirm'
    PENDING = 'pending'

    CONFIRM_CHOICES = [
    (CONFIRM ,'Confirm'),
    (PENDING, 'Pending'),

    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE, blank=True, null=True)

    is_confirm = models.CharField(
            max_length=10,
            choices=CONFIRM_CHOICES,
            default=PENDING,
        )

class Productcost(models.Model):
    pname = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100,null=True, blank=True)
    # serviceimage =  models.ImageField(upload_to='blog/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

# class Machinery(models.Model):
#     # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

#     mname = models.CharField(max_length=100)
#     count = models.IntegerField(max_length=100,null=True, blank=True)
#     price = models.IntegerField(max_length=100,null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     days = models.IntegerField(max_length=100,null=True, blank=True)
    
#     available = models.IntegerField(max_length=100,null=True, blank=True)
#     apply_date = models.DateField(null=True, blank=True)
#     farmerName = models.CharField(max_length=100,null=True, blank=True)
#     # applied_by = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='applied_machines', null=True, blank=True)
#     machinery_photo = models.ImageField(upload_to='crop_photos/', blank=True, null=True)


# class ApplicationMachinery(models.Model):
#     # machine = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='machine_applications')
#     apply_date = models.DateField(null=True, blank=True)
#     farmer_name = models.CharField(max_length=100, null=True, blank=True)
#     applied_by = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
#     available = models.IntegerField(max_length=100,null=True, blank=True)


# class MachineryApply(models.Model):
    # machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, blank=True, null=True)  # Add this field
class AddMachinery(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    farmer_profile = models.ForeignKey('FarmerProfile', on_delete=models.CASCADE, blank=True, null=True)
    machinery_photo = models.ImageField(upload_to='machinery_photos/')
    mname = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    apply_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    farmerName = models.CharField(max_length=100,null=True, blank=True)
    address = models .CharField(max_length=100,null=True,blank=True)
    wardNo = models .CharField(max_length=100,null=True,blank=True)
class MachineryApplication(models.Model):
    machinery = models.ForeignKey(AddMachinery, on_delete=models.CASCADE, related_name='applications')
    farmer_profile = models.ForeignKey('FarmerProfile', on_delete=models.CASCADE)
    farmerName = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    wardNo = models.CharField(max_length=100, null=True, blank=True)
    apply_date = models.DateField(null=True, blank=True)
    total_days = models.DateField(null=True, blank=True)
    acount = models.IntegerField(default=0)
    Tcount = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # New field for total price
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)

class MachineryTcount(models.Model):
    mname = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def _str_(self):
        return self.title
    

class Payment(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESSFUL = 'successful', 'Successful'
        FAILED = 'failed', 'Failed'
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link the payment to a user
    razorpay_order_id = models.CharField(max_length=255)  # Razorpay order ID
    payment_id = models.CharField(max_length=255)  # Razorpay payment ID
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # Amount paid
    currency = models.CharField(max_length=3)  # Currency code (e.g., "INR")
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the payment
    payment_status = models.CharField(max_length=20, choices=PaymentStatusChoices.choices, default=PaymentStatusChoices.PENDING)
    MachineryApplication = models.ForeignKey(MachineryApplication, on_delete=models.CASCADE)

    def str(self):
        return f"Order for {self.user.username}"

    class Meta:
        ordering = ['-timestamp']

#Update Status not implemented
    def update_status(self):
        # Calculate the time difference in minutes
        time_difference = (timezone.now() - self.timestamp).total_seconds() / 60

        if self.payment_status == self.PaymentStatusChoices.PENDING and time_difference > 1:
            # Update the status to "Failed"
            self.payment_status = self.PaymentStatusChoices.FAILED
            self.save()