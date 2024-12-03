-- Question 1 

-- It will most likely select everything from tracks from album id and also oupt album id from the year 2019 and above 
-- It will most likely select track name  and album name from tracks and album it will only out put if the track id and album id are the same and their realease year is after 2020
-- The same as answer before 
-- select  A.artist_name, COUNT all the rows in T.track_id ,FROM Artists A ,and the join Tracks T ON A.artist_id = T.artist_id ,

-- Question 2 

-- tells the programm where to get the database information from 
-- 




-- Question 3 

SELECT * 
FROM Tracks 
WHERE track_id IN (
  SELECT track_id
  FROM Artists 
  WHERE duration_ms >100000
);

SELECT T.track_id, A.album_id
FROM Tracks T 
JOIN Albums A ON T.album_id = A.album_name
WHERE A.release_year > 2020;

-- Question 4

SELECT artist_name,track_name, genre_name
FROM Artists A ,Tracks T,Genres G 
WHERE artist_name = "Lizzo" 
and T.artist_id = A.artist_id
and T.genre_id =G.genre_id;


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
