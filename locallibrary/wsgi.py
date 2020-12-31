"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.
# TODO: Remember to uncomment the following line to make the setting file dynamic, depending on prod or dev environments
# settings_module = 'locallibrary.production' if 'WEBSITE_HOSTNAME' in os.environ else 'locallibrary.settings'
settings_module = 'locallibrary.production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
