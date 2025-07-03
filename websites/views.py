from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Contact

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        
        return redirect('contact')  # yahan sirf url name dena hai
    return render(request, 'contact.html')
    
def projects(request):
    return render(request, 'projects.html')

def skills(request):
    return render(request, 'skills.html')