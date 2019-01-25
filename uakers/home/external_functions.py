from django.core import validators
from django.utils.translation import gettext_lazy as _

class CustomUsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z0-9]+$'
    message = _(
        'Enter a valid username. A valid username may contain only letters '
        'and numbers.'
    )
