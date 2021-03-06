from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from landfill.generators import generate_addons


class Command(BaseCommand):
    """
    Generate example addons for development/testing purpose.

    Addons will have 1 preview image, 2 translations (French and
    Spanish), 5 ratings and might be featured randomly. If you don't
    provide any --owner email address, all created add-ons will have
    'nobody@mozilla.org' as owner. If you don't provide any --app name,
    all created add-ons will have 'firefox' as application.

    Categories from production (Alerts & Updates, Appearance, etc)
    will be created and randomly populated with generated addons.

    Usage:

        python manage.py generate_addons <num_addons>
            [--owner <email>] [--app <application>]

    """

    help = __doc__
    option_list = BaseCommand.option_list + (
        make_option('--owner', action='store', dest='email',
                    default='nobody@mozilla.org',
                    help="Specific owner's email to be created."),
        make_option('--app', action='store', dest='app_name',
                    default='firefox',
                    help="Specific application targeted by add-ons creation."),
    )

    def handle(self, *args, **kwargs):
        if not settings.DEBUG:
            raise CommandError('You can only run this command with your '
                               'DEBUG setting set to True.')
        num = int(args[0])
        email = kwargs.get('email')
        app_name = kwargs.get('app_name')
        generate_addons(num, email, app_name)
