### Installation
```bash
$ pip install django-command-stdout
```

#### `settings.py`
```python
INSTALLED_APPS+=['django_command_stdout']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Examples
`@command_stdout` decorator
```python
from django_command_stdout.decorators import command_stdout

class Command(BaseCommand):
    @command_stdout
    def handle(self,*args,**options):
```

`BaseCommand`
```python
import io
from django.core.management.base import BaseCommand
from django_command_stdout.models import Stdout

class Command(BaseCommand):
    def execute(self, *args, **options):
        command = type(self).__module__.split('.')[-1]
        with io.StringIO() as f:
            super().execute(*args, stdout=f,**options)
            Stdout(command=command,stdout=f.getvalue()).save()
```

`call_command`
```python
from django_command_stdout.utils import call_command

call_command('name',*args,**options)
```

