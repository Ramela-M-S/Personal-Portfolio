import os
import django

# Replace 'project.settings' with your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User

# Change username, email, and password as you like
USERNAME = 'ramela'
EMAIL = 'ramelams07@gmail.com'
PASSWORD = 'ramela'

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")
