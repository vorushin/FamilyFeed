from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.RegexField(
        max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={'invalid': 'This value may contain only letters, '\
            'numbers and @/./+/-/_ characters.'})
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('A user with that username already '\
            'exists.')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
