import io

from django.conf import settings

from .models import Stdout

def command_stdout(f):
    def wrapper(self,*args,**options):
        command = type(self).__module__.split('.')[-1]
        with io.StringIO() as f:
            options['stdout'] = f
            f(self,*args, **options)
            stdout=f.getvalue()
            Stdout(command=command,stdout=stdout).save()
            if settings.DEBUG:
                print(stdout)
    wrapper.__name__ = f.__name__
    return wrapper
