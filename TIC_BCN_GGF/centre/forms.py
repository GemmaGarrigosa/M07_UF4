from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User #Model que volem fer servir
        fields = '__all__' #Volem que hi hagi tots els camps