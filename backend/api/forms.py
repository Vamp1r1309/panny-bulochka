import random
import re
from django import forms
from catalog.models import UserTelegram
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RussianValidator:
    ALLOWED_CHAR = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские буквы!"

    def __call__(self, value, *args, **kwargs):
        if not (set(value.lower()) <= set(self.ALLOWED_CHAR)):
            raise ValidationError(self.message, code=self.code)


class AddRegisterUserForm(forms.ModelForm):

    username = forms.CharField(max_length=50,
                               min_length=2,
                               label='Ваше Имя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               validators=[RussianValidator()])

    class Meta:
        model = UserTelegram
        fields = ['id', 'username', 'phone_user', 'date_of_birth']
        widgets = {
            'phone_user': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            }
        labels = {'username': 'Имя пользователя'}

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 2:
            raise ValidationError("длина должна быть более 2 символов")
        if len(username) > 50:
            raise ValidationError("Длина имени превышает 50 символов")
        return username

    def clean_phone_user(self):
        user_phone = self.cleaned_data['phone_user']
        result = re.match(
            r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
            string=user_phone)
        if not result:
            raise ValidationError("Данный номер телефона не соответствует")
        return user_phone
