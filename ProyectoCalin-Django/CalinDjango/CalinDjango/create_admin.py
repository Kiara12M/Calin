import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CalinDjango.settings')
django.setup()

from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(email='admin@calin.com').exists():
    U.objects.create_superuser('admin@calin.com', 'admin@calin.com', 'Admin1234!')
    print("Superusuario creado")
else:
    print("Ya existe")