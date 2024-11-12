-- Quesion 1

-- Its most likely goingt to  give an artist name that begins with the letter T and can have as many characters after T 
-- Its most likely going to give Album names and release year from after 2015 in a certain order 
-- Its most likely going to rename album names just as albums but with names of albums still in the coloumns same with release year minus the fact that it will be called year instead of release year.The put the album and year in order from 2015 and later 
-- Its most likely going to output artist name and add a coloum for artist name length with only artist names who have an a as their second character in their name and show haw the length of the characters in their name 

-- Question 2 

-- Any artist whose name starts with 'T' will be in the table no matter the length of their name
-- The significance is that it makes it know that the table of results should be in a certain order 
-- The header name will be slightly changed depending on th einstruction give
-- 

-- Question 3 

SELECT artist_name 
FROM Artists 
WHERE artist_name LIKE '__A%'

SELECT album_name, release_year 
FROM Albums 
WHERE release_year >= 2015 
ORDER BY release_year DESC;

SELECT artist_name, LENGTH(artist_name) AS Name_Length 
FROM Artists 
WHERE artist_name LIKE 'H%';


-- Questionm 4 

SELECT track_name 
FROM Tracks 
WHERE track_name LIKE 'S%e';

SELECT album_name, release_year,2024-release_year AS 'Years since release'
FROM Albums 
WHERE release_year >= 2010;

SELECT artist_name, LENGTH(artist_name) AS Name_Length 
FROM Artists 
WHERE artist_name LIKE '_____';


