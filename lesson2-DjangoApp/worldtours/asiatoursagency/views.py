from django.shortcuts import render, redirect
from .models import Tour
from .forms import ContactForm
# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html') #context

def home_view(request):
    return render(request, 'forms/home.html')

# Define the contact_view function to handle the contact
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'forms/contact.html', context)

# Define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'forms/contact-success.html')