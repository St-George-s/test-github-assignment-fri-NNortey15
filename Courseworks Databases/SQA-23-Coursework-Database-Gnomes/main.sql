-- SELECT gnomeName, SUM(quantity) 
-- FROM Gnome G,Gnomepurchase P  
-- WHERE G.description LIKE "%solar%" 
-- and G.gnomeid = P.gnomeid 
-- GROUP BY gnomeName 
-- ORDER BY sum(quantity) DESC; 

SELECT C.emailAddress, CO.orderID, GP.quantity
FROM Customer C
Join Orders CO ON CO.customerID = C.customerID
Join  GnomePurchase GP ON CO.orderID = GP.orderID
Join  Gnome G ON G.gnomeid = GP.gnomeid
WHERE quantity >= 3 AND unitPrice=
    (
        SELECT max(unitPrice)
        FROM gnome
    );


SELECT forename, surname, SUM(quantity * unitPrice * 1.2) AS [Total to Pay]
FROM Customer, Gnome, GnomePurchase, Orders
WHERE Orders.orderID = "ord0024"
AND Customer.customerID = Orders.customerID
AND Orders.orderID = GnomePurchase.orderID
AND Gnome.gnomeID = GnomePurchase.gnomeID
GROUP BY forename, surname;
