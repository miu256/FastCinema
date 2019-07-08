import googlemaps

APIKey = "MYAPIKey"
LIMIT = 6


def findCinema(nowLocation):
    myClient = googlemaps.Client(APIKey)

    geoResult = myClient.geocode(nowLocation)
    if len(geoResult) == 0:
        return []
    location = geoResult[0]['geometry']['location']

    placeResult = myClient.places_nearby(location=location, radius=1000, type='movie_theater', language='ja')

    if placeResult['status'] != 'OK':
        return []

    place = []
    lenPlace = 0
    for result in placeResult['results']:
        if lenPlace == LIMIT:
            break
        place.append(result)
        lenPlace += 1

    return place
