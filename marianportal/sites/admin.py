from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Subject, Section
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(forms.ModelForm): 

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    ROLE_CHOICES =     [('Student', 'Student'),    
                        ('Teacher', 'Teacher'),    
                        ('Coordinator', 'Coordinator'),]

    role = forms.ChoiceField(choices=ROLE_CHOICES, initial='Student')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'middle_initial', 'last_name', 'gr_section', 'role')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')    
        if password != '':
            user.password = make_password(password)
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label='Password', help_text='Raw passwords are not stored, so there is no way to see the password, but you can change the password using <a href="password/">this form</a>.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'middle_initial', 'last_name', 'email', 'gr_section', 'role', 'is_active')

    def clean_password(self):
        return self.initial['password']


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        fieldsets = super().get_fieldsets(request, obj)
        if obj.role == 'Teacher':
            fieldsets[1][1]['fields'] = ('first_name', 'middle_initial', 'last_name', 'picture', 'assigned_sections')
        else:
            fieldsets[1][1]['fields'] = ('first_name', 'middle_initial', 'last_name', 'picture')
        return fieldsets

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'first_name', 'middle_initial', 'last_name', 'gr_section', 'role',)
        }),
    )

    list_display = ('username', 'first_name', 'last_name', 'role', 'gr_section', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'role')
    ordering = ('username', 'first_name')


class CustomUserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name} ({obj.username})"

class SubjectAdminForm(forms.ModelForm):
    teacher = CustomUserModelChoiceField(
        queryset=CustomUser.objects.filter(role='Teacher'),
        required=False,
        label='Teacher',
    )

    class Meta:
        model = Subject
        fields = '__all__'

class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ['name', 'gr_section', 'teacher']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Section)
