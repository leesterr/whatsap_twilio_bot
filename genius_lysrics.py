import lyricsgenius

api_token = 'api_token_here'
genius = lyricsgenius.Genius(access_token=api_token)


def search(name) -> str:
    artist, song = name.split('-')
    lyric = genius.search_song(title=song, artist=artist)
    music = lyric.lyrics
    if len(music) > 1600:
        list1 = []
        length = 1600
        for i in range(0, length):
            list1.append(music[i])
        first_half = list1[:1599]
        return f'{"".join(first_half)}'
    else:
        return music


