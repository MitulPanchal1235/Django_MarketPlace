from django.forms import ModelForm
from .models import *

class Profileform(ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
        exclude=['user']

class Postform(ModelForm):
    class Meta:
        model = Posts
        fields ='__all__'