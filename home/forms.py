from django import forms
from .models import Profile, BlogPost
from django.contrib.auth.models import User




class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    phone_no = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    social_media_handle = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    image = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['phone_no', 'bio', 'social_media_handle', 'image',]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'social_media_handle', 'image', )
     
        
class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=500,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }