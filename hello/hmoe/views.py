from django.shortcuts import render, HttpResponse
from datetime import datetime
from hmoe.models import Contact

from django.contrib import messages
# Create your views here.
def index(request):
    
    
    
    context = {
            'variable' : 'this is sent'
            }
            
            
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is ABOUT PAGE')


def service(request):
    return render(request, 'services.html')
    #return HttpResponse('This is SERVICE PAGE')

def contact(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        textarea = request.POST.get('textarea')
        contact = Contact(email=email, password = password, textarea= textarea, 
                          date = datetime.today())
        
        contact.save()
        
        messages.success(request, 'Succesfully Submitted')
    
    return render(request, 'contact.html')
    #return HttpResponse('This is CONTACT PAGE')