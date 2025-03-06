-- Question 1 

-- Its most likely going to count the number of rows inthe tracks category 
-- It is most likely going count all the rows in genre id 1 and out put the amount of tracks in genre id 1 
-- It is most likely going get an average of  all the durations in genre id 1 from tracks

-- Question 2 

-- the amount of tracks in genre id 

-- For all the tracks under one genre id for example one it will calculate the average of duration for each group 

-- Question 3 

SELECT COUNT(track_id)
FROM Tracks;

SELECT album_id, COUNT(*)
FROM Tracks 
GROUP BY album_id;

SELECT genre_id, max(duration_ms)
FROM Tracks 
GROUP BY genre_id;

-- Question 4 

SELECT album_id, SUM(duration_ms)
FROM Tracks 
GROUP BY album_id;


SELECT  AVG(duration_ms)
FROM Tracks;
