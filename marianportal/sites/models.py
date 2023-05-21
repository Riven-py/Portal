from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxChoicesValidator
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Section(models.Model):
    name = models.CharField(max_length=255, default='Set')

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return self.name.replace("[", "").replace("]", "").replace("'", "")
    
    def id_this(self):
        return str(self.id).replace("[", "").replace("]", "").replace("'", "")

        

class CustomUser(AbstractUser):

    username = models.CharField(max_length=7, unique=True, verbose_name='School ID', 
    help_text='6 Digit School ID upon enrollment is required', error_messages={'unique': 'A user with that school ID already exists.'})
    first_name = models.CharField(max_length=30, verbose_name='First name')
    middle_initial = models.CharField(max_length=2, verbose_name='Middle initial')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    email = models.EmailField(verbose_name='Email', blank=True)
    role = models.CharField(max_length=20, verbose_name='Role', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    gr_section = models.ForeignKey(Section, default='Set', on_delete=models.PROTECT, verbose_name='Grade and Section')
    balance = models.IntegerField(verbose_name="Balance", default='0')
    uid = models.CharField(default="A1A1A1A1", verbose_name='RFID', max_length=8)
    picture = models.FileField(upload_to='id_pictures/', null=True)

    attached_phone = models.CharField(max_length=13, default = '+631234567890')
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'middle_initial', 'last_name']
    


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['last_name', 'first_name']
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_initial}. {self.last_name}"
    
class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Subject Name')
    gr_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subjects', verbose_name='Grade & Section')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Teacher')

    def __str__(self):
        return self.name
    
    def id_thiss(self):
        return str(self.id).replace("[", "").replace("]", "").replace("'", "")



class Module(models.Model):
    file = models.FileField(upload_to='uploads/')
    subject = models.ForeignKey( Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    

    
    
    
    
    
    
    
    
    
    
    
    