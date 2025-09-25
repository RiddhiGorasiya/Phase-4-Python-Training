from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    
class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    
# Field type Examples

class DemoForm(forms.Form):
    # basic fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()
    
    # Additional fields
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()
    
    # Choice fields
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    interests = forms.MultipleChoiceField(choices=[('sports', 'Sports'), ('music', 'Music'), ('travel', 'Travel')])
    
    # File and URL fields
    profile_picture = forms.FileField()
    website = forms.URLField()
    resume = forms.FileField()
    profile_image = forms.ImageField()
    
    # other Specialized fields
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': 'Enter a valid phone number.'})
    password = forms.CharField(widget=forms.PasswordInput)
    slag = forms.SlugField()
    id_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()