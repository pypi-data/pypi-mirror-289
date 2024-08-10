import django

__version__ = "1.3.0"


if django.VERSION[:2] < (3, 2):
    default_app_config = "django_readonly_field.apps.Readonly"
