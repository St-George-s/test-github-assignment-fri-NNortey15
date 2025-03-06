SELECT genre_name, COUNT(T.track_id)
FROM Albums A ,Tracks T,Genres G 
WHERE A.release_year = 2017
and T.album_id = A.album_id
and T.genre_id =G.genre_id
GROUP BY genre_name;

SELECT genre_name, T.track_name
FROM Albums A ,Tracks T,Genres G 
WHERE A.release_year = 2017
and T.album_id = A.album_id
and T.genre_id =G.genre_id;