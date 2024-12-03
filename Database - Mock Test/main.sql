<<<<<<< HEAD
-- SELECT eventname,name, maxAttendees, eventDate
-- FROM Shop S,Event E
-- Where S.shopid =E.shopid;

-- SELECT  name,eventname
-- FROM Shop S,
-- JOIN Event E ON S.shopid = E.shopid
-- Where eventDate = 2024-12-25;


UPDATE OpeningTime 
SET closeTime = '19:00'
WHERE date = '2024-12-24' AND shopid = (
    SELECT  shopid
    FROM shop S
    WHERE S.name = 'Zara'
    );


SELECT name AS 'Shop Name', COUNT(bookingID) AS 'Total Bookings'
FROM Shop, Booking, event
WHERE Shop.shopID = Event.eventID
AND Event.eventID = Booking.eventID
GROUP BY name;


=======
DESCRIBE ALL TABLES;
>>>>>>> 6c99ea2 (Mock DB Test)
