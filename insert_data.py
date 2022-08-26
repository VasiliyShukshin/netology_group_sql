import sqlalchemy
db = 'postgresql://user:pass@localhost:5432/homeworke'

engine = sqlalchemy.create_engine(db)

connection = engine.connect()

albom_list = connection.execute(
    """
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom1', '2014-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom2', '2015-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom3', '2016-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom4', '2017-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom5', '2018-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom6', '2019-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom7', '2020-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom8', '2021-01-01 00:00:00');
        insert into album_list(albom_name, year_of_issuse) VALUES('NewYearAlbom9', '2014-01-01 00:00:00');
    """
)

music_genre = connection.execute(
    """
        insert into music_genre(genre_name) VALUES('Rock');
        insert into music_genre(genre_name) VALUES('Folk_music');
        insert into music_genre(genre_name) VALUES('Jazz');
        insert into music_genre(genre_name) VALUES('Reggae');
        insert into music_genre(genre_name) VALUES('Punk');
    """
)

performer = connection.execute(
    """
        insert into performer(name) VALUES('Pavel');
        insert into performer(name) VALUES('Vasya');
        insert into performer(name) VALUES('Kira');
        insert into performer(name) VALUES('Joni');
        insert into performer(name) VALUES('Nik');
        insert into performer(name) VALUES('Nik Nikolski');
        insert into performer(name) VALUES('Pupa Lupa');
        insert into performer(name) VALUES('Nina Petrova');
        insert into performer(name) VALUES('Pavel Pavlov');
    """
)

track_list = connection.execute(
    """
    insert into track_list(albom_id, track_name, track_duration) VALUES('1', 'Going Backwards', 300);
    insert into track_list(albom_id, track_name, track_duration) VALUES('2', 'Song On Fire', 100);
    insert into track_list(albom_id, track_name, track_duration) VALUES('3', 'Time for Bedlam', 123);
    insert into track_list(albom_id, track_name, track_duration) VALUES('4', 'The Surprising', 321);
    insert into track_list(albom_id, track_name, track_duration) VALUES('5', 'Heavy', 333);
    insert into track_list(albom_id, track_name, track_duration) VALUES('6', 'feat. Kiiara', 270);
    insert into track_list(albom_id, track_name, track_duration) VALUES('7', 'One More Light', 281);
    insert into track_list(albom_id, track_name, track_duration) VALUES('8', 'Run', 360);
    insert into track_list(albom_id, track_name, track_duration) VALUES('1', 'The Sky Is A Neighborhood', 167);
    insert into track_list(albom_id, track_name, track_duration) VALUES('2', 'Wonderful Wonderful', 215);
    insert into track_list(albom_id, track_name, track_duration) VALUES('3', 'What Lovers Do', 219);
    insert into track_list(albom_id, track_name, track_duration) VALUES('4', 'SAY10', 460);
    insert into track_list(albom_id, track_name, track_duration) VALUES('5', 'KILL4ME', 365);
    insert into track_list(albom_id, track_name, track_duration) VALUES('6', 'Believer', 239);
    insert into track_list(albom_id, track_name, track_duration) VALUES('7', 'Thunder', 100);
    insert into track_list(albom_id, track_name, track_duration) VALUES('9', 'Sad single', 300);
    """
)

music_collection = connection.execute(
    """
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 1', '2015-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 2', '2016-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 3', '2017-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 4', '2018-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 5', '2019-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 6', '2020-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 7', '2021-12-01 11:00:00');
        insert into music_collection(name, year_of_issuse) VALUES('New Year Collection 8', '2022-12-01 11:00:00');
    """
)

performer_music_genre = connection.execute(
    """
    insert into performer_music_genre(performer_id, genre_id) VALUES(1, 1);
    insert into performer_music_genre(performer_id, genre_id) VALUES(2, 2);
    insert into performer_music_genre(performer_id, genre_id) VALUES(3, 3);
    insert into performer_music_genre(performer_id, genre_id) VALUES(4, 4);
    insert into performer_music_genre(performer_id, genre_id) VALUES(5, 5);
    insert into performer_music_genre(performer_id, genre_id) VALUES(6, 1);
    insert into performer_music_genre(performer_id, genre_id) VALUES(7, 2);
    insert into performer_music_genre(performer_id, genre_id) VALUES(8, 3);
    insert into performer_music_genre(performer_id, genre_id) VALUES(9, 1);
    """
)

performer_albom_lis = connection.execute(
    """
    insert into performer_albom_list(performer_id, albom_id) VALUES(1, 1);
    insert into performer_albom_list(performer_id, albom_id) VALUES(2, 2);
    insert into performer_albom_list(performer_id, albom_id) VALUES(3, 3);
    insert into performer_albom_list(performer_id, albom_id) VALUES(4, 4);
    insert into performer_albom_list(performer_id, albom_id) VALUES(5, 5);
    insert into performer_albom_list(performer_id, albom_id) VALUES(6, 6);
    insert into performer_albom_list(performer_id, albom_id) VALUES(7, 7);
    insert into performer_albom_list(performer_id, albom_id) VALUES(8, 8);
    insert into performer_albom_list(performer_id, albom_id) VALUES(9, 9);
    insert into performer_albom_list(performer_id, albom_id) VALUES(9, 1);
    """
)

track_to_collection = connection.execute(
    """
    insert into track_to_collection(track_id, music_collection_id) VALUES(1, 1);
    insert into track_to_collection(track_id, music_collection_id) VALUES(2, 2);
    insert into track_to_collection(track_id, music_collection_id) VALUES(3, 3);
    insert into track_to_collection(track_id, music_collection_id) VALUES(4, 4);
    insert into track_to_collection(track_id, music_collection_id) VALUES(5, 5);
    insert into track_to_collection(track_id, music_collection_id) VALUES(6, 6);
    insert into track_to_collection(track_id, music_collection_id) VALUES(7, 7);
    insert into track_to_collection(track_id, music_collection_id) VALUES(8, 8);
    insert into track_to_collection(track_id, music_collection_id) VALUES(9, 8);
    insert into track_to_collection(track_id, music_collection_id) VALUES(10, 1);
    insert into track_to_collection(track_id, music_collection_id) VALUES(11, 2);
    insert into track_to_collection(track_id, music_collection_id) VALUES(12, 3);
    insert into track_to_collection(track_id, music_collection_id) VALUES(13, 4);
    insert into track_to_collection(track_id, music_collection_id) VALUES(14, 5);
    insert into track_to_collection(track_id, music_collection_id) VALUES(15, 6);
    """
)
