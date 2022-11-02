from django.views.generic import TemplateView,View,ListView
from django.forms.models import model_to_dict
from django.shortcuts import render,redirect
from .models import Dresses
from .forms import InputBodyForm

# Create your views here.
class VirtualRoom(ListView):
    """ virtualRoom template view."""
    model = Dresses
    template_name ="virtualRoom/index.html"
    form = InputBodyForm

def post(self,request):
    """Handle submissions."""
    form = self.form(request.POST)
    if form.is_valid():
        user = form    
