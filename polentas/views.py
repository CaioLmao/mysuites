from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import *

class IndexView (ListView):
   model = Membro
   template_name= "index.html"
   context_object_name = 'polentas'