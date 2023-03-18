from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model=Poll
        fields=['question','op1','op2','op3']