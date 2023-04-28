from django.forms import ModelForm
from django import forms
 
# define the class of a form

from django import forms
  
class PostForm(forms.Form):
    first_name = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your First Name"
                 })
    last_name = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your Last Name"
                 })
    date_of_birth = forms.DateField(
                  error_messages = {
                 'required':"Please Enter your Date of Birth"
                 })
    gender = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your Date of Birth"
                 })
    country = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your Date of Birth"
                 })
    state = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your state"
                 })
    town = forms.CharField(
                  error_messages = {
                 'required':"Please Enter your town"
                 })
    zipcode = forms.IntegerField(
                  error_messages = {
                 'required':"Please Enter your Zipcode"
                 })     
    phonenumber1 = forms.IntegerField(
                  error_messages = {
                 'required':"Please Enter your town"
                 })