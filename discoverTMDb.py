import tmdbsimple as tmdb
import datetime

tmdb.API_KEY = 'MYAPIKey'
photo_URL = 'https://image.tmdb.org/t/p/w500'

def takeMovieImage(date):
    date += datetime.timedelta(weeks=-8)
    release_date = date.date()

    discover = tmdb.Discover()
    response = discover.movie(page=1, original_language='ja', sort_by='popularity.desc', release_date_gte=release_date)

    imageURL = [photo_URL+result['poster_path'] for result in response['results']]

    return imageURL

