# -*- coding: utf-8 -*-

import django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RestPasswordResetConfig(AppConfig):
    """Default configuration for django_rest_passwordreset app."""

    name = "django_rest_passwordreset"
    label = "django_rest_passwordreset"
    verbose_name = _("REST Password Reset")
