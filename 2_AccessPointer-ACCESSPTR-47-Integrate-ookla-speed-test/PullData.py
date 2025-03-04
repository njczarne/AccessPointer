import os
import django
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "database"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

from myapp.models import Location, Internet

def get_data():
    #Fetch all data from the Internet and Location models
    internet_data = Internet.objects.all() # Query all Internet entries
    location_data = Location.objects.all() # Query all Location entries

    # Dictionary to store the data based on the unique_id
    combined_data = {}

    # Store Internet data in the dictionary using unique_id as key
    for internet_entry in internet_data:
        unique_id = internet_entry.unique_id
        combined_data[unique_id] = {
            'download': internet_entry.download,
            'upload': internet_entry.upload,
            'ping': internet_entry.ping,
            'location': None # Placeholdder for location data
        }

    # Store Location data in the dictionary using unique_id
    for location_entry in location_data:
        unique_id = location_entry.unique_id
        if unique_id in combined_data:
            #Add location data to corresponding unique_id
            combined_data[unique_id]['location'] = {
                'latitude': location_entry.latitude,
                'longitude': location_entry.longitude
            }
    return combined_data

def print_data():
    data = get_data()
    for unique_id, info in data.items():
        print(f"Unique ID: {unique_id}")
        print(f"Internet Data: {info['download']} download, {info['upload']} upload, {info['ping']} ping")
        print(f"Location Data: Latitude: {info['location']['latitude']}, Longitude: {info['location']['longitude']}")
        print("-" * 40)


if __name__ == "__main__":
    data = get_data()
    for unique_id, info in data.items():
        print(f"Unique ID: {unique_id}")
        print(f"Internet Data: {info['download']} download, {info['upload']} upload, {info['ping']} ping")
        print(f"Location Data: Latitude: {info['location']['latitude']}, Longitude: {info['location']['longitude']}")
        print("-" * 40)