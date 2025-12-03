from django import forms
from django.contrib.auth.models import User
from .models import Product, Profile


class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
    )

    # ✅ NEW: WhatsApp field in signup form
    whatsapp = forms.CharField(
        max_length=15,
        required=False,
        label="WhatsApp number (optional)",
        widget=forms.TextInput(attrs={
            "placeholder": "WhatsApp number for chat with buyers"
        })
    )

    class Meta:
        model = User
        # whatsapp is NOT a field on User model, so it stays outside Meta.fields
        fields = ['username', 'email', 'password']

    # Optional: control the order of fields in the template loop
    field_order = ['username', 'email', 'whatsapp', 'password', 'confirm_password']

    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip().lower()
        allowed = ('@bbdnitm.ac.in', '@bbdniit.ac.in', '@bbdu.org')

        if not any(email.endswith(d) for d in allowed):
            raise forms.ValidationError(
                "Only @bbdnitm.ac.in, @bbdniit.ac.in or @bbdu.org email IDs are allowed."
            )

        # prevent duplicate emails
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('confirm_password')
        if p1 and p2 and p1 != p2:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'whatsapp', 'branch', 'year', 'hide_name']
        labels = {
            'phone': 'Phone number (optional)',
            'whatsapp': 'WhatsApp number for chat',
            'branch': 'Branch',
            'year': 'Year',
            'hide_name': 'Hide my name from buyers',
        }
        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder': 'e.g. 9876543210'
            }),
            'whatsapp': forms.TextInput(attrs={
                'placeholder': 'WhatsApp number used for chat'
            }),
            'branch': forms.TextInput(attrs={
                'placeholder': 'e.g. CSE, ECE, BBA...'
            }),
            'year': forms.TextInput(attrs={
                'placeholder': 'e.g. 1st, 2nd, 3rd, Final'
            }),
            'hide_name': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-teal-600'
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'category',
            'price',
            'condition',
            'image',
            'city_campus',
        ]
