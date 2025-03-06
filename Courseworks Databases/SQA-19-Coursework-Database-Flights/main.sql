DESCRIBE ALL TABLES;


-- SELECT forename,surname,COUNT(adultTicket) * 5.5 + COUNT(childticket) * 2.0 + COUNT(concessionTicket) * 1.5 AS "Tax"
-- FROM Customer, Booking 
-- WHERE flightID LIKE '%QH182%';

SELECT forename,surname
FROM Customer C, Booking B
WHERE C.customerID = B.customerID 
AND B.childticket =
    
    (SELECT MAX(childticket) AS 'Max children'
    FROM Booking
    );

-- SELECT * 
-- FROM Booking;
