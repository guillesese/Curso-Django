from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request): 
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffetiera: Nuevo mensaje de contacto', 
                'De {} <{}>\n\nEscribio:\n\n'.format(name,email,content) , 
                'no-contestar@email_pruebas.io',
                ['emailprueba@email_pruebas.io'], 
                reply_to = [email]
            )
            try:
                #todo ha ido bien, redireccionar
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                #todo ha ido mal, redireccionar
                return redirect(reverse('contact')+'?fail')
            
            



    return render(request, 'contact/contact.html', {'form':contact_form})
