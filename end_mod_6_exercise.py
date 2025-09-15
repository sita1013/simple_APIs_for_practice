import requests

def get_song():
    song_title = input("Please enter a song title: ")
    artist = input("Please enter an artist: ")
    return [song_title, artist]

def get_lyrics(artist, title):
    response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}.")
    print(response.json().keys())
    print(response.status_code)

def main():
    song_info = get_song()
    artist = song_info()
    song_title = song_info[0]
    get_lyrics(artist, song_title)

main()