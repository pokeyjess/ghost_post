from django import forms
from ghost_post_app.models import Posts

#https://docs.djangoproject.com/en/3.1/ref/forms/fields/


class PostForm(forms.Form):
    content = forms.CharField(max_length=280)
    choice = forms.ChoiceField(help_text='Boast or Roast?', choices=[(True, 'Boast'), (False, 'Roast')])

    
    