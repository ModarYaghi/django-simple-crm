from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record


class SignUpForm(UserCreationForm):
    """Sign up a new user"""

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:  # type: ignore
        model = User  # Django will look at the built-in `User` model for generating any fields that arn't explicitly defined.
        fields = (  # which files to include
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_customizations = {
            "username": {
                "widget_attrs": {"class": "form-control", "placeholder": "User Name"},
                "label": "",
                "help_text": (
                    "<span class='form-text text-muted'><small>Required. 150 charcter or fewer. "
                    "Letters, digits and @/./+/-/_ only.</small></span>"
                ),
            },
            "password!": {
                "widget_attrs": {"class": "form-control", "placeholder": "Password"},
                "label": "",
                "help_text": (
                    "<ul class='form-text text-muted small'>"
                    "<li>Your password can't be too similar to your other personal information.</li>"
                    "<li>Your password must contain at least 8 character.</li>"
                    "<li>Your password can't be a commonly used password.</li>"
                    "<li>Your password can't be entirely numeric.</li>"
                    "</ul>"
                ),
            },
            "password2": {
                "widget_attrs": {
                    "class": "form-control",
                    "placeholder": "Confirm Password",
                },
                "label": "",
                "help_text": (
                    "<span class='form-text text-muted'><small>Enter the same password as before, for verification.</small></span>"
                ),
            },
        }

        for field_name, settings in field_customizations.items():
            field = self.fields.get(field_name)
            if field:
                # Update widget attributes
                field.widget.attrs.update(settings.get("widget_attrs", {}))

                # Set label and help_text
                field.label = settings.get("label", field.label)
                field.help_text = settings.get("help_text", field.help_text)


class AddRecordForm(forms.ModelForm):
    """Add record form"""

    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        label="",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        label="",
    )

    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="",
    )

    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Phone Number", "class": "form-control"}
        ),
        label="",
    )

    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Address", "class": "form-control"}
        ),
        label="",
    )

    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "City", "class": "form-control"}
        ),
        label="",
    )

    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "State", "class": "form-control"}
        ),
        label="",
    )

    zipcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Zipcode", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = Record
        exclude = ("user",)
