import io

from django.conf import settings
from django.core.management import call_command as _call_command
from django.core.management.base import BaseCommand

def call_command(name,*args,**options):
    with io.StringIO() as f:
        options['stdout'] = f
        _call_command(name,*args, **options)
        stdout=f.getvalue()
        Stdout(command=name,stdout=stdout).save()
        if settings.DEBUG:
            print(stdout)
