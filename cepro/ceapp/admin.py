from django.contrib import admin
from .models import Member
from .models import Crop
from .models import Product
from .models import ApplyCrop
# from .models import UserProfile
from .models import CustomUser
from .models import FarmerProfile
from .models import Meeting
from .models import SecretaryProfile
from .models import Attendance
from .models import Driver
from .models import Service
from .models import WardAttendance

# from .models import Notification
# from .models import Notification


# Register your models here.
admin.site.register(Member)
admin.site.register(Crop)
admin.site.register(Product)
admin.site.register(ApplyCrop)
# admin.site.register(UserProfile)
admin.site.register(CustomUser)
admin.site.register(FarmerProfile)
admin.site.register(SecretaryProfile)
admin.site.register(Meeting)
admin.site.register(Attendance)
admin.site.register(WardAttendance)
admin.site.register(Driver)
admin.site.register(Service)
# admin.site.register(Notification)