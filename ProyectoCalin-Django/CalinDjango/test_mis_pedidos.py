import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CalinDjango.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.first()

if not user:
    print("No users found!")
    exit()

from rest_framework_simplejwt.tokens import RefreshToken
refresh = RefreshToken.for_user(user)
access_token = str(refresh.access_token)

print("Got token for user:", user.email)

headers = {
    'Authorization': f'Bearer {access_token}'
}
import urllib.request
import json

req = urllib.request.Request('http://localhost:8000/api/productos/mis-pedidos/', headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        print("Response:", response.read().decode())
except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print("Body:", e.read().decode())
