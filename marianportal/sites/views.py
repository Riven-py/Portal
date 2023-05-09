from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.cache import cache_control, cache_page
import boto3
from .forms import UploadForm
from .models import Module
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
            'gr_section' : user.gr_section,
            'balance' : user.balance
        }
        return redirect('/landing/')
    
#    if request.user.is_authenticated:
#        sweetify.success(request, 'You have already been authenticated.')
#        return redirect('/landing/')
 
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

    modules = Module.objects.filter(grade_section=user_gr)
    
    
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
        'modules': modules,
        'role' : user_role,
    })

@login_required
def attendance(request):
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

    return render(request, 'home.html' , {
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

@login_required
def sendmodule(request):
    assigned_sections = request.user.assigned_sections
    
    user_data = request.session.get('user')
    user_first_name = user_data.get('first_name')
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            grade_section = form.cleaned_data.get('grade_section')
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            uploaded_file = Module(file=form.cleaned_data['file'], grade_section=grade_section, title=title, description=description, uploaded_by=request.user)
            uploaded_file.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('formsend')
    else:
        form = UploadForm()
        
    return render(request, 'test.html', {
        'form': form,
        'assigned_sections': assigned_sections,
        'user_first_name': user_first_name,
    })
    

def success(request):

    return render(request, 'success.html')