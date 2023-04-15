"""
WSGI config for timesheet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
#pylint: disable=inconsistent-return-statements
#pylint: disable=wrong-import-order
#pylint: disable=ungrouped-imports
#pylint: disable=missing-function-docstring
#pylint: disable=unused-import
#pylint: disable=no-member
#pylint: disable=bad-whitespace
#pylint: disable=no-else-return
#pylint: disable=bad-continuation
#pylint: disable=missing-module-docstring
#pylint: disable=missing-class-docstring
#pylint: disable=trailing-newlines
#pylint: disable=missing-final-newline
#pylint: disable=invalid-name

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timesheet.settings')

application = get_wsgi_application()
