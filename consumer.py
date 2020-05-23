import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dotenv


dotenv.load_dotenv()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='slayer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])