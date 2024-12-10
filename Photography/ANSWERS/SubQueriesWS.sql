-- Find the lastet photo taken by any photographer 

SELECT date_taken, title
FROM Photos 
WHERE date_taken = (
    SELECT MAX(date_taken)
    FROM Photos);

SELECT date_taken, title
FROM Photos 
ORDER BY date_taken DESC
LIMIT 1;

-- List the photographers who have booked a wedding event

SELECT P.photographer_id, name
FROM Bookings B
JOIN Photographers P ON P.photographer_id = B.photographer_id
WHERE date_booked  = (
    SELECT MIN(date_booked )
    FROM Bookings);

-- Identify clients who have booked a wedding 
 
  SELECT name
  FROM Clients
WHERE client_id  =(SELECT event_type ="Wedding"
FROM Bookings);

SELECT name
FROM Clients
WHERE client_id  IN (
    SELECT client_id
    FROM Bookings
    WHERE event_type ="Wedding"
);

 SELECT client_id
    FROM Bookings
    WHERE event_type ="Wedding";

-- Count the number of photos taken by photographers with more than 5 years of experience.

-- Outer and inner query.Inner query gets evaluated first 
SELECT photographer_id
FROM Photographers
WHERE experience_years > 5;

SELECT COUNT(*)
FROM Photos
WHERE photographer_id IN (
    SELECT photographer_id
    FROM Photographers
    WHERE experience_years > 5
);
