from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import request

from myblog.models import NewBlog, Feedback


class SignupForm(forms.ModelForm):
    username = forms.CharField(label="Username",max_length=100)
    first_name = forms.CharField(label="First Name",max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput ,max_length=100)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput, max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2',)

    def save(self,commit=True):
            user = super(SignupForm,self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

    def clean_password2(self):
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]
        if pass1 and pass2 and pass1!=pass2:
            raise forms.ValidationError("Password does not match")
        return pass2

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is None:
            raise forms.ValidationError("Invalid")
        return super(LoginForm,self).clean()
    
class BlogNew(ModelForm):
    class Meta:
        model = NewBlog
        exclude = ('blog_creationdate','username','username_id')

class ContactForm(forms.Form):
    name = forms.CharField(label="Name")
    emailid = forms.CharField(label="Email ID")
    message = forms.CharField(label="Message",widget=forms.Textarea)

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('id',)