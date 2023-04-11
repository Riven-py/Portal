from django.shortcuts import render

# Create your views here.
def main_html(request):
    return render(request, 'main.html')

def attendance(request):
    return render(request, 'attendance.html')

def home(request):
    return render(request, 'home.html')

def landing(request):
    return render(request, 'learn.html')

def requests(request):
    return render(request, 'requests.html')