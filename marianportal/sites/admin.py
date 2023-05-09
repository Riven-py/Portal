from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField


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
    list_display = ('username', 'first_name', 'last_name', 'role','gr_section', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'role')
    ordering = ('last_name', 'first_name')
    
    def get_fieldsets(self, request, obj=None):
        if obj is None:
            role_fields = ('role',)
        elif obj.role == 'Teacher':
            role_fields = ('first_name', 'middle_initial', 'last_name', 'picture', 'assigned_sections')
        else:
            role_fields = ('first_name', 'middle_initial', 'last_name', 'picture')

        fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': role_fields}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
            ('Custom fields', {'fields': ('role','balance', 'uid')}),
        )
        return fieldsets
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_initial', 'last_name', 'gr_section', 'picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('role','balance', 'uid')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'first_name', 'middle_initial', 'last_name','gr_section', 'role', 'uid'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
