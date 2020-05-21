from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomepageView(TemplateView):
    template_name = 'index.html'


    def get_context_data(Self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "greeting1":"hello ! nice to meet you",
            "greeting2":"hello again!",
        }
        return context

    def say_byee(self):
        return goodbye!

