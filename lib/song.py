class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
    
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, song):
        if (song.genre not in cls.genres):
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        if (song.artists not in cls.artists):
            cls.artists.append(song.artist)
    
    @classmethod
    def add_to_genre_count(cls, song, increment=1):
        if song.genre in cls.genre_count:
            cls.genre_count[song.genre] += increment
        else:
            cls.genre_count[song.genre] = increment

    @classmethod
    def add_to_artist_count(cls, song, increment=1):
        if song.artist in cls.artist_count:
            cls.artist_count[song.artist] += increment
        else:
            cls.artist_count[song.artist] = increment

