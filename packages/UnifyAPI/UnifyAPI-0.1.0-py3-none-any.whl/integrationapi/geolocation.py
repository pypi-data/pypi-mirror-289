# IntegrationAPI/integrationapi/geolocation.py

import googlemaps

class GeolocationAPI:
    def __init__(self, api_key):
        self.client = googlemaps.Client(api_key)

    def geocode(self, address):
        try:
            result = self.client.geocode(address)
            if result:
                return result[0]['geometry']['location']
            else:
                raise Exception("Location not found.")
        except Exception as e:
            raise Exception(f"Google Maps API Error: {str(e)}")
