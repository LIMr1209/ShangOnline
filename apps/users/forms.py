from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile, EmailVerify
import re


class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={
        'required': '邮箱必须为填写'
    })
    password = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })
    captcha = CaptchaField(error_messages={
        'invalid': '验证码错误'
    })


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={
        'required': '邮箱必须为填写'
    })
    password = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })


class UserForgetForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={
        'required': '邮箱必须为填写'
    })

    captcha = CaptchaField(error_messages={
        'invalid': '验证码错误'
    })


class UserResetForm(forms.Form):
    password = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })

    password1 = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })


class UserChangeImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'address', 'gender', 'birthday', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        com = re.compile('^(13\d|14[57]|15\d|166|17[367]|18\d)\d{8}$')
        if com.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号不合法')


class UserChangePasswordForm(forms.Form):
    password1 = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })
    password2 = forms.CharField(min_length=3, max_length=20, required=True, error_messages={
        "min_length": '密码最少为3个',
        'max_length': '密码最多20为',
        'required': '密码必须填写',
    })


class UserSendCodeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']


class UserChangeEmailForm(forms.ModelForm):
    class Meta:
        model = EmailVerify
        fields = ['email','code']
