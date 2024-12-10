-- Question 1

-- get an artist name 



-- Get all details from albulm 



-- Get tracks where duration is in the 200000



-- give all albums that were released before 2018

-- Question 2 

-- SELECT artist_name FROM Artists; gives one field whereas SELECT * FROM Artists; gives everything about the artist 
--  SELECT * FROM Albums; gives all the dtails about the albulms
--  The significance of the where in SELECT * FROM Tracks WHERE duration_ms > 200000; is that it allows it to filter the results 
--  SELECT album_name FROM Albums WHERE release_year > 2018; it changes compared to not having the where in the clause because it would give all the albums but with where it gives only before 2018 

-- Question 3

--  SELECT artist_Id FROM Artists;
--  SELECT album_name FROM Albums WHERE release_year > 2017;
--  SELECT * FROM Tracks WHERE duration_ms > 100000

-- Question 4 

SELECT artist_name 
FROM Artists;

SELECT album_name 
FROM Albums 
WHERE release_year > 2017;

SELECT * 
   FROM Tracks 
   WHERE duration_ms > 100000;

-- Question 5 

SELECT track_names
FROM tracks 

SELECT album_name
FROM Albums 
WHERE release_year >2010;

SELECT artist_name
From Artist 
WHERE artist_Id < 10:
