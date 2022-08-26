CREATE TABLE IF NOT EXISTS performer (
  id SERIAL PRIMARY KEY,
  name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS album_list(
  id SERIAL PRIMARY KEY,
  albom_name VARCHAR(50) NOT NULL,
  year_of_issuse DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS track_list(
  id SERIAL PRIMARY KEY,
  albom_id INTEGER REFERENCES album_list(id),
  track_name VARCHAR(50) NOT NULL,
  track_duration INTEGER CHECK(track_duration > 0)
);

CREATE TABLE IF NOT EXISTS music_collection(
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  year_of_issuse DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS music_genre(
  id SERIAL PRIMARY KEY,
  genre_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS performer_music_genre(
  performer_id INTEGER REFERENCES performer(id),
  genre_id INTEGER REFERENCES music_genre(id),
  constraint pk_performer_in_music_genre primary key (performer_id, genre_id)
);

CREATE TABLE IF NOT EXISTS performer_albom_list(
  performer_id INTEGER REFERENCES performer(id),
  albom_id INTEGER REFERENCES album_list(id),
  constraint pk_performer_albom_list primary key (performer_id, albom_id)
);

CREATE TABLE IF NOT EXISTS track_to_collection(
  track_id INTEGER REFERENCES track_list(id),
  music_collection_id INTEGER REFERENCES music_collection(id),
  constraint pk_track_to_collection primary key (track_id, music_collection_id)
);