-- Question 1 
-- I think any track with the id 5 will get deleted 
-- Artists with an ID between 20 and 25 will get deleted 
-- A new genre will be inserted in with the valuse given 
-- A new tracvk will be added with all the values given 
-- Update albums that were released in 2021 to where the album id is 3 
-- Update artist to name to the new name given in where the id is 1,2 and 3 

-- Question 2 
-- The tracks table would be one row less 
-- Multiple new rows have been added to the tracks 
-- rerlease year has change in album id 3 to 2021
-- The row does not delete but certain information details are deleted 

-- Question 3

DELETE FROM Tracks 
WHERE track_id = 30;

INSERT INTO Artist (artist_Id, artist_name,) 
VALUES (34, 'Summer Walker'), 
       (35, 'Bryson Tiller');

UPDATE Tracks 
SET duration_ms = 100000
WHERE track_id = 7

-- Question 4 
DELETE FROM Tracks 
WHERE duration_ms < 200000


INSERT INTO Albums (album_id ,album_name, release_year) 
VALUES (34, 'Anniversary ', 2017), 
       (35, 'Over it ', 2019 );
