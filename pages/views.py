from django.views.generic import TemplateView
from django.shortcuts import render
import requests

class HomePageView(TemplateView):
    template_name = 'home.html'

def profile_view(request):
    return render(request, 'account/profile.html')

def spotify_view(request):
    client_id = "0365d01656034781bef2e8f42fbe1c41"
    client_secret = "c6bf652b853c4cc1a17ed364673d45d7"

    grant_type = 'client_credentials'

    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'

    respnse = requests.post(url, data=body_params, auth = (client_id, client_secret)) 
    

    top_50_usa_playlist_id = '37i9dQZEVXbLRQDuF5jeBp'
    get_playlists_endpoint_url = 'https://api.spotify.com/v1/playlists/{playlist_id}'

    request_url = get_playlists_endpoint_url.format(
        playlist_id=top_50_usa_playlist_id
    )

    token = respnse.json()['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(
            token=token
        )
    }

    response = requests.get(request_url, headers=headers)

    

    testex = requests.get(request_url, headers=headers)

    data = []

    for item in testex.json()['tracks']['items']:
        info_musica = { 'musica': item['track']['name'], 'artista': item['track']['artists'][0]['name'], 'album': item['track']['album']['name'] }
        data.append(info_musica)
    context = {'data': data}
    return render(request, 'spotify.html', context=context)