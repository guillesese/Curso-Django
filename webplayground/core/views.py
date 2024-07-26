from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/home.html'

    ''' OP 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi super Web Playground'
        return context
    ''' 
    # OP 2
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Mi super Web playground'})

class SamplePageView(TemplateView): 
    template_name = 'core/sample.html'    
