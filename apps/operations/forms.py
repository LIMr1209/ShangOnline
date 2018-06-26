from django import forms
from .models import UserAskInfo
import re


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAskInfo  # 模型类对应
        # fields = '__all__'  #  验证全部
        # fields = ['name','phone','course'] #仅验证 。。
        exclude = ['add_time']  # 除了add_time 验证

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # 创建正则对象
        com = re.compile("^(13\d|14[57]|15\d|166|17[367]|18\d)\d{8}$")
        if com.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机验证不合法')


class UserCommentFrom(forms.Form):
    comment = forms.CharField(max_length=200, min_length=5, required=True)
    courseid = forms.IntegerField(required=True)
