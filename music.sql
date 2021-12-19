CREATE TABLE artists
( id INTEGER PRIMARY KEY ASC,
    artist_name
);

CREATE TABLE albums
( id INTEGER PRIMARY KEY ASC,
    album_name TEXT,
    artist_name TEXT
);

CREATE TABLE songs
( id INTEGER PRIMARY KEY ASC,
song_name TEXT,
album_name TEXT,
track_num INTEGER,
track_length INTEGER)

