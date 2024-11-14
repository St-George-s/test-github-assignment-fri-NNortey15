-- SELECT P.photographer_id, name
-- FROM Bookings B
-- JOIN Photographers P ON P.photographer_id = B.photographer_id
-- WHERE date_booked  = (
--     SELECT MIN(date_booked )
--     FROM Bookings);

-- SELECT name
-- FROM Clients
-- WHERE client_id  =(SELECT event_type ="Wedding"
-- FROM Bookings);

-- SELECT name
-- FROM Clients
-- WHERE client_id  IN (
--     SELECT client_id
--     FROM Bookings
--     WHERE event_type ="Wedding"
-- );

--  SELECT client_id
--     FROM Bookings
--     WHERE event_type ="Wedding";

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