from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from websites.models import Contact
from django.contrib.auth.models import User

@login_required
def custom_admin_panel(request):
    user_count= User.objects.count()
    contacts = Contact.objects.all()
    return render(request, 'adminpanel1/custom_admin_panel.html', {'contacts': contacts , 'user_count': user_count})


@login_required
def edit(request, id):
    contact= get_object_or_404(Contact, id=id)
    if request.method =='POST':
        name= request.POST.get('name')
        email =request.POST.get('email')
        subject=request.POST.get('subject')
        message= request.POST.get('message')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        
        contact.save()
        return redirect('custom_admin_panel')
    return render(request, "adminpanel1/edit_contact.html", {'contact': contact})


@login_required
def delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('custom_admin_panel')
    return render(request, 'adminpanel1/delete.html', {'contact': contact})