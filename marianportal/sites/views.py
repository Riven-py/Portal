from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.cache import cache_control
import boto3
from .forms import UploadForm
from .models import Module, Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def logout_view(request):
    logout(request)
    return redirect('home')

@cache_control(max_age=7200)
def main_html(request):
  
    if request.method == "POST":
        school_id = request.POST.get("id")
        password = request.POST.get("password")
        user = authenticate(request, username=school_id, password=password)
        if user is None:
            return render(request, 'main.html', {"error": "Invalid school ID or password."})
        login(request, user)

        
        # Store the user object in the session
        request.session['user'] = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'middle_initial': user.middle_initial,
            'last_name': user.last_name,
            'gr_section' : user.gr_section.to_dict(),
            'balance' : user.balance,
            'gr_section_id': user.gr_section.id_this()
        }
        return redirect('/landing/')
    
 
    return render(request, 'main.html')

@login_required
def landing(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('/')
    
    #S3 INIT
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    # Retrieve the stored user object from the session
    user_data = request.session.get('user') 
    user_role = request.user.role
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    balance = user_data.get('balance')
    image_url = s3.generate_presigned_url('get_object', Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f"id_pictures/{user_username}.png"})
    gr_section_id2 = user_data.get('gr_section_id')
    subjects = Subject.objects.filter(gr_section_id = gr_section_id2)
    teacher_subjects = Subject.objects.filter(teacher_id = user_id)
    
    # Pass the user data to the template context
    return render(request, 'learn.html', {
        'user_id': user_id,
        'user_username': user_username,      
        'user_first_name': user_first_name,
        'user_middle_initial': user_middle_initial,
        'user_last_name': user_last_name,
        'user_gr' : user_gr,
        'balance' : balance,
        'picture' : image_url,
        'role' : user_role,
        'subjects' : subjects,
        'teacher_subjects': teacher_subjects,
    })

@login_required
def attendance(request):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    # Retrieve the stored user object from the session
    user_data = request.session.get('user')
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    balance = user_data.get('balance')   
    image_url = s3.generate_presigned_url('get_object', Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f"id_pictures/{user_username}.png"})

    return render(request, 'attendance.html', {
        'user_id': user_id,
        'user_username': user_username,
        'user_first_name': user_first_name,
        'user_middle_initial': user_middle_initial,
        'user_last_name': user_last_name,
        'user_gr' : user_gr,
        'balance' : balance,
        'picture' : image_url,
    })

@login_required
@cache_control(max_age=10800)
def home(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('/')

    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    # Retrieve the stored user object from the session
    user_data = request.session.get('user')
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    balance = user_data.get('balance')    
    image_url = s3.generate_presigned_url('get_object', Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f"id_pictures/{user_username}.png"})
    gr_section_id2 = user_data.get('gr_section_id')
    subjects = Subject.objects.filter(gr_section_id = gr_section_id2)

    return render(request, 'home.html' , {
        'user_id': user_id,
        'user_username': user_username,
        'user_first_name': user_first_name,
        'user_middle_initial': user_middle_initial,
        'user_last_name': user_last_name,
        'user_gr' : user_gr,
        'balance' : balance,
        'picture' : image_url,
        'subject': subjects,
    })

@login_required
def requests(request):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    # Retrieve the stored user object from the session
    user_data = request.session.get('user')
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    balance = user_data.get('balance')
    image_url = s3.generate_presigned_url('get_object', Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f"id_pictures/{user_username}.png"})
    
    return render(request, 'requests.html', {
        'user_id': user_id,
        'user_username': user_username,
        'user_first_name': user_first_name,
        'user_middle_initial': user_middle_initial,
        'user_last_name': user_last_name,
        'user_gr' : user_gr,
        'balance' : balance,
        'picture' : image_url,
    })



def enroll(request):
    return render(request, 'enroll.html')
    
@login_required
def delete_module(request, id):
    # Retrieve the module object with the given id

    if request.method == 'POST':
        redirect('success')


    return redirect('landing')

def sendmodule(request):
    
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    
    user_data = request.session.get('user')
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    balance = user_data.get('balance')
    image_url = s3.generate_presigned_url('get_object', Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f"id_pictures/{user_username}.png"})
    
    assigned_subjects = Subject.objects.filter(teacher=request.user)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            module = form.save(commit=False)
            module.uploaded_by = request.user
            module.save()
            messages.success(request, 'Module uploaded successfully')
            return redirect('test')
    else:
        form = UploadForm()
    return render(request, 'test.html', {
        'form': form, 
        'assigned_subjects': assigned_subjects,
        'user_id': user_id,
        'user_username': user_username,
        'user_first_name': user_first_name,
        'user_middle_initial': user_middle_initial,
        'user_last_name': user_last_name,
        'user_gr' : user_gr,
        'balance' : balance,
        'picture' : image_url,
        
        })

    

def success(request):

    return render(request, 'success.html')

from .models import Subject


def subject_detail(request, subject_id):
    
    user_data = request.session.get('user')
    user_id = user_data.get('id')
    user_username = user_data.get('username')
    user_first_name = user_data.get('first_name')
    user_middle_initial = user_data.get('middle_initial')
    user_last_name = user_data.get('last_name')
    user_gr = user_data.get('gr_section')
    subject = get_object_or_404(Subject, id=subject_id)
    teacher_subjects = Subject.objects.filter(teacher_id=user_id)
    modules = Module.objects.filter(subject=subject)
    
    return render(request, 'dynamic_subject.html', 
                  {'subject': subject,
                    'user_id': user_id,
                    'user_username': user_username,
                    'user_first_name': user_first_name,
                    'user_middle_initial': user_middle_initial,
                    'user_last_name': user_last_name,
                    'user_gr' : user_gr,
                    'modules' : modules,
                    'teacher' : teacher_subjects,
                   })

