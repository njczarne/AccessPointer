import os
import django
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "database"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

from myapp.models import Location
from myapp.models import Internet

def enterNewLocation(lat, long, id):
   location = Location(latitude=lat, longitude=long, id=id)
   location.save()

   print("New location entry added!")

def enterNewInternet(down, up, p, id):
   internet = Internet(download=down, upload=up, ping=p, id=id)
   internet.save()

   print("New Internet entry added!")