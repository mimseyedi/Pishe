from django import forms
from account.models import UserInfo

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = "__all__"