from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Batch, User


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=False, label='Last Name')
    batch_name = forms.ModelChoiceField(
        queryset=Batch.objects.all(),
        empty_label='Select batch',
        label='Batch Name',
        required=True,
        to_field_name='name',
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        selected_batch = self.cleaned_data.get('batch_name')
        if selected_batch:
            user.batch_name = str(selected_batch)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'batch_name', 'password1', 'password2']
