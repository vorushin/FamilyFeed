from datetime import date

from django import forms
from django.contrib.auth.models import User

from profiles.models import Child


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


class ChildForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChildForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Child
        fields = ['name', 'birthdate']

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Child.objects.get(user=self.user, name=name)
        except Child.DoesNotExist:
            return name
        raise forms.ValidationError('A child with that name already exists.')

    def clean(self):
        try:
            year = int(self.data['year'])
            month = int(self.data['month'])
            day = int(self.data['day'])

            if year and month and day:
                self.cleaned_data['birthdate'] = date(year, month, day)
                del self._errors['birthdate']
        except ValueError:
            pass

        return self.cleaned_data

    def save(self, commit=True):
        child = super(ChildForm, self).save(commit=False)
        child.user = self.user
        if commit:
            child.save()
        return child
