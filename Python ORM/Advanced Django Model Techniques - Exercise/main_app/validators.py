from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("Name can only contain letters and spaces")


def validate_phone(value):
    if len(value) != 13 or value[0:4] != "+359" or not value[4: ].isdigit():
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


