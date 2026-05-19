import django
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CalinDjango.settings')
django.setup()

from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(email='admin@calin.com').exists():
    U.objects.create_superuser(email='admin@calin.com', password='Admin1234!')
    print("Superusuario creado")
else:
    print("Ya existe")