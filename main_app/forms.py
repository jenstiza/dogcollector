from django.forms import ModelForm
from .models import Feeding, Toy

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class RatingForm(ModelForm):
  class Meta:
    model = Toy
    fields = ['rating']