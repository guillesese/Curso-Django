from django.shortcuts import render, HttpResponse

#HttpResponse permite contestar una peticion devolviendo un codigo. 
#  

html_base = """
<h1>Mi web personal</h1>
<ul> 
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""

'''Metodo de la portada
    request: peticion de que se quiere ver la portada. '''
def home (request):
    # se devuelve usando la plantilla templates\core\home.html
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")


def contact(request):
    return render(request,"core/contact.html")