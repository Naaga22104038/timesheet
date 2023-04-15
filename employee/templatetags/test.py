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
from django import template
register = template.Library()
@register.filter
def multiply(value, arg):
    return value * arg

