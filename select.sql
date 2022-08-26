--количество исполнителей в каждом жанре;
select genre_name, count(genre_name)  from music_genre
full join performer_music_genre on music_genre.id = performer_music_genre.genre_id
group by genre_name;


--количество треков, вошедших в альбомы 2019-2020 годов;
select sum(count(music_collection_id)) over () from album_list
full join track_to_collection on album_list.id = track_to_collection.music_collection_id
where
extract(year from year_of_issuse) between '2019' and '2020';

--select count(music_collection_id) as ctfc from album_list
--full join track_to_collection on album_list.id = track_to_collection.music_collection_id
--where
--extract(year from year_of_issuse) between '2019' and '2020';

--средняя продолжительность треков по каждому альбому
select albom_name, avg(track_duration)  from track_list
full join album_list on track_list.albom_id = album_list.id
group by album_list.id
order by albom_name asc;

--все исполнители, которые не выпустили альбомы в 2020 году;
select performer."name"   from album_list
left join performer_albom_list  on album_list.id = performer_albom_list.albom_id
right  join performer on performer_albom_list.performer_id = performer.id
where
extract(year from year_of_issuse) != '2020';

--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select music_collection."name"  from performer
left join performer_albom_list on performer.id = performer_albom_list.performer_id
left join album_list on performer_albom_list.albom_id = album_list.id
left join track_list on album_list.id = track_list.albom_id
left join track_to_collection on track_list.id  = track_to_collection.track_id
left join music_collection on track_to_collection.music_collection_id = music_collection.id
where performer."name" = 'Kira';

--название альбомов, в которых присутствуют исполнители более 1 жанра;
select albom_name  from album_list
inner join performer_albom_list on album_list.id = performer_albom_list.albom_id
inner join performer on  performer_albom_list.performer_id = performer.id
inner join performer_music_genre on performer.id = performer_music_genre.performer_id
inner join music_genre on performer_music_genre.genre_id = music_genre.id
group by music_genre, albom_name
having count(music_genre) > 1;

--наименование треков, которые не входят в сборники;
select track_name  from track_list
full join track_to_collection on track_list.id  = track_to_collection.track_id
where track_to_collection.track_id is null;

--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select performer."name"  from track_list
left join album_list on track_list.albom_id  = album_list.id
left join performer_albom_list on album_list.id = performer_albom_list.albom_id
left join performer on performer_albom_list.performer_id = performer.id
where track_duration = (select min(track_duration) as small_track from track_list);

--название альбомов, содержащих наименьшее количество треков.
select albom_name  from album_list
left join track_list on album_list.id = track_list.albom_id
where albom_id in (
select albom_id from
(select  count(id) as c_id, albom_id  from track_list
GROUP by albom_id) as count_t_a
where count_t_a.c_id = (select min(c_id) from
(select  count(id) as c_id, albom_id  from track_list
GROUP by albom_id) as min_count_track_albom));
