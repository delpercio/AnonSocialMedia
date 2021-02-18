from django import forms
from ghost_app.models import Posts

POST_CHOICES = ((True, 'Boast'), (False, 'Roast'))

class PostForm(forms.Form):
    text= forms.CharField(max_length=100)
    post_type= forms.CharField(label='Is this a...', widget=forms.Select(choices=POST_CHOICES))
