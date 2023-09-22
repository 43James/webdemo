from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms
from users.models import CustomUser, Profile

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 
                  'first_name', 'last_name')
           
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'email': 'อีเมล'
        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control mt-2', 'style':'font-weight: bold; color: rgb(8, 0, 255);'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control mt-2', 'style':'font-weight: bold; color: rgb(8, 0, 255);'}),
            'email' : forms.TextInput(attrs={'class': 'form-control mt-2', 'style':'font-weight: bold; color: rgb(8, 0, 255);'}),
        }

CHOICE = [
    ('female', 'หญิง'),
    ('maie','ชาย'),
]

class ExtendedProfileForm(forms.ModelForm):
    prefix = 'extended'

    class Meta:
        model = Profile
        fields = ('gender', 'work_group')
        labels = {
            'gender': 'เพศ',
            'work_group': 'กลุ่มงาน'
        }
        widgets = {
            'gender': forms.RadioSelect(choices=CHOICE),
            'work_group': forms.TextInput(attrs={'class': 'form-control mt-2', 'style':'font-weight: bold; color: rgb(8, 0, 255);'}),
        }